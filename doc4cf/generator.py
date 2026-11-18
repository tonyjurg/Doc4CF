"""Build an offline corpus reference from Context-Fabric."""
import argparse
from collections.abc import Sequence
from collections import Counter
from hashlib import sha256
from html import escape
import json
import logging
import os
import time
import random
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from urllib.error import HTTPError, URLError
from numbers import Integral
from pathlib import Path
import shutil
from tempfile import NamedTemporaryFile, TemporaryDirectory
from typing import Any, cast
import unicodedata
from urllib.parse import quote, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from cfabric.core import Fabric


logger = logging.getLogger(__name__)


def header(path: Path) -> dict[str, Any]:
    """Read a Text-Fabric header and return its kind, metadata, and encoding."""
    # Decode the entire source strictly before claiming UTF-8.
    raw = path.read_bytes()
    lines = raw.decode("utf-8-sig").splitlines()
    if not lines:
        raise ValueError(f"{path.name} is empty; expected a Text-Fabric feature file")
    meta = {}
    for line in lines[1:]:
        if not line.startswith("@"):
            break
        key, _, value = line[1:].partition("=")
        meta[key] = value
    return dict(kind=lines[0].lstrip("@"), meta=meta,
                encoding="UTF-8 with BOM" if raw.startswith(b"\xef\xbb\xbf") else "UTF-8")


