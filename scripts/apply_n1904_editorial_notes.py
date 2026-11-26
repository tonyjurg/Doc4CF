"""Apply source-cited N1904 clarifications after generating a complete reference."""
import argparse
from html import escape
from pathlib import Path
import re

SOURCE = "https://github.com/CenterBLC/N1904/blob/3f53a5a9075cbca5c3001a000a7b004cdee251b6/docs/tutorial/louw-nida.ipynb"
DESCRIPTION = (
    "The ln feature records Louw–Nida semantic-domain classifications. Values are strings and may contain "
    "several space-separated codes, so equality tests and code-membership tests answer different questions. "
    "For word counts, restrict the selection to word nodes: this corpus also records ln on phrases and subphrases."
)
SHORT_DESCRIPTION = "Louw–Nida semantic-domain codes (editorial clarification)"
VERSE_SOURCE = "https://github.com/CenterBLC/N1904/blob/3f53a5a9075cbca5c3001a000a7b004cdee251b6/docs/features/verse.md"
VERSE_DESCRIPTION = (
    "The verse feature records the verse number within a chapter, derived from the XML ref attribute. "
    "On verse nodes it identifies the verse itself; on word nodes it indicates the containing verse. "
    "On other populated node types it records the verse where the item begins. A sentence can span "
    "several verses, so this annotation does not establish verse containment. Verse numbers can have gaps."
)


def clarify_verse(output: Path) -> None:
    """Distinguish a starting-verse annotation from measured containment."""
    page = output / "features" / "verse.html"
    if not page.is_file():
        return
    html = page.read_text(encoding="utf-8")
    source = (f'<p class="editorial-source">Editorial clarification: <a href="{VERSE_SOURCE}" '
              'rel="noopener noreferrer">pinned N1904 verse documentation</a>.</p>')
    if 'data-editorial-feature="verse"' not in html:
        replacement = ('<section class="inferred-description" data-editorial-feature="verse">'
                       r'<h2>Reviewed description \1</h2>'
                       f'<p>{escape(VERSE_DESCRIPTION)}</p>{source}</section>')
        html, changed = re.subn(
            r'<section class="inferred-description"><h2>Description (.*?)</h2><p>.*?</p></section>',
            replacement, html, count=1, flags=re.DOTALL)
        if not changed:
            note = ('<section class="editorial-description" data-editorial-feature="verse">'
                    f'<h2>Editorial description</h2><p>{escape(VERSE_DESCRIPTION)}</p>{source}</section>')
            html = html.replace('<details><summary>Source metadata</summary>',
                                note + '<details><summary>Source metadata</summary>', 1)
        page.write_text(html, encoding="utf-8")
    path = output / "markdown" / "features" / "verse.md"
    if path.is_file():
        text = path.read_text(encoding="utf-8")
        if f']({VERSE_SOURCE})' not in text:
            note = f'{VERSE_DESCRIPTION}\n\nEditorial clarification: [pinned N1904 verse documentation]({VERSE_SOURCE}).\n'
            text, changed = re.subn(
                r'## Generated description\n\n.*?\n\n(\*AI-assisted[^\n]*\*)',
                '## Reviewed description\n\n' + note + r'\n\1', text, count=1, flags=re.DOTALL)
            if not changed:
                text = text.replace('## Description\n', '## Editorial description\n\n' + note + '\n## Description\n', 1)
            path.write_text(text, encoding="utf-8")
    path = output / "audit.html"
    text = path.read_text(encoding="utf-8")
    if 'class="editorial-verse"' not in text:
        note = ('<section class="editorial-verse"><h2>Verse-number clarification</h2>'
                '<p>The <a href="features/verse.html">verse description</a> was clarified against the pinned '
                'upstream feature documentation. The raw model cache and original uncertainty flags are retained.</p>'
                + source + '</section>')
        path.write_text(text.replace('<h1>Audit report</h1>', '<h1>Audit report</h1>' + note, 1), encoding="utf-8")


def apply_notes(output: Path) -> None:
    """Clarify ln and verse without altering source metadata or raw model caches."""
    page = output / "features" / "ln.html"
    index = output / "index.html"
    if not page.is_file() or "Greek New Testament (Nestle 1904)" not in index.read_text(encoding="utf-8"):
        raise ValueError("Expected a generated N1904 reference with an ln feature page")
    html = page.read_text(encoding="utf-8")
    source = f'<p class="editorial-source">Editorial clarification: <a href="{SOURCE}" rel="noopener noreferrer">pinned N1904 Louw–Nida tutorial</a>.</p>'
    pattern = r'<section class="inferred-description"><h2>Description (.*?)</h2><p>.*?</p></section>'
    replacement = ('<section class="inferred-description" data-editorial-feature="ln"><h2>Reviewed description '
                   + r'\1' + f'</h2><p>{escape(DESCRIPTION)}</p>{source}</section>')
    if 'data-editorial-feature="ln"' not in html:
        html, changed = re.subn(pattern, replacement, html, count=1, flags=re.DOTALL)
        if not changed:
            note = f'<section class="editorial-description" data-editorial-feature="ln"><h2>Editorial description</h2><p>{escape(DESCRIPTION)}</p>{source}</section>'
            html = html.replace('<details><summary>Source metadata</summary>', note + '<details><summary>Source metadata</summary>', 1)
        page.write_text(html, encoding="utf-8")
    for filename in ("index.md", "features.md"):
        path = output / "markdown" / filename
        if path.is_file():
            text = path.read_text(encoding="utf-8").replace('| [ln](features/ln.md) | node | ln |',
                                                        f'| [ln](features/ln.md) | node | {SHORT_DESCRIPTION} |')
            path.write_text(text, encoding="utf-8")
    path = output / "markdown" / "features" / "ln.md"
    if path.is_file():
        text = path.read_text(encoding="utf-8")
        note = f'{DESCRIPTION}\n\nEditorial clarification: [pinned N1904 Louw–Nida tutorial]({SOURCE}).\n'
        if f']({SOURCE})' not in text:
            text, changed = re.subn(r'## Generated description\n\n.*?\n\n(\*AI-assisted[^\n]*\*)',
                                    '## Reviewed description\n\n' + note + r'\n\1', text, count=1, flags=re.DOTALL)
            if not changed:
                text = text.replace('## Description\n', '## Editorial description\n\n' + note + '\n## Description\n', 1)
        path.write_text(text, encoding="utf-8")
    path = output / "features.html"
    text = path.read_text(encoding="utf-8").replace(
        '<a href="features/ln.html">ln</a></td><td>node</td><td>ln</td>',
        f'<a href="features/ln.html">ln</a></td><td>node</td><td>{SHORT_DESCRIPTION}</td>')
    path.write_text(text, encoding="utf-8")
    path = output / "audit.html"
    text = path.read_text(encoding="utf-8")
    note = ('<section class="editorial-clarifications"><h2>Editorial clarifications</h2>'
            '<p>The <a href="features/ln.html">ln description</a> was clarified against the pinned upstream tutorial. '
            'The raw model cache and its original uncertainty flags are retained for traceability.</p>' + source + '</section>')
    if 'class="editorial-clarifications"' not in text:
        path.write_text(text.replace('<h1>Audit report</h1>', '<h1>Audit report</h1>' + note, 1), encoding="utf-8")
    clarify_verse(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    apply_notes(parser.parse_args().output)
    print("Applied the source-cited N1904 ln and verse clarifications.")
