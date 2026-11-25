"""Apply measured DSS context clarifications without changing raw model caches."""
import argparse
from html import escape
import json
from pathlib import Path
import re

from doc4cf.context import _atomic_json, inventory_digest, validate_dataset_context

CL_SOURCE = "https://github.com/ETCBC/dss/blob/3a9ab5b5df4dba72f2179016e8163b61c0a1752d/tf/2.0.4/cl.tf"
CL_DESCRIPTION = (
    "The cl feature records a morphological class tag on word nodes in the Dead Sea Scrolls corpus. "
    "Its metadata identifies Martin Abegg's data files as the source. Attested values include cmn and prep. "
    "Missing assignments mean no tag is recorded. Corpus credits and the Creative Commons "
    "Attribution-NonCommercial license remain recorded separately in the source metadata."
)
LEXO_SOURCE = "https://github.com/ETCBC/dss/blob/3a9ab5b5df4dba72f2179016e8163b61c0a1752d/tf/2.0.4/otext.tf"
LEXO_APP_SOURCE = "https://github.com/ETCBC/dss/blob/3a9ab5b5df4dba72f2179016e8163b61c0a1752d/app/config.yaml"
LEXO_DESCRIPTION = (
    "The lexo feature records an original-source lexeme representation on lex and word nodes. "
    "The app lists it as a bare display feature for lex nodes. The TF configuration includes it in "
    "lex-default, with template word#{lang:h}-{lex}-{lexe}-{lexo}. The surface-text template "
    "text-orig-full uses glyph, punc, and after. Missing assignments indicate no recorded value."
)
NOTE_SOURCE = "https://github.com/ETCBC/dss/blob/3a9ab5b5df4dba72f2179016e8163b61c0a1752d/tf/2.0.4/note_etcbc.tf"
NOTE_DESCRIPTION = (
    "The note_etcbc feature stores editorial notes on word nodes. The source description attributes the notes "
    "to Thijs Amersfoort for 11Q19 and 1Qisaa, and Saulo de Oliveira Cantanhêde for 1QpHab, during "
    "morphological parsing. Values such as Afgebroken and Weer afgebroken are free-text comments. "
    "Missing assignments indicate that no note is recorded."
)
OTEXT_DESCRIPTION = (
    "The otext configuration defines the Text API's section labels and rendering templates for the DSS corpus. "
    "The section features are scroll, fragment, and line. Formats include Unicode text, original-source text, "
    "and ETCBC transliteration; text-trans-full uses glyphe, punce, and after. These declarations configure "
    "presentation and referencing rather than storing node-level annotations."
)
PS_SOURCE = "https://github.com/ETCBC/dss/blob/3a9ab5b5df4dba72f2179016e8163b61c0a1752d/tf/2.0.4/ps_etcbc.tf"
PS_DESCRIPTION = (
    "The ps_etcbc feature assigns string codes to word nodes in the DSS additions. Attested values include "
    "NA and p3. The metadata describes BHSA-based additions but does not supply a code-to-category mapping. "
    "A parallel-scheme relationship to ps is inferred in the context artifacts; it does not establish "
    "equivalence between their value sets."
)
PUNCO_SOURCE = "https://github.com/ETCBC/dss/blob/3a9ab5b5df4dba72f2179016e8163b61c0a1752d/tf/2.0.4/punco.tf"
PUNCO_DESCRIPTION = (
    "The punco feature records trailing punctuation in the original-source rendering on word nodes. "
    "The declared templates pair it with glypho in text-source-full, glexo in lex-source-full, and morpho "
    "in morph-source-full; each also uses after. Observed values include . and ±. Missing assignments "
    "mean no punctuation value is recorded."
)
ASSOCIATIONS = re.compile(
    r'<section class="correlated-features">.*?</section>'
    r'|<details class="feature-associations">.*?</details>'
    r'|<aside class="association-limits">.*?</aside>', re.DOTALL)
INFERRED_HTML = re.compile(r'<section class="inferred-description"[^>]*>.*?</section>', re.DOTALL)
INFERRED_MARKDOWN = re.compile(
    r'## (?:Generated|Reviewed) description\n\n.*?\n\*AI-assisted[^\n]*\*\n', re.DOTALL)