class _NoRedirect(HTTPRedirectHandler):
    """Refuse redirects: urllib would forward API-key headers to the new host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_OPENER = build_opener(_NoRedirect)


def urlopen(req: Request, timeout: float | None = None) -> Any:
    """Open ``req`` without following redirects.

    The provider endpoints are fixed HTTPS URLs and answer directly, so a
    redirect surfaces as ``HTTPError`` instead of sending credentials elsewhere.
    """
    return _OPENER.open(req, timeout=timeout)


RETRYABLE_STATUS = (408, 500, 502, 503, 504)


def write_atomic(path: Path, text: str, mode: int = 0o644) -> None:
    """Write ``text`` to ``path`` through a temporary file in the same directory.

    ``NamedTemporaryFile`` creates files readable only by their owner, so ``mode``
    is applied explicitly: site output stays readable by a web server, while
    private caches can pass ``0o600``. The temporary file is removed on failure.
    """
    tmp = NamedTemporaryFile(dir=path.parent, mode="w", encoding="utf-8", delete=False)
    tmp_path = Path(tmp.name)
    try:
        with tmp:
            tmp.write(text)
        tmp_path.chmod(mode)
        tmp_path.replace(path)
    except BaseException:
        tmp_path.unlink(missing_ok=True)
        raise


def _raise_if_daily_quota(body):
    """Raise RuntimeError when a 429 body reports an exhausted OpenRouter daily quota."""
    try:
        metadata = json.loads(body.decode("utf-8")).get("error", {}).get("metadata", {})
        exhausted = metadata.get("limit_source") == "openrouter_free_tier_daily"
        reset_ms = (metadata.get("headers") or {}).get("X-RateLimit-Reset")
    except (ValueError, AttributeError):
        return
    if not exhausted:
        return
    try:
        reset_time = datetime.fromtimestamp(int(reset_ms) / 1000, tz=UTC).astimezone()
    except (ValueError, TypeError, OverflowError, OSError):
        raise RuntimeError(
            "OpenRouter daily free-model quota exhausted. "
            "Check your account for the reset time."
        ) from None
    raise RuntimeError(
        "OpenRouter daily free-model quota exhausted. "
        f"Quota resets at {reset_time:%Y-%m-%d %H:%M %Z}. "
        "Previously generated descriptions remain cached."
    )


def _retry_delay(retry_after, attempt, base_delay, max_delay):
    """Return seconds to wait before a retry, never more than ``max_delay``.

    ``Retry-After`` (seconds or an HTTP date) is honored but capped, so a server
    cannot make the build sleep for hours. Without it, use exponential backoff.
    """
    delay = None
    if retry_after:
        try:
            delay = max(0.0, float(retry_after))
        except ValueError:
            try:
                retry_date = parsedate_to_datetime(retry_after)
                if retry_date.tzinfo is None:
                    retry_date = retry_date.replace(tzinfo=UTC)
                delay = max(0.0, (retry_date - datetime.now(UTC)).total_seconds())
            except (TypeError, ValueError, OverflowError):
                pass
    if delay is None:
        delay = min(max_delay, base_delay * (2 ** attempt))
        delay += random.uniform(0, min(2, delay * 0.1))
    return min(max_delay, delay)


def request_with_retry(
    req: Request, timeout: float = 90, max_retries: int = 6,
    base_delay: float = 5, max_delay: float = 120,
) -> dict[str, Any]:
    """Return a decoded JSON response, retrying rate limits and transient failures.

    HTTP 429, 408 and 5xx responses and network errors are retried. The delay
    follows ``Retry-After`` when present, otherwise bounded exponential backoff;
    either way it never exceeds ``max_delay``. OpenRouter free-tier daily quota
    exhaustion is raised immediately because retrying cannot succeed before the
    quota reset. Other HTTP errors are raised unchanged.
    """
    for attempt in range(max_retries + 1):
        try:
            with urlopen(req, timeout=timeout) as response:
                return json.load(response)
        except HTTPError as error:
            # The body can be read only once, so read it here and reuse it.
            try:
                body = error.read()
            except OSError:
                body = b""
            if error.code == 429:
                _raise_if_daily_quota(body)
                if attempt == 0:
                    logger.warning("Rate-limit response: %s", body.decode("utf-8", errors="replace"))
                    logger.warning("Rate-limit headers:")
                    for name in ("Retry-After", "X-RateLimit-Limit",
                                 "X-RateLimit-Remaining", "X-RateLimit-Reset"):
                        logger.warning("  %s: %s", name, error.headers.get(name))
            if (error.code != 429 and error.code not in RETRYABLE_STATUS) or attempt == max_retries:
                raise
            delay = _retry_delay(error.headers.get("Retry-After"), attempt, base_delay, max_delay)
            reason = f"HTTP {error.code}"
        except (URLError, TimeoutError) as error:
            if attempt == max_retries:
                raise
            delay = _retry_delay(None, attempt, base_delay, max_delay)
            reason = f"Network error ({getattr(error, 'reason', error)})"

        logger.info("%s: retrying in %.1f seconds (attempt %d/%d).",
                    reason, delay, attempt + 1, max_retries)
        time.sleep(delay)

    raise RuntimeError("HTTP retry loop ended unexpectedly")


def request_with_completion_retry(
    req: Request, timeout: float = 90, max_token_retries: int = 2,
) -> dict[str, Any]:
    """Retry a completion only when the provider truncates it at its token limit.

    Each retry doubles the request's ``max_tokens`` budget. Other failures,
    including content-filter responses, are returned to the caller unchanged.
    """
    request_data = json.loads(cast(bytes, req.data).decode("utf-8"))
    token_budget = request_data.get("max_tokens")
    if not isinstance(token_budget, int) or token_budget < 1:
        return request_with_retry(req, timeout=timeout)

    for attempt in range(max_token_retries + 1):
        if attempt:
            request_data["max_tokens"] = token_budget
            req = Request(
                req.full_url,
                data=json.dumps(request_data, ensure_ascii=False).encode("utf-8"),
                headers=req.headers,
                origin_req_host=req.origin_req_host,
                unverifiable=req.unverifiable,
                method=req.get_method(),
            )
        reply = request_with_retry(req, timeout=timeout)
        choice = reply.get("choices", [{}])[0] if reply.get("choices") else {}
        truncated = (
            choice.get("finish_reason") == "length"
            or reply.get("stop_reason") == "max_tokens"
        )
        if not truncated or attempt == max_token_retries:
            return reply
        token_budget *= 2
        logger.info("Completion was truncated at the output-token limit; retrying with max_tokens=%s.",
                    f"{token_budget:,}")
    raise RuntimeError("Completion retry loop ended unexpectedly")

def e(value: object) -> str:
    """Escape a value for safe insertion into an HTML text or attribute."""
    return escape(str(value), quote=True)


def table(headings: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    """Render a table from headings and pre-rendered cell contents."""
    head = "".join(f"<th>{e(h)}</th>" for h in headings)
    body = "".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows)
    return f"<div class=scroll><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>"


def link(url: str, label: str) -> str:
    """Render an HTML link, escaping its URL and visible label."""
    return f'<a href="{e(url)}">{e(label)}</a>'


def feature(name: str) -> str:
    """Link to the generated reference page for a feature name."""
    return link(f"features/{quote(name)}.html", name)


def check_project_home(project_home: str | None) -> str | None:
    """Return ``project_home`` if it is a relative path or an http(s) URL.

    Schemes such as ``javascript:`` or ``data:`` would become a clickable link
    on every generated page, so they are rejected.
    """
    if project_home:
        scheme = urlsplit(project_home).scheme.lower()
        if scheme not in ("", "http", "https"):
            raise ValueError(
                f"--project-home must be a relative path or an http(s) URL, not {scheme}:"
            )
    return project_home


def write_page(
    out: Path, filename: str, title: str, body: str, corpus: str,
    project_home: str | None = None,
) -> None:
    """Write one complete responsive HTML page with corpus navigation.

    Relative asset paths are calculated from the page location so nested
    feature pages can share root-level styles and scripts.
    """
    prefix = "../" * (len(Path(filename).parts) - 1)
    check_project_home(project_home)
    if project_home and not (urlsplit(project_home).scheme or project_home.startswith("/")):
        project_home = prefix + project_home
    footer = f'<footer class="project-credit">Generated with <a href="{e(project_home)}"><img src="{prefix}doc4cf-logo.svg" width="26" height="26" alt="">Doc4CF</a></footer>' if project_home else ""
    logo = f'<img src="{prefix}doc4cf-logo-reversed.svg" width="38" height="38" alt="Doc4CF">'
    brand = f'<a class="header-logo" href="{prefix}index.html" aria-label="{e(corpus)} overview">{logo}</a>'
    nav = " ".join(link(prefix + url, label) for url, label in [
        ("index.html", "Overview"), ("features.html", "Features"),
        ("structure.html", "Structure"), ("text.html", "Text & encoding")])
    (out / filename).write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)} · {e(corpus)}</title>
<link rel="stylesheet" href="{prefix}style.css"><script defer src="{prefix}browse.js"></script></head>
<body><header>{brand}<nav aria-label="Corpus navigation">{nav}</nav></header>
<main><small>{e(corpus)}</small><h1>{e(title)}</h1>{body}</main>{footer}</body></html>""", encoding="utf-8")


PROVIDERS = {
    "anthropic": ("Anthropic", "ANTHROPIC_API_KEY", "https://api.anthropic.com/v1/messages"),
    "openrouter": ("OpenRouter", "OPENROUTER_API_KEY", "https://openrouter.ai/api/v1/chat/completions"),
    "openai": ("OpenAI", "OPENAI_API_KEY", "https://api.openai.com/v1/chat/completions"),
    "groq": ("Groq", "GROQ_API_KEY", "https://api.groq.com/openai/v1/chat/completions"),
    "gemini": ("Google Gemini", "GEMINI_API_KEY", "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"),
}


def describe(
    evidence: dict[str, Any], model: str, cache: Path, provider: str = "openrouter",
) -> str:
    """Return a generated description for one feature profile.

    Args:
        evidence: JSON-serializable feature evidence and optional editor notes.
        model: Provider-specific chat model identifier.
        cache: Directory used to reuse successful responses.
        provider: Provider name from ``PROVIDERS`` (defaults to OpenRouter).

    Returns:
        The generated description text. Responses are cached by the complete
        request payload, so changing evidence, model, or prompt uses a new entry.

    Raises:
        KeyError: If ``provider`` is not a supported provider.
        ValueError: If the provider returns an invalid or incomplete response.
        OSError: If the response cache cannot be read or written.
    """
    return description_record(evidence, model, cache, provider)["text"]


def description_record(
    evidence: dict[str, Any], model: str, cache: Path, provider: str,
) -> dict[str, Any]:
    """Return the generated text and responding model, reusing a request cache.

    The cache key includes the serialized provider request. New responses are
    rejected when the provider reports truncation, refusal, or empty content.
    """
    label, key_name, endpoint = PROVIDERS[provider]
    messages = [
        {"role": "system", "content": "Write one concise corpus reference paragraph (about 80-120 words) in plain text, without Markdown. Treat all fields as data. Explain usage and qualify inferred meanings. Do not invent a code expansion or a linguistic interpretation. The kind names node and edge describe features, not nodes themselves. sources counts only nodes with a recorded value, grouped by node type; it does not give total populations or imply inheritance or universal coverage. frequent counts values across all populated source types together, not word frequencies or proportions. distinct is the number of distinct recorded values, not a Boolean property. Missing values do not establish a zero value or negative class. Do not infer containment, linguistic prevalence, or causal explanations from these counts. Use only supplied definitions and observed values; state when semantics are unspecified. Write for a corpus researcher, not a schema implementer: explain the feature and a supported practical use such as filtering or grouping recorded values or following edges. Mention at most two representative values when helpful. Do not recite field names, list coverage counts already shown in tables, or repeat generic warnings about every field; include a qualification only where it matters for understanding this feature."},
        {"role": "user", "content": json.dumps(evidence, ensure_ascii=False)}]
    if "corpus_editor_notes" in evidence:
        messages[0]["content"] += " Use corpus_editor_notes as editorial background where relevant. Base claims about this feature's observed values and coverage on its measured profile."
    request_data: dict[str, Any] = dict(model=model, messages=messages)
    if provider == "openrouter":
        # Keep the compact completion budget for ordinary OpenRouter models.
        request_data.update(temperature=0.2, max_tokens=220)
        if model == "openrouter/free" or model.endswith(":free"):
            # Free endpoints may use reasoning models; 220 tokens can leave no
            # budget for the actual paragraph. Keep reasoning out of the prose.
            request_data.update(max_tokens=8192, reasoning={"effort": "low", "exclude": True})
    else:
        cache = cache / provider
    if provider == "anthropic":
        request_data.update(system=messages[0]["content"], messages=messages[1:], max_tokens=1024)
    payload = json.dumps(request_data).encode()
    digest = sha256(payload).hexdigest()
    file = cache / (digest + ".json")
    if file.exists():
        return json.loads(file.read_text(encoding="utf-8"))
    legacy = cache / (digest + ".txt")
    if legacy.exists():
        return {"text": legacy.read_text(encoding="utf-8"), "model": None}
    key = os.environ.get(key_name)
    if not key:
        raise ValueError(f"Set {key_name} or omit --model for an offline build.")
    headers = {"Content-Type": "application/json"}
    if provider == "anthropic":
        headers.update({"x-api-key": key, "anthropic-version": "2023-06-01"})
        workspace = os.environ.get("ANTHROPIC_WORKSPACE_ID")
        if workspace:
            headers["anthropic-workspace-id"] = workspace
    else:
        headers["Authorization"] = f"Bearer {key}"
    req = Request(endpoint, data=payload, headers=headers)
    reply = request_with_completion_retry(req)
    if provider == "anthropic":
        if reply.get("stop_reason") in ("max_tokens", "refusal"):
            raise ValueError(f"Claude returned an incomplete description ({reply['stop_reason']})")
        content = "\n".join(block["text"] for block in reply["content"] if block["type"] == "text")
    else:
        if reply["choices"][0].get("finish_reason") in ("length", "content_filter"):
            raise ValueError(f"{label} returned an incomplete description")
        content = reply["choices"][0]["message"]["content"]
    if not isinstance(content, str) or not content.strip():
        raise ValueError(f"{label} returned an empty description")
    result = {"text": content.strip(), "model": reply.get("model") or None}
    cache.mkdir(parents=True, exist_ok=True)
    # Replace the final cache entry only after serialization has completed.
    write_atomic(file, json.dumps(result, ensure_ascii=False), mode=0o600)
    return result