def preserve_measurements(baseline: Path, output: Path, *, allow_legacy: bool = False) -> bool:
    """Carry forward measured reference material only for matching corpus facts."""
    if baseline.resolve() == output.resolve() or not baseline.is_dir():
        return False
    current = json.loads((output / "context_review.json").read_text(encoding="utf-8"))
    if not isinstance(current.get("inventory_sha256"), str) or not current["inventory_sha256"]:
        return False
    prior_review = baseline / "context_review.json"
    if prior_review.is_file():
        prior = json.loads(prior_review.read_text(encoding="utf-8"))
        if prior.get("inventory_sha256") != current.get("inventory_sha256"):
            return False
    elif not allow_legacy:
        return False
    pages = sorted((output / "features").glob("*.html"))
    if {p.name for p in pages} != {p.name for p in (baseline / "features").glob("*.html")}:
        return False
    changes = {}
    for page in pages:
        original = (baseline / "features" / page.name).read_text(encoding="utf-8")
        generated = page.read_text(encoding="utf-8")
        if ASSOCIATIONS.sub("", INFERRED_HTML.sub("", original)) != ASSOCIATIONS.sub("", INFERRED_HTML.sub("", generated)):
            return False
        retained = "".join(match.group() for match in ASSOCIATIONS.finditer(original))
        text = ASSOCIATIONS.sub("", generated)
        anchor = '<section class="feature-app-details">'
        if anchor not in text:
            anchor = '<details><summary>Source metadata</summary>'
        if retained and anchor not in text:
            return False
        changes[page] = text.replace(anchor, retained + anchor, 1) if retained else text
        old_md = baseline / "markdown/features" / f"{page.stem}.md"
        new_md = output / "markdown/features" / f"{page.stem}.md"
        if old_md.is_file() and new_md.is_file():
            text = INFERRED_MARKDOWN.sub("", old_md.read_text(encoding="utf-8"))
            model = INFERRED_MARKDOWN.search(new_md.read_text(encoding="utf-8"))
            if model:
                section = re.search(r"^#{2,3} ", text, re.MULTILINE)
                position = section.start() if section else len(text)
                text = text[:position].rstrip() + "\n\n" + model.group().strip() + "\n\n" + text[position:]
            changes[new_md] = text
    for filename in ("index.md", "features.md"):
        previous = baseline / "markdown" / filename
        if previous.is_file() and (output / "markdown" / filename).is_file():
            changes[output / "markdown" / filename] = previous.read_text(encoding="utf-8")
    for path, text in changes.items():
        path.write_text(text, encoding="utf-8")
    return True


def apply_site_notes(output: Path, baseline: Path | None = None) -> None:
    """Apply source-cited DSS feature clarifications, preserving raw responses."""
    if baseline is not None:
        preserve_measurements(baseline, output)
    if "Dead Sea Scrolls" not in (output / "index.html").read_text(encoding="utf-8"):
        raise ValueError("Expected a generated DSS reference")
    notes = (
        ("cl", CL_DESCRIPTION, (("pinned DSS cl feature header", CL_SOURCE),)),
        ("lexo", LEXO_DESCRIPTION, (("pinned DSS text formats", LEXO_SOURCE),
                                    ("pinned DSS app configuration", LEXO_APP_SOURCE))),
        ("note_etcbc", NOTE_DESCRIPTION, (("pinned DSS note_etcbc feature header", NOTE_SOURCE),)),
        ("otext", OTEXT_DESCRIPTION, (("pinned DSS text formats", LEXO_SOURCE),)),
        ("ps_etcbc", PS_DESCRIPTION, (("pinned DSS ps_etcbc feature header", PS_SOURCE),)),
        ("punco", PUNCO_DESCRIPTION, (("pinned DSS punco feature header", PUNCO_SOURCE),
                                      ("pinned DSS text formats", LEXO_SOURCE))),
    )
    for feature, description, references in notes:
        page = output / "features" / f"{feature}.html"
        if not page.is_file():
            continue
        html = page.read_text(encoding="utf-8")
        if 'class="inferred-description"' not in html or f'data-editorial-feature="{feature}"' in html:
            continue
        source = ('<p class="editorial-source">Editorial clarification: '
                  + "; ".join(f'<a href="{url}" rel="noopener noreferrer">{label}</a>'
                              for label, url in references) + '.</p>')
        html, changed = re.subn(
            r'<section class="inferred-description"><h2>Description (.*?)</h2><p>.*?</p></section>',
            f'<section class="inferred-description" data-editorial-feature="{feature}">'
            + r'<h2>Reviewed description \1</h2>' + f'<p>{escape(description)}</p>{source}</section>',
            html, count=1, flags=re.DOTALL)
        if not changed:
            raise ValueError(f"Could not locate the generated {feature} description")
        page.write_text(html, encoding="utf-8")
        path = output / "markdown/features" / f"{feature}.md"
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            note = (description + '\n\nEditorial clarification: '
                    + "; ".join(f'[{label}]({url})' for label, url in references) + '.\n')
            text = re.sub(r'## Generated description\n\n.*?\n\n(\*AI-assisted[^\n]*\*)',
                          '## Reviewed description\n\n' + note + r'\n\1', text, count=1, flags=re.DOTALL)
            path.write_text(text, encoding="utf-8")
        path = output / "audit.html"
        text = path.read_text(encoding="utf-8")
        note = (f'<section class="editorial-{feature}"><h2>{feature} clarification</h2>'
                f'<p>The <a href="features/{feature}.html">{feature} description</a> was clarified against '
                'the pinned sources. The raw model cache and original uncertainty flags are retained.</p>'
                + source + '</section>')
        path.write_text(text.replace('<h1>Audit report</h1>', '<h1>Audit report</h1>' + note, 1), encoding="utf-8")