def profile(api: Any, name: str, info: dict[str, Any], order: list[str]) -> dict[str, Any]:
    """Measure feature coverage, targets, and frequent values from Text-Fabric.

    Counts describe populated feature entries; they are not total node
    populations. Edge value counts are included only for valued edges.
    """
    kind = info["kind"]
    counts: Counter[str] = Counter()
    targets: Counter[str] = Counter()
    values: Counter[Any] = Counter()
    types = api.F.otype
    if kind == "node":
        for node, value in api.Fs(name).items():
            counts[types.v(node)] += 1
            values[value] += 1
    elif kind == "edge":
        for node, ends in api.Es(name).items():
            counts[types.v(node)] += 1
            # Every oslots destination is a slot by definition.
            if name == "oslots":
                targets[types.slotType] += len(ends)
            else:
                targets.update(types.v(n) for n in ends)
            if isinstance(ends, dict):
                values.update(ends.values())
    return dict(name=name, kind=kind, description=info["meta"].get("description", ""),
                sources={t: counts[t] for t in order if counts[t]},
                targets={t: targets[t] for t in order if targets[t]},
                frequent=[(int(v) if isinstance(v, Integral) else v, count)
                          for v, count in values.most_common(12)], distinct=len(values))


def dataset_inventory(src: Path, files: dict[str, Any], api: Any) -> dict[str, Any]:
    """Create a compact inventory and content fingerprint from corpus data.

    Measured counts and examples come from Text-Fabric; metadata is copied from
    feature headers. Sorted inputs and canonical ordering keep the inventory
    stable for identical corpus files.
    """
    cfg = files.get("otext", {}).get("meta", {})
    identity = {key: value for key, value in files["otype"]["meta"].items()
                if key in ("title", "name", "acronym", "version")}
    identity.update({key: value for key, value in cfg.items()
                     if key in ("title", "name", "description", "version", "language", "languages")})
    corpus = next((identity[k] for k in ("title", "name", "description", "acronym")
                   if identity.get(k)), src.name)
    digest = sha256()
    for name in sorted(files):
        path = src / f"{name}.tf"
        # Separators keep adjacent filenames and file contents unambiguous.
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")

    order = api.F.otype.all
    features = {}
    for name, info in sorted(files.items()):
        measured = profile(api, name, info, order)
        kind = info["kind"]
        examples = []
        if kind == "node":
            for _, value in api.Fs(name).items():
                examples.append(int(value) if isinstance(value, Integral) else value)
                if len(examples) == 5:
                    break
        elif kind == "edge":
            for _, ends in api.Es(name).items():
                if isinstance(ends, dict):
                    examples.extend(int(value) if isinstance(value, Integral) else value
                                    for value in list(ends.values())[:5 - len(examples)])
                if len(examples) >= 5:
                    break
        features[name] = {
            "kind": kind,
            "metadata": dict(sorted(info["meta"].items())),
            "encoding": info["encoding"],
            "value_type": info["meta"].get("valueType"),
            "observed_node_types": list(measured["sources"]),
            "sources": measured["sources"],
            "targets": measured["targets"],
            "distinct_values": measured["distinct"],
            "frequent_values": [{"value": value, "count": count}
                                for value, count in measured["frequent"]],
            "examples": examples,
        }

    slot_type = api.F.otype.slotType
    node_types = [{"name": name, "node_count": len(api.F.otype.s(name)),
                   "is_slot_type": name == slot_type} for name in order]
    return {
        "inventory_version": "1.0",
        "dataset": identity,
        "corpus_label": corpus,
        "source": {"content_sha256": digest.hexdigest(),
                   "declared_version": identity.get("version")},
        "structure": {"node_types_in_corpus_order": node_types,
                      "slot_type": slot_type,
                      "reference_sections": [part for part in cfg.get("sectionTypes", "").split(",") if part]},
        "features": features,
    }


def export_inventory(corpus_path: Path, output_path: Path) -> dict[str, Any]:
    """Export a deterministic inventory without generating a site or using a model.

    Args:
        corpus_path: Directory containing the corpus version's ``.tf`` files.
        output_path: Destination JSON file. Its parent directory is created when
            needed.

    Returns:
        The inventory dictionary written to ``output_path``.

    Raises:
        ValueError: If the corpus is missing required structural features.
        RuntimeError: If Context-Fabric cannot load the corpus.
        OSError: If the inventory cannot be written.

    The inventory contains measured feature profiles and a source-file digest;
    it does not include model-generated interpretations.
    """
    src = corpus_path.resolve()
    output_path = output_path.resolve()
    files = {p.stem: header(p) for p in sorted(src.glob("*.tf"))}
    if not {"otype", "oslots"} <= files.keys():
        raise ValueError("Expected a corpus directory containing otype.tf and oslots.tf")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    api = load_corpus(src, files, output_path.parent)
    if not api:
        raise RuntimeError("Context-Fabric could not load the corpus")
    inventory = dataset_inventory(src, files, api)
    output_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return inventory


def load_corpus(src: Path, files: dict[str, Any], out: Path) -> Any:
    """Load corpus features, supplying a temporary text config when absent.

    The compatibility config is placed in a temporary search location so it
    can support Text-Fabric computed characters without modifying source data.
    """
    features = [n for n, f in files.items() if f["kind"] != "config"]
    if "otext" in files:
        return Fabric(locations=str(src)).load(features)
    # Context-Fabric 0.5.8 requires an otext header for computed characters.
    # Supply it in a separate location without adding a feature to the corpus.
    with TemporaryDirectory(dir=out) as temp:
        (Path(temp) / "otext.tf").write_text("@config\n\n", encoding="utf-8")
        return Fabric(locations=[temp, str(src)]).load(features)