def apply_notes(folder: Path) -> None:
    """Remove unsupported edge-presence and date inferences from DSS context."""
    inventory = json.loads((folder / "inventory.json").read_text(encoding="utf-8"))
    path = folder / "dataset_context.json"
    dataset = json.loads(path.read_text(encoding="utf-8"))
    if inventory.get("dataset", {}).get("acronym") != "dss":
        raise ValueError("Expected the DSS inventory")
    if dataset.get("inventory_sha256") != inventory_digest(inventory):
        raise ValueError("Dataset context does not match the DSS inventory")
    occ = inventory["features"]["occ"]
    if not (occ["kind"] == "edge" and occ["sources"].get("lex") and occ["targets"].get("word")):
        raise ValueError("Expected measured lexeme-to-word occurrence links")
    additions = [{
        "claim": ("Editorial clarification: occ has measured links from lex nodes to word nodes. "
                  "Its empty scalar-value inventory does not mean the edge is unpopulated."),
        "status": "verified",
        "evidence": ["features.occ.sources", "features.occ.targets", "features.occ.distinct_values"],
    }]
    dated_features = ("g_cons", "g_lex_etcbc")
    if all(inventory["features"][name]["metadata"].get("dateWritten", "").startswith("2026-11-04")
           for name in dated_features):
        additions.append({
            "claim": ("Editorial clarification: g_cons and g_lex_etcbc record a metadata date of "
                      "2026-11-04. These timestamps alone do not establish a data-currency problem."),
            "status": "verified",
            "evidence": [f"features.{name}.metadata.dateWritten" for name in dated_features],
        })
    prefixes = ("Feature occ reports distinct_values 0",)
    if len(additions) == 2:
        prefixes += ("Some dss-additions feature metadata carry createdDate/dateWritten in 2026",)
    dataset["ambiguities"] = [item for item in dataset["ambiguities"] if not item.startswith(prefixes)]
    existing = {item["claim"] for item in dataset["conventions"]}
    dataset["conventions"] += [item for item in additions if item["claim"] not in existing]
    dataset["needs_review"] = bool(dataset["ambiguities"])
    validate_dataset_context({key: dataset[key] for key in (
        "dataset_profile", "conventions", "ambiguities", "needs_review")})
    _atomic_json(path, dataset)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("mode", choices=("context", "site"), nargs="?", default="context")
    parser.add_argument("baseline", type=Path, nargs="?")
    args = parser.parse_args()
    if args.mode == "context":
        apply_notes(args.path)
    else:
        apply_site_notes(args.path, args.baseline)
    print("Applied DSS editorial clarifications; raw model cache unchanged.")