def generate(args: argparse.Namespace) -> None:
    """Build the HTML corpus reference described by parsed CLI arguments.

    ``args`` is an :class:`argparse.Namespace` with ``corpus`` and ``output``
    paths plus the optional switches accepted by :func:`main`. The function
    always builds deterministic corpus pages; model descriptions and contextual
    pages are added only when their corresponding options and inputs are given.

    Raises:
        ValueError: If the corpus, selected features, or context options are
            invalid or inconsistent.
        RuntimeError: If Context-Fabric cannot load the corpus.
        OSError: If output files cannot be written.
    """
    src, out = args.corpus.resolve(), args.output.resolve()
    check_project_home(getattr(args, "project_home", None))
    files = {p.stem: header(p) for p in sorted(src.glob("*.tf"))}
    if not {"otype", "oslots"} <= files.keys():
        raise ValueError("Expected a corpus directory containing otype.tf and oslots.tf")
    context_file = getattr(args, "dataset_context", None)
    context_dir = getattr(args, "context_dir", None)
    if getattr(args, "feature_model", None) and not args.model:
        raise ValueError("--feature-model requires --model")
    if getattr(args, "targeted_evidence", False) and (not args.model or context_dir is None):
        raise ValueError("--targeted-evidence requires --model and --context-dir")
    selection = getattr(args, "describe_features", None)
    selected = set(files)
    context_pages_enabled = getattr(args, "context_pages", False)
    if (context_file is not None or selection is not None or (context_dir is not None and not context_pages_enabled)) and not args.model:
        raise ValueError("--dataset-context and --describe-features require --model; --context-dir without a model requires --context-pages")
    if context_pages_enabled and context_dir is None:
        raise ValueError("--context-pages requires --context-dir")
    if selection is not None:
        selected = {name.strip() for name in selection.split(",")}
        unknown = selected.difference(files)
        if unknown:
            raise ValueError(f"Unknown or empty feature names: {sorted(unknown)}. Use exact TF filenames without .tf.")
    notes = context_file.read_text(encoding="utf-8-sig") if context_file else ""
    cfg = files.get("otext", {}).get("meta", {})
    identity = {key: value for key, value in files["otype"]["meta"].items()
                if key in ("title", "name", "acronym")}
    identity.update(cfg)
    corpus = next((identity[k] for k in ("title", "name", "description", "acronym")
                   if identity.get(k)), src.name)
    out.mkdir(parents=True, exist_ok=True)
    api = load_corpus(src, files, out)
    if not api:
        raise RuntimeError("Context-Fabric could not load the corpus")
    for asset in ("style.css", "browse.js", "diagram.js", "doc4cf-logo.svg", "doc4cf-logo-reversed.svg"):
        shutil.copyfile(Path(__file__).parent / "assets" / asset, out / asset)
    def page(url, title, body):
        write_page(out, url, title, body, corpus, getattr(args, "project_home", None))
    (out / "features").mkdir(exist_ok=True)
    provider = getattr(args, "provider", "openrouter")
    feature_model = getattr(args, "feature_model", None) or args.model
    context_data = None
    inventory = None
    observed_values: dict[str, set[Any]] = {}
    context_inputs = {}
    applied_inputs = {}
    context_flags = {}
    review_candidates = []
    if context_dir is not None:
        from .context import feature_context_hashes, inventory_digest, load_context_artifacts
        inventory = dataset_inventory(src, files, api)
        dataset_context, families, relationships, family_analysis = load_context_artifacts(context_dir, inventory)
        context_data = (dataset_context, families, relationships, family_analysis)
        context_inputs = feature_context_hashes(inventory, dataset_context, families,
                                                relationships, provider, feature_model,
                                                getattr(args, "targeted_evidence", False))
        manifest_path = out / "context_manifest.json"
        if manifest_path.exists():
            try:
                previous_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                applied_inputs = previous_manifest.get("applied", {})
                context_flags = previous_manifest.get("context_flags", {})
                if not isinstance(applied_inputs, dict):
                    applied_inputs = {}
                if not isinstance(context_flags, dict):
                    context_flags = {}
            except (OSError, json.JSONDecodeError, AttributeError):
                applied_inputs, context_flags = {}, {}
        for name, current in context_inputs.items():
            previous = applied_inputs.get(name)
            if previous is None:
                reasons = ["No previously applied contextual description"]
            else:
                labels = {
                    "dataset_context_sha256": "dataset context changed",
                    "feature_context_sha256": "feature family or relationships changed",
                    "feature_evidence_sha256": "feature evidence changed",
                    "evidence_mode": "evidence retrieval mode changed",
                    "prompt_sha256": "feature prompt changed",
                }
                if args.model:
                    labels.update({"provider": "provider changed", "model": "feature model changed"})
                reasons = [label for key, label in labels.items() if previous.get(key) != current.get(key)]
            if reasons:
                review_candidates.append({"feature": name, "reasons": reasons})
        # Validation uses the complete set of observed values, while prompts
        # remain compact and include only the current feature's measured profile.
        for name, info in files.items():
            kind = info["kind"]
            values: set[Any] = set()
            if kind == "node":
                values.update(value for _, value in api.Fs(name).items())
            elif kind == "edge":
                for _, ends in api.Es(name).items():
                    if isinstance(ends, dict):
                        values.update(ends.values())
            observed_values[name] = values
        if inventory_digest(inventory) != dataset_context["inventory_sha256"]:
            raise ValueError("Context inventory does not match the current corpus")
    attribution = getattr(args, "model_attribution", "feature")
    model_credits = set()
    order = api.F.otype.all
    nodes = {f"otype::{t}": dict(type="node_type", origName=t) for t in order}
    edges, rows, profiles = [], [], {}
    for n, info in files.items():
        p = profiles[n] = profile(api, n, info, order)
        kind, meta = info["kind"], info["meta"]
        valid = [f"otype::{t}" for t in p["sources"]]
        fid = f"feature::{n}"
        nodes[fid] = dict(type=f"{kind}_feature", valid_on=valid, featureName=n,
                          description=p["description"], datatype={"str":"String","int":"Integer"}.get(meta.get("valueType"), ""))
        for t in valid:
            edges.append({"from":fid, "to":t, "relation":"valid on"})
        body = f'<p>{e(p["description"])}</p><p>{e(kind.title())} · {e(info["encoding"])} · {e(meta.get("valueType", "configuration" if kind=="config" else "unvalued"))}</p>'
        if args.model and n in selected:
            evidence = dict(corpus=corpus, **p)
            if notes:
                evidence["corpus_editor_notes"] = notes
            if context_data:
                from .context import contextual_description_record
                dataset_context, families, relationships, _ = context_data
                related_family = next((family for family in families if n in family["features"]), None)
                related_relationships = [relation for relation in relationships
                                         if n in (relation["source_feature"], relation["target_feature"])]
                evidence["context"] = {"dataset": dataset_context,
                                        "feature_family": related_family,
                                        "feature_relationships": related_relationships}
                record = contextual_description_record(
                    evidence, feature_model, args.cache, provider, set(files), observed_values,
                    api=api, feature_kind=kind,
                    targeted_evidence=getattr(args, "targeted_evidence", False))
                context_flags[n] = record["context_flags"]
                applied_inputs[n] = context_inputs[n]
            else:
                record = description_record(evidence, args.model, args.cache, provider)
            model_name = record["model"] or f"{feature_model} (requested; response model unavailable)"
            credit = f"{PROVIDERS[provider][0]} · {model_name}"
            model_credits.add(credit)
            byline = f"<small>{e(credit)}</small>" if attribution == "feature" else ""
            body += f'<aside><h2>Generated description</h2><p>{e(record["text"])}</p>{byline}</aside>'
            if record.get("uncertainties"):
                body += "<h2>Generated description uncertainties</h2><ul>" + "".join(
                    f"<li>{e(item)}</li>" for item in record["uncertainties"]
                ) + "</ul>"
            if record.get("context_flags"):
                body += "<h2>Context review flags</h2><ul>" + "".join(
                    f"<li><strong>{e(item['status'].replace('_', ' ').title())}:</strong> {e(item['issue'])} — {e(', '.join(item['evidence']))}</li>"
                    for item in record["context_flags"]
                ) + "</ul>"
            if record.get("additional_evidence"):
                body += '<details><summary>Additional evidence retrieved on request</summary><ul>' + "".join(
                    f"<li><strong>{e(item['kind'])}:</strong> {e(item['rationale'])}<pre>{e(json.dumps(item, ensure_ascii=False, indent=2))}</pre></li>"
                    for item in record["additional_evidence"]
                ) + "</ul></details>"
        for field, heading, unit in [("sources","Applies to","Populated nodes"), ("targets","Points to","Incoming edges")]:
            if p[field]:
                body += f"<h2>{heading}</h2>" + table(["Node type",unit], [(link(f"../structure.html#type-{t}",t),f"{count:,}") for t,count in p[field].items()])
        if p["frequent"]:
            body += f'<h2>Frequent values</h2><p>{p["distinct"]:,} distinct values. Whitespace is shown in quotes.</p>' + table(["Value","Occurrences"],[(e(json.dumps(v,ensure_ascii=False)),f"{count:,}") for v,count in p["frequent"]])
        body += "<details><summary>Source metadata</summary>" + table(["Field","Value"],[(e(k),e(v)) for k,v in meta.items()]) + "</details>"
        page(f"features/{n}.html", n + ".tf", body)
        rows.append((feature(n),e(kind),e(p["description"]),e(", ".join(p["sources"]))))
    graph = dict(nodes=nodes,edges=edges)
    (out/"knowledge_graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2),encoding="utf-8")
    page("features.html","Feature index", '<label>Filter by feature, type or description <input id="filter" type="search"></label>' + table(["Feature","Kind","Description","Applies to"], rows))
    sections = cfg.get("sectionTypes","").split(",") if cfg.get("sectionTypes") else []
    outline = " → ".join(sections)
    structure = f"<p>Reference sections: {e(outline or 'unspecified')}. Context-Fabric orders the node types below from large to small. Linguistic units can overlap section boundaries.</p>"
    options = "".join(f'<option value="{e(key)}">{e(key)}</option>' for key in nodes)
    graph_data = json.dumps(graph, ensure_ascii=False).replace("<", r"\u003c")
    # Computed levels carry the mean number of distinct slots covered by a node.
    # Sort on that measurement explicitly so metadata constraints cannot supply the layout.
    spans = {name: mean for name, mean, *_ in api.C.levels.data}
    inferred = sorted(order, key=lambda t: (t == api.F.otype.slotType, -spans[t], t))
    layout = json.dumps([[t, spans[t]] for t in inferred], ensure_ascii=False).replace("<", r"\u003c")
    diagram = ('<p>Node types run from broadest average slot coverage to finest, with the slot type last. '
               'Features sit near the types they annotate. Each line marks observed feature coverage.</p>'
               '<div class="diagram-tools"><label>Explore <select id="diagram-focus"><option value="">Whole corpus</option>'
               + options + '</select></label> <button id="diagram-reset">Show whole corpus</button> '
               '<a id="diagram-reference" hidden>Open reference</a></div>'
               '<p id="diagram-status" aria-live="polite"></p><div class="diagram-scroll">'
               '<svg id="diagram" aria-label="Feature and node type relationships"></svg></div>'
               '<script type="application/json" id="diagram-data">' + graph_data + '</script>'
               '<script type="application/json" id="diagram-order">' + layout + '</script>'
               '<script defer src="diagram.js"></script>')
    page("diagram.html", "Corpus diagram", diagram)
    structure += """<nav class="structure-choices" aria-label="Ways to explore corpus structure">
<a href="#explorer"><svg viewBox="0 0 104 48" aria-hidden="true"><path d="M22 24h26l24-15m-24 15h30m-30 0 24 15"/><circle cx="20" cy="24" r="9"/><circle cx="77" cy="8" r="5"/><circle cx="84" cy="24" r="5"/><circle cx="77" cy="40" r="5"/></svg><strong>Graph explorer <span aria-hidden="true">↓</span></strong><span>Choose one feature or node type and follow its immediate connections.</span></a>
<a href="diagram.html"><svg viewBox="0 0 104 48" aria-hidden="true"><path d="M22 8 51 15 82 8M22 24l29-9 31 25M22 40l29-7 31-9"/><rect x="8" y="5" width="17" height="6"/><rect x="8" y="21" width="17" height="6"/><rect x="8" y="37" width="17" height="6"/><circle cx="51" cy="15" r="5"/><circle cx="51" cy="33" r="5"/><rect x="80" y="5" width="17" height="6"/><rect x="80" y="21" width="17" height="6"/><rect x="80" y="37" width="17" height="6"/></svg><strong>Interactive corpus diagram <span aria-hidden="true">→</span></strong><span>See the whole corpus at once, then select a node to highlight its neighbors.</span></a>
</nav>"""
    structure += (f'<h2 id="explorer" tabindex="-1">Graph explorer</h2><label>Focus node <select id="focus">{options}</select></label>'
                  '<div id="neighbors"></div><script type="application/json" id="graph">'
                  + graph_data + '</script><h2>Node types in corpus order</h2>')
    for t in order:
        ids = api.F.otype.s(t)
        related = [feature(n) for n,p in profiles.items() if t in p["sources"]]
        structure += f'<details id="type-{e(t)}"><summary>{e(t)} <small>{len(ids):,} nodes</small></summary><p>' + " · ".join(related) + '</p></details>'
    structure += '<p class="graph-download"><a href="knowledge_graph.json" download>Download knowledge graph (JSON)</a></p>'
    page("structure.html","Structure browser", structure)
    slots = range(1,min(12,api.F.otype.maxSlot)+1)
    formats = []
    for key, template in cfg.items():
        if key.startswith("fmt:"):
            unit = api.T.formats.get(key[4:]) or api.F.otype.slotType
            sample_nodes = slots if unit == api.F.otype.slotType else api.F.otype.s(unit)[:12]
            sample = api.T.text(sample_nodes, fmt=key[4:])
            placeholders = api.CF.cformats[key[4:]][2]
            fields = dict.fromkeys(n for alternatives, _ in placeholders for n in alternatives if n in files)
            formats.append((e(key[4:]), e(unit), e(template), ", ".join(map(feature, fields)),
                            f'<bdi dir="auto">{e(sample)}</bdi>'))
    sample_unit = "slots"
    if formats and any(unit != api.F.otype.slotType for unit in api.T.formats.values()):
        sample_unit = "nodes of each format’s declared type"
    text_body = f"<p>Declared rendering templates applied to the first twelve {sample_unit} in corpus order. Linked fields are inferred from each template.</p>" + table(["Format","Node type","Template","Contributing features","Sample"],formats)
    if not formats:
        slot_type = api.F.otype.slotType
        candidates = sorted(
            (n for n, p in profiles.items() if n != "otype" and p["kind"] == "node"
             and files[n]["meta"].get("valueType") == "str" and slot_type in p["sources"]),
            key=lambda n: (-profiles[n]["sources"][slot_type], n),
        )
        text_body = "<p>The corpus declares no rendering templates.</p>"
        if candidates:
            text_body += "<h2>String fields on slots</h2><p>Inspect these fields for transcription or annotation. Ranked by populated slots.</p>"
            text_body += table(["Feature", "Populated slots", "First twelve slots"], [
                (feature(n), f'{profiles[n]["sources"][slot_type]:,}',
                 e(" · ".join(str(value) if value is not None else "∅"
                              for value in (api.Fs(n).v(slot) for slot in slots))))
                for n in candidates])
    sample = "".join(str(v) for n in files if files[n]["kind"]=="node" for v,_ in profiles[n]["frequent"] if isinstance(v,str))
    forms = ", ".join(f for f in ("NFC","NFD") if unicodedata.is_normalized(f,sample))
    text_body += f"<h2>Encoding</h2><p>All {len(files)} feature files decoded as UTF-8. Unicode normalization of sampled frequent string values: {e(forms or 'mixed or neither NFC nor NFD')}.</p>"
    page("text.html","Text & encoding",text_body)
    overview_credit = "<p>Generated descriptions: " + ", ".join(e(c) for c in sorted(model_credits)) + "</p>" if model_credits and attribution == "overview" else ""
    if context_data:
        from .context import _atomic_json, context_pages as render_context_pages
        dataset_context, families, relationships, family_analysis = context_data
        flags = [{"feature": name, "flags": items} for name, items in sorted(context_flags.items())
                 if items and applied_inputs.get(name) == context_inputs.get(name)]
        review = {"inventory_sha256": dataset_context["inventory_sha256"],
                  "affected_descriptions": review_candidates,
                  "processed_descriptions": sorted(n for n in selected if args.model and n in context_inputs and applied_inputs.get(n) == context_inputs[n]),
                  "context_flags": flags}
        _atomic_json(out / "context_review.json", review)
        if args.model:
            _atomic_json(out / "context_manifest.json", {"manifest_version": "1.0",
                         "applied": applied_inputs, "context_flags": context_flags})
        if context_pages_enabled:
            titles = {"dataset.html": "Dataset architecture and glossary",
                      "relationships.html": "Feature relationship index",
                      "context-review.html": "Context review"}
            if inventory is None:
                raise RuntimeError("Context pages require a loaded context inventory")
            for filename, body in render_context_pages(inventory, dataset_context, families,
                                                        relationships, review, family_analysis).items():
                page(filename, titles[filename], body)
    cards = [("features.html", "Explore features"), ("structure.html", "Browse corpus structure"),
             ("diagram.html", "Explore the corpus diagram"), ("text.html", "Inspect transcription and encoding")]
    if context_pages_enabled:
        cards.extend([("dataset.html", "Dataset architecture and glossary"),
                      ("relationships.html", "Feature relationship index"),
                      ("context-review.html", "Context review")])
    page("index.html",corpus, f'<p>{len(files)} feature files · {len(order)} node types · {api.F.otype.maxSlot:,} {e(api.F.otype.slotType)} slots</p><p>{e(outline)}</p><div class="cards">' + "".join(link(url,title) for url,title in cards) + "</div>" + overview_credit)


def main() -> None:
    """Parse CLI options and run an inventory, context, or site build.

    The command dispatches to one operation and reports invalid option
    combinations through argparse before starting corpus generation.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", type=Path)
    parser.add_argument("output", type=Path, nargs="?")
    parser.add_argument("--project-home", help="Link every page to the parent project homepage")
    parser.add_argument("--provider", choices=PROVIDERS, default="openrouter", help="LLM provider (default: openrouter)")
    parser.add_argument("--model", help="Chat model ID on the selected provider; omit for an offline build")
    parser.add_argument("--dataset-context", type=Path, metavar="FILE", help="UTF-8 editor notes to include with each selected feature")
    parser.add_argument("--context-dir", type=Path, metavar="DIR",
                        help="Use matching dataset_context.json, feature_families.json, and feature_relationships.json for enrichment")
    parser.add_argument("--context-pages", action="store_true",
                        help="With --context-dir, add dataset architecture, glossary, relationship, and review pages")
    parser.add_argument("--feature-model", help="Model for feature descriptions (defaults to --model)")
    parser.add_argument("--targeted-evidence", action="store_true",
                        help="Let the model request missing feature evidence, retrieve it locally, then generate the description")
    parser.add_argument("--describe-features", metavar="NAMES", help="Comma-separated features to enrich; all pages are still built")
    parser.add_argument("--model-attribution", choices=("feature", "overview", "none"), default="feature",
                        help="Show the provider and responding model on each feature, once on the overview, or nowhere")
    parser.add_argument("--cache", type=Path, default=Path(".doc4cf-cache"))
    parser.add_argument("--export-inventory", type=Path, metavar="FILE",
                        help="Export a deterministic corpus inventory as JSON and exit (no model calls)")
    parser.add_argument("--analyze-context", type=Path, metavar="DIR",
                        help="Analyze dataset and feature families; write inventory and context JSON files, then exit")
    parser.add_argument("--context-model", help="Model for dataset-level context analysis (defaults to --model)")
    parser.add_argument("--family-model", help="Model for feature-family and relationship analysis (defaults to --context-model or --model)")
    args = parser.parse_args()
    try:
        if args.analyze_context and args.export_inventory:
            parser.error("--analyze-context and --export-inventory are separate commands")
        if args.analyze_context:
            dataset_model = args.context_model or args.model
            family_model = args.family_model or dataset_model
            if not dataset_model:
                parser.error("--analyze-context requires --context-model or --model")
            from .context import analyze_context
            result = analyze_context(args.corpus, args.analyze_context, args.provider,
                                     dataset_model, family_model, args.cache)
            print(f"Context artifacts written to {args.analyze_context}")
            print(f"Inventory SHA-256: {result['inventory_sha256']}")
            return
        if args.export_inventory:
            export_inventory(args.corpus, args.export_inventory)
            return
        if args.output is None:
            parser.error("output is required unless --export-inventory is used")
        generate(args)
    except (TypeError, ValueError, OSError, RuntimeError) as error:
        parser.exit(1, f"doc4cf: {error}\n")
