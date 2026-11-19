"""Build an offline corpus reference from Context-Fabric."""
import argparse
from collections.abc import Callable, Sequence
from collections import Counter
from hashlib import sha256
from html import escape
import json
import logging
import time
import random
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from urllib.error import HTTPError, URLError
from numbers import Integral
from pathlib import Path
from statistics import median
import shutil
from tempfile import NamedTemporaryFile, TemporaryDirectory
from typing import Any, cast
import unicodedata
from urllib.parse import quote, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from cfabric.core import Fabric
from .providers import PROVIDERS, build_provider_request
from .prompts import load_description, load_prompt


logger = logging.getLogger(__name__)


def ai_indicator(provider: str, requested_model: str, responding_model: str | None,
                 explanation: str, identifier: str = "") -> str:
    """Render a compact, keyboard-accessible explanation for inferred content."""
    response = responding_model or f"{requested_model} (reported model unavailable)"
    tooltip_id = "ai-info-" + sha256(f"{identifier}|{provider}|{requested_model}|{explanation}".encode()).hexdigest()[:12]
    return (
        '<span class="ai-indicator"><button type="button" aria-label="About this AI-generated content" '
        f'aria-describedby="{tooltip_id}">✦</button><span class="ai-tooltip" role="tooltip" id="{tooltip_id}">'
        f'<strong>AI-assisted interpretation</strong><br>{e(explanation)}<br>'
        f'<span>Provider: {e(provider)} · Model: {e(response)}</span></span></span>'
    )


def application_source_files(application: dict[str, Any] | None) -> list[tuple[str, str]]:
    """Return harvested app paths and hashes across supported inventory shapes."""
    if not application:
        return []
    source_files = application.get("source_files", [])
    if isinstance(source_files, dict):
        return [(str(path), str(digest)) for path, digest in sorted(source_files.items())]
    if isinstance(source_files, list):
        return sorted(
            (str(item["path"]), str(item["sha256"]))
            for item in source_files
            if isinstance(item, dict) and "path" in item and "sha256" in item
        )
    return []


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
FEATURE_SYSTEM = load_prompt("feature-description.txt")
STRUCTURAL_FEATURES = ("otype", "otext", "oslots")
_FEATURE_KIND_GUIDANCE = {
    "node": load_prompt("feature-node.txt"),
    "edge": load_prompt("feature-edge.txt"),
}
_STRUCTURAL_DESCRIPTIONS = {
    name: load_description(f"{name}.txt") for name in STRUCTURAL_FEATURES
}
_STRUCTURAL_GUIDANCE = {
    name: load_prompt(f"feature-{name}.txt") for name in STRUCTURAL_FEATURES
}


def standard_feature_description(name: str, metadata_description: str = "") -> str:
    """Return the maintained baseline for a structural feature, else metadata."""
    return _STRUCTURAL_DESCRIPTIONS.get(name, metadata_description)


def feature_description_prompt(
    name: str, base_prompt: str = FEATURE_SYSTEM, kind: str | None = None,
) -> str:
    """Select kind guidance or a more specific structural-feature prompt."""
    guidance = _STRUCTURAL_GUIDANCE.get(name) or _FEATURE_KIND_GUIDANCE.get(kind)
    return f"{base_prompt}\n\n{guidance}" if guidance else base_prompt


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


def audit_section(title: str, explanation: str, details: str,
                  disclosure: str = "Show details") -> str:
    """Render an audit section with a fixed summary and collapsed technical detail."""
    return (
        '<section class="audit-section">'
        f"<h2>{e(title)}</h2><p class=\"audit-summary\">{e(explanation)}</p>"
        f"<details><summary>{e(disclosure)}</summary>{details}</details>"
        "</section>"
    )


def is_http_url(value: str) -> bool:
    """Return True for well-formed absolute http(s) URLs; never raises."""
    try:
        return urlsplit(value).scheme in ("http", "https")
    except ValueError:
        return False


def link(url: str, label: str) -> str:
    """Render an HTML link, escaping its URL and visible label.

    External links get ``rel="noopener noreferrer"``.
    """
    rel = ' rel="noopener noreferrer"' if is_http_url(url) else ""
    return f'<a href="{e(url)}"{rel}>{e(label)}</a>'


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


# The site is static: its own CSS, JS and images only, no inline code or forms.
CONTENT_SECURITY_POLICY = ("default-src 'none'; img-src 'self'; style-src 'self'; "
                           "script-src 'self'; base-uri 'none'; form-action 'none'")


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
        ("structure.html", "Structure"), ("text.html", "Text & encoding"),
        ("audit.html", "Audit report")])
    (out / filename).write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CONTENT_SECURITY_POLICY}"><title>{e(title)} · {e(corpus)}</title>
<link rel="stylesheet" href="{prefix}style.css"><script defer src="{prefix}browse.js"></script></head>
<body><header>{brand}<nav aria-label="Corpus navigation">{nav}</nav></header>
<main><small>{e(corpus)}</small><h1>{e(title)}</h1>{body}</main>{footer}</body></html>""", encoding="utf-8")


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
    label = PROVIDERS[provider][0]
    messages = [
        {"role": "system", "content": feature_description_prompt(
            evidence.get("name", ""), kind=evidence.get("kind"))},
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
    req = build_provider_request(provider, payload, "--model")
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


def profile(
    api: Any, name: str, info: dict[str, Any], order: list[str],
    node_counts: dict[str, int] | None = None,
    node_assignments: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Measure feature coverage, targets, and frequent values from Text-Fabric.

    Counts describe populated feature entries; they are not total node
    populations. Edge value counts are included only for valued edges.
    """
    kind = info["kind"]
    counts: Counter[str] = Counter()
    targets: Counter[str] = Counter()
    endpoint_pairs: Counter[tuple[str, str]] = Counter()
    degrees: dict[str, list[int]] = {}
    values: Counter[Any] = Counter()
    types = api.F.otype
    if kind == "node":
        from array import array

        assigned_nodes: dict[str, array] = {}
        for node, value in api.Fs(name).items():
            node_type = types.v(node)
            counts[node_type] += 1
            values[value] += 1
            if node_assignments is not None and name != "otype":
                assigned_nodes.setdefault(node_type, array("Q")).append(node)
        if node_assignments is not None and name != "otype":
            node_assignments[name] = assigned_nodes
    elif kind == "edge":
        for node, ends in api.Es(name).items():
            source_type = types.v(node)
            counts[source_type] += 1
            degrees.setdefault(source_type, []).append(len(ends))
            # Every oslots destination is a slot by definition.
            if name == "oslots":
                targets[types.slotType] += len(ends)
                endpoint_pairs[(source_type, types.slotType)] += len(ends)
            else:
                targets.update(types.v(n) for n in ends)
                endpoint_pairs.update((source_type, types.v(target)) for target in ends)
            if isinstance(ends, dict):
                values.update(ends.values())
    result: dict[str, Any] = dict(
        name=name, kind=kind,
        description=standard_feature_description(name, info["meta"].get("description", "")),
        sources={t: counts[t] for t in order if counts[t]},
        coverage={t: counts[t] / node_counts[t] for t in order
                  if counts[t] and node_counts and node_counts.get(t)},
        targets={t: targets[t] for t in order if targets[t]},
        endpoint_pairs=[{"source_type": source, "target_type": target, "edge_count": count}
                        for (source, target), count in sorted(endpoint_pairs.items())],
        degree_summary={t: {"source_nodes": len(values), "min": min(values),
                            "median": median(values), "max": max(values)}
                        for t, values in degrees.items() if values},
        frequent=[(int(v) if isinstance(v, Integral) else v, count)
                  for v, count in values.most_common(12)], distinct=len(values),
        value_count=sum(values.values()),
    )
    if kind == "config":
        result["configuration"] = info["meta"]
    return result


def _feature_associations(
    node_assignments: dict[str, dict[str, Any]], node_counts: dict[str, int], order: list[str],
) -> dict[str, list[dict[str, Any]]]:
    """Rank binary presence/absence associations between node features.

    For each node type, sparse feature assignments give the two presence
    margins and their intersection. The remaining two contingency cells are
    calculated from the full node population, so missing assignments count as
    absence rather than disappearing from the comparison.
    """
    from array import array
    from hashlib import sha256
    from heapq import merge
    from itertools import combinations

    def events(feature_name: str, node_ids: array):
        for node in node_ids:
            yield node, feature_name

    by_type: dict[str, dict[str, Any]] = {node_type: {} for node_type in order}
    for name, per_type in node_assignments.items():
        for node_type, ids in per_type.items():
            if any(ids[index] > ids[index + 1] for index in range(len(ids) - 1)):
                ids = array("Q", sorted(ids))
            by_type[node_type][name] = ids

    associations: dict[str, list[dict[str, Any]]] = {name: [] for name in node_assignments}
    for node_type, feature_ids in by_type.items():
        population = node_counts.get(node_type, 0)
        if population == 0:
            continue
        streams = [events(name, feature_ids[name]) for name in sorted(feature_ids)]
        intersections: Counter[tuple[str, str]] = Counter()
        previous_node = None
        node_features = []
        for node, name in merge(*streams):
            if previous_node is not None and node != previous_node:
                intersections.update(combinations(node_features, 2))
                node_features = []
            node_features.append(name)
            previous_node = node
        if node_features:
            intersections.update(combinations(node_features, 2))

        # Features with an identical node-presence mask share one matrix row;
        # this prevents duplicate coverage fields from crowding the display.
        pattern_groups: dict[bytes, list[str]] = {}
        pattern_arrays: dict[bytes, Any] = {}
        pattern_for: dict[str, bytes] = {}
        for name, ids in feature_ids.items():
            digest = sha256(ids.tobytes()).digest()
            bucket = digest
            suffix = 0
            while bucket in pattern_arrays and pattern_arrays[bucket] != ids:
                suffix += 1
                bucket = digest + suffix.to_bytes(4, "big")
            pattern_arrays[bucket] = ids
            pattern_groups.setdefault(bucket, []).append(name)
            pattern_for[name] = bucket

        candidate_rows: dict[str, list[dict[str, Any]]] = {name: [] for name in feature_ids}
        for left, right in combinations(sorted(feature_ids), 2):
            both_present = intersections.get((left, right), 0)
            left_present = len(feature_ids[left])
            right_present = len(feature_ids[right])
            left_only = left_present - both_present
            right_only = right_present - both_present
            neither = population - both_present - left_only - right_only
            denominator = ((both_present + left_only) * (right_only + neither)
                           * (both_present + right_only) * (left_only + neither)) ** 0.5
            if denominator == 0:
                continue
            phi = (both_present * neither - left_only * right_only) / denominator

            def record(target_present, target_absent, other_present, other_absent,
                       target_only, other_only, correlation,
                       node_type_name=node_type, both_present_count=both_present,
                       neither_count=neither):
                if min(target_present, target_absent, other_present, other_absent) < 10:
                    return None
                if abs(correlation) < 0.10:
                    return None
                return {
                    "node_type": node_type_name,
                    "phi": correlation,
                    "both_present": both_present_count,
                    "other_only": other_only,
                    "target_only": target_only,
                    "both_absent": neither_count,
                    "target_when_other_present": both_present_count / other_present,
                    "target_when_other_absent": target_only / other_absent,
                    "other_present": other_present,
                    "other_absent": other_absent,
                }

            for target, other, target_present, other_present, target_only, other_only in (
                (left, right, left_present, right_present, left_only, right_only),
                (right, left, right_present, left_present, right_only, left_only),
            ):
                item = record(target_present, population - target_present,
                              other_present, population - other_present,
                              target_only, other_only, phi)
                if item is not None:
                    item["pattern"] = pattern_for[other]
                    candidate_rows[target].append(item)

        for target, rows in candidate_rows.items():
            grouped_rows: dict[bytes, dict[str, Any]] = {}
            for item in rows:
                group = grouped_rows.setdefault(item["pattern"], {**item, "features": []})
                group["features"].extend(pattern_groups[item["pattern"]])
            unique_rows = []
            for item in grouped_rows.values():
                item["features"] = sorted(set(item["features"]) - {target})
                item.pop("pattern")
                if item["features"]:
                    unique_rows.append(item)
            positive = sorted((item for item in unique_rows if item["phi"] >= 0.10),
                              key=lambda item: (-item["phi"], -item["both_present"], item["features"]))[:3]
            inverse = sorted((item for item in unique_rows if item["phi"] <= -0.10),
                             key=lambda item: (item["phi"], -item["target_only"], item["features"]))[:2]
            if positive or inverse:
                associations[target].append({"node_type": node_type,
                                             "positive": positive, "inverse": inverse})

    return associations


def dataset_inventory(
    src: Path, files: dict[str, Any], api: Any, app_dir: Path | None = None,
) -> dict[str, Any]:
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
    node_counts = {node_type: len(api.F.otype.s(node_type)) for node_type in order}
    features = {}
    for name, info in sorted(files.items()):
        measured = profile(api, name, info, order, node_counts)
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
    inventory = {
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
    from .app_context import extract_app_context
    application = extract_app_context(
        src, app_dir, sorted(features), {name: info["meta"] for name, info in files.items()})
    if application is not None:
        inventory["application"] = application
    return inventory


def export_inventory(
    corpus_path: Path, output_path: Path, app_dir: Path | None = None,
) -> dict[str, Any]:
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
    inventory = dataset_inventory(src, files, api, app_dir)
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


def _validate_options(args: argparse.Namespace, files: dict[str, Any]) -> set[str]:
    """Check option combinations and return the set of features to describe."""
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
    return selected


def _load_manifest(manifest_path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Read previously applied description inputs; unreadable manifests count as empty."""
    applied_inputs: dict[str, Any] = {}
    context_flags: dict[str, Any] = {}
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
    return applied_inputs, context_flags


def _review_candidates(context_inputs: dict[str, Any], applied_inputs: dict[str, Any],
                      has_model: bool) -> list[dict[str, Any]]:
    """List features whose saved description inputs differ from the current ones."""
    review_candidates: list[dict[str, Any]] = []
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
            if has_model:
                labels.update({"provider": "provider changed", "model": "feature model changed"})
            reasons = [label for key, label in labels.items() if previous.get(key) != current.get(key)]
        if reasons:
            review_candidates.append({"feature": name, "reasons": reasons})
    return review_candidates


def _observed_values(api: Any, files: dict[str, Any]) -> dict[str, set[Any]]:
    """Collect every observed value per feature for validating model references."""
    observed_values: dict[str, set[Any]] = {}
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
    return observed_values


def _render_structure_pages(api: Any, page: Callable[[str, str, str], None], cfg: dict[str, Any],
                             nodes: dict[str, Any], graph: dict[str, Any], order: list[str],
                             profiles: dict[str, Any]) -> str:
    """Write the diagram and structure pages; return the section outline text."""
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
    return outline


def _render_text_page(api: Any, page: Callable[[str, str, str], None], cfg: dict[str, Any],
                      files: dict[str, Any], profiles: dict[str, Any]) -> None:
    """Write the text-format and encoding page."""
    slots = range(1,min(12,api.F.otype.maxSlot)+1)
    formats = []
    for key, template in cfg.items():
        if key.startswith("fmt:"):
            unit = api.T.formats.get(key[4:]) or api.F.otype.slotType
            sample_nodes = slots if unit == api.F.otype.slotType else api.F.otype.s(unit)[:12]
            sample = api.T.text(sample_nodes, fmt=key[4:])
            placeholders = api.CF.cformats[key[4:]][2]
            fields = dict.fromkeys(n for alternatives, _ in placeholders for n in alternatives if n in files)
            anchor = "format-" + sha256(key[4:].encode("utf-8")).hexdigest()[:12]
            formats.append((f'<span id="{anchor}">{e(key[4:])}</span>', e(unit), e(template), ", ".join(map(feature, fields)),
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


def _feature_application_section(
    application: dict[str, Any] | None, name: str, feature_names: set[str],
) -> str:
    """Render configured app uses and linked local documentation for one feature."""
    if not application:
        return ""
    app_links = application.get("feature_application_links", {}).get(name, {})
    config_refs = app_links.get("configuration_references", [])
    text_formats = app_links.get("text_formats", [])
    documentation_links = app_links.get("documentation_links", [])
    linked_docs = application.get("linked_documentation", {}).get("features", {}).get(name, [])
    if not (config_refs or text_formats or documentation_links or linked_docs):
        return ""

    rows = []
    for item in config_refs[:12]:
        value = item.get("value")
        rendered = value if isinstance(value, str) else json.dumps(
            value, ensure_ascii=False, sort_keys=True,
        )
        rows.append((f'<code>{e(item.get("path", "configuration"))}</code>', e(rendered)))
    if len(config_refs) > 12:
        rows.append(("More settings", e(f"{len(config_refs) - 12} additional matching settings omitted")))
    if text_formats:
        for item in text_formats:
            metadata_path = str(item.get("metadata_path", ""))
            format_name = metadata_path.split("metadata.", 1)[-1].removeprefix("fmt:")
            anchor = "format-" + sha256(format_name.encode("utf-8")).hexdigest()[:12]
            label = link(f"../text.html#{anchor}", f"{format_name} rendering format")
            contributing = []
            for placeholder in item.get("placeholders", []):
                contributing.append(link(f"{quote(placeholder)}.html", placeholder)
                                    if placeholder in feature_names else f"<code>{e(placeholder)}</code>")
            rows.append((label, f'<code>{e(item.get("template", ""))}</code>'
                         + (" <span>Uses: " + ", ".join(contributing) + "</span>" if contributing else "")))
    for item in documentation_links[:3]:
        rows.append(("Feature documentation", link(item["url"], "Open source documentation")
                     + " <small>Source: <code>" + e(item.get("source_path", "local app docs"))
                     + "</code>; configured at <code>" + e(item.get("configuration_path", "app config"))
                     + "</code></small>"))

    section = (
        '<section class="feature-app-details"><h2>How the app uses this feature</h2>'
        '<p>These settings describe configured app presentation and documented guidance; '
        'they are separate from the measured corpus data above.</p>'
    )
    if rows:
        section += table(["App setting or format", "Configured value"], rows)
    for document in linked_docs[:3]:
        path = str(document.get("path", "linked app documentation"))
        excerpt = str(document.get("text", ""))[:2400]
        section += (f'<details class="feature-app-document"><summary>Related documentation: '
                    f'{e(path)}</summary><pre>{e(excerpt)}</pre></details>')
    if len(linked_docs) > 3:
        section += f'<p>{len(linked_docs) - 3} additional linked documents are listed in the audit report.</p>'
    return section + "</section>"


def _overview_section(overview_notes: str, context_data: Any) -> str:
    """Render the "About this dataset" overview section, or an empty string."""
    overview_description = ""
    if overview_notes or context_data:
        overview_description = "<section><h2>About this dataset</h2>"
        if overview_notes:
            overview_description += "".join(
                f"<p>{e(paragraph)}</p>" for paragraph in overview_notes.strip().split("\n\n") if paragraph.strip()
            )
        if context_data:
            dataset_context = context_data[0]
            dataset_analysis = dataset_context.get("analysis", {})
            badge = ai_indicator(
                dataset_analysis.get("provider", "Unknown"), dataset_analysis.get("requested_model", "Unknown"),
                dataset_analysis.get("responding_model"),
                "Inferred from the corpus inventory and harvested app configuration. See the Audit report for evidence and review details.",
                "dataset-overview",
            )
            overview_description += (
                f"<p>{e(dataset_context['dataset_profile'])} {badge}</p>"
            )
        overview_description += "</section>"
    return overview_description


def _provenance_section(application: dict[str, Any] | None) -> str:
    """Render configured provenance rows from the harvested app configuration."""
    provenance_description = ""
    if application:
        app_config = application.get("configuration", {})
        provenance = app_config.get("provenanceSpec", {}) if isinstance(app_config, dict) else {}
        if isinstance(provenance, dict):
            provenance_rows: list[tuple[str, str]] = []
            for field_name, value in provenance.items():
                if value is None or value == "" or value == [] or value == {}:
                    continue
                label = "".join((" " + char if char.isupper() else char) for char in str(field_name))
                label = label.replace("_", " ").strip().title()
                if isinstance(value, str) and ("<" in value or "{" in value or "}" in value):
                    continue  # App URL templates are useful to inference, but not as overview links.
                if isinstance(value, str) and str(field_name).lower() == "doi":
                    rendered_value = link("https://doi.org/" + quote(value, safe="/"), value)
                elif isinstance(value, str) and is_http_url(value):
                    rendered_value = link(value, value)
                else:
                    rendered_value = e(value if isinstance(value, str) else json.dumps(
                        value, ensure_ascii=False, sort_keys=True,
                    ))
                provenance_rows.append((e(label), rendered_value))
            writing = app_config.get("writing") if isinstance(app_config, dict) else None
            if writing:
                provenance_rows.append(("Writing", e(writing)))
            if provenance_rows:
                provenance_description = (
                    "<section><h2>Source and provenance</h2>"
                    + table(["Field", "Configured value"], provenance_rows)
                    + "</section>"
                )
    return provenance_description


def _fallback_audit_body(feature_audit: dict[str, Any], application: dict[str, Any] | None) -> str:
    """Render the audit page used when no contextual analysis report exists."""
    evidence_audit = "".join(
        f"<details><summary>{feature(n)}: additional evidence</summary><pre>{e(json.dumps({'requests': item['evidence_requests'], 'retrieved': item['additional_evidence']}, ensure_ascii=False, indent=2, sort_keys=True))}</pre></details>"
        for n, item in sorted(feature_audit.items())
        if item["evidence_requests"] or item["additional_evidence"]
    ) or "<p>No additional evidence was requested.</p>"
    return (
        "<p>Technical record of the AI-assisted descriptions in this corpus site.</p>"
        + audit_section("Harvested app files",
                        "File fingerprints identify the application configuration and behavior inputs available to this build.",
                        table(["Path", "SHA-256"], [
            (e(path), e(digest)) for path, digest in application_source_files(application)
        ]), "Show app file fingerprints")
        + audit_section("Feature description provenance",
                        "Provider and model details identify the source of each generated feature description.",
                        table(["Feature", "Provider", "Requested model", "Responding model", "Uncertainties"],
                [(feature(n), e(item["provider"]), e(item["requested_model"]),
                  e(item["responding_model"] or "Unavailable"),
                  e("; ".join(item["uncertainties"]) or "None recorded"))
                 for n, item in sorted(feature_audit.items())]),
                        "Show feature provenance")
        + audit_section("Input fingerprints",
                        "Hashes describe the feature evidence and prompt inputs associated with each generated description.",
                        "<pre>" + e(json.dumps(
            {name: item["input_fingerprints"] for name, item in sorted(feature_audit.items())},
            ensure_ascii=False, indent=2, sort_keys=True,
        )) + "</pre>", "Show input fingerprints")
        + audit_section("Targeted evidence details",
                        "Requests and locally retrieved examples show what additional evidence supported the descriptions.",
                        evidence_audit, "Show evidence details")
    )

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
    overview_notes_file = getattr(args, "overview_notes", None)
    context_dir = getattr(args, "context_dir", None)
    selected = _validate_options(args, files)
    context_pages_enabled = getattr(args, "context_pages", False)
    notes = context_file.read_text(encoding="utf-8-sig") if context_file else ""
    overview_notes = overview_notes_file.read_text(encoding="utf-8-sig") if overview_notes_file else ""
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
    context_inputs: dict[str, Any] = {}
    applied_inputs: dict[str, Any] = {}
    context_flags: dict[str, Any] = {}
    feature_audit: dict[str, Any] = {}
    audit_body = ""
    review_candidates: list[dict[str, Any]] = []
    if context_dir is not None:
        from .context import feature_context_hashes, inventory_digest, load_context_artifacts
        inventory = dataset_inventory(src, files, api, getattr(args, "app_dir", None))
        application = inventory.get("application")
        dataset_context, families, relationships, family_analysis = load_context_artifacts(context_dir, inventory)
        context_data = (dataset_context, families, relationships, family_analysis)
        context_inputs = feature_context_hashes(inventory, dataset_context, families,
                                                relationships, provider, feature_model,
                                                getattr(args, "targeted_evidence", False))
        applied_inputs, context_flags = _load_manifest(out / "context_manifest.json")
        review_candidates = _review_candidates(context_inputs, applied_inputs, bool(args.model))
    else:
        from .app_context import extract_app_context
        application = extract_app_context(
            src, getattr(args, "app_dir", None), sorted(files),
            {name: info["meta"] for name, info in files.items()})
    page_application = application
    if application:
        # The dataset inference inventory is deliberately kept within its
        # prompt budget. Recompute compact per-feature presentation links
        # from the bounded config for HTML rendering.
        from .app_context import _feature_application_links
        page_config = dict(application.get("configuration", {}))
        if application.get("additional_configuration"):
            page_config["additional_configuration"] = application["additional_configuration"]
        configured_app_dir = getattr(args, "app_dir", None)
        repo_root = (Path(configured_app_dir).resolve().parent if configured_app_dir
                     else src.parent.parent)
        feature_links = _feature_application_links(
            page_config, sorted(files), {name: info["meta"] for name, info in files.items()}, repo_root)
        page_application = {**application, "feature_application_links": feature_links}
    # Validation uses the complete set of observed values, while prompts
    # remain compact and include only the current feature's measured profile.
    observed_values = _observed_values(api, files)
    if context_data:
        if inventory is None:
            raise RuntimeError("Context analysis requires a loaded inventory")
        if inventory_digest(inventory) != dataset_context["inventory_sha256"]:
            raise ValueError("Context inventory does not match the current corpus")
    order = api.F.otype.all
    node_counts = {node_type: len(api.F.otype.s(node_type)) for node_type in order}
    nodes = {f"otype::{t}": dict(type="node_type", origName=t) for t in order}
    edges, rows, profiles = [], [], {}
    node_assignments: dict[str, dict[str, Any]] = {}
    for n, info in files.items():
        p = profiles[n] = profile(api, n, info, order, node_counts, node_assignments)
    associations = _feature_associations(node_assignments, node_counts, order)
    for n, info in files.items():
        p = profiles[n]
        kind, meta = info["kind"], info["meta"]
        valid = [f"otype::{t}" for t in p["sources"]]
        fid = f"feature::{n}"
        nodes[fid] = dict(type=f"{kind}_feature", valid_on=valid, featureName=n,
                          description=p["description"], datatype={"str":"String","int":"Integer"}.get(meta.get("valueType"), ""))
        for t in valid:
            edges.append({"from":fid, "to":t, "relation":"valid on"})
        body = f'<p>{e(p["description"])}</p><p>{e(kind.title())} · {e(info["encoding"])} · {e(meta.get("valueType", "configuration" if kind=="config" else "unvalued"))}</p>'
        if args.model and n in selected:
            omitted_evidence = {"coverage", "value_count"}
            if kind != "edge":
                omitted_evidence.update(("endpoint_pairs", "degree_summary"))
            evidence = dict(corpus=corpus, **{
                key: value for key, value in p.items()
                if key not in omitted_evidence
            })
            # Raw headers are direct corpus evidence for every feature. Keep
            # shared app context compact by attaching only matching settings
            # and explicitly linked local docs to each feature request.
            evidence["feature_metadata"] = meta
            if application:
                feature_links = application.get("feature_application_links", {}).get(n)
                linked_docs = application.get("linked_documentation", {}).get("features", {}).get(n)
                if feature_links or linked_docs:
                    evidence["application_evidence"] = {
                        "feature_links": feature_links or {},
                        "linked_documentation": linked_docs or [],
                    }
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
            explanation = (
                "Based on measured feature data, supplied metadata, and dataset context. "
                "Interpretations may need review against the source corpus."
                if context_data else
                "Based on feature metadata and measured values available for this corpus."
            )
            badge = ai_indicator(PROVIDERS[provider][0], feature_model, record["model"], explanation, f"feature-{n}")
            body += (f'<section class="inferred-description"><h2>Description {badge}</h2>'
                     f'<p>{e(record["text"])}</p></section>')
            feature_audit[n] = {
                "provider": PROVIDERS[provider][0], "requested_model": feature_model,
                "responding_model": record["model"], "uncertainties": record.get("uncertainties", []),
                "context_flags": record.get("context_flags", []),
                "evidence_requests": record.get("evidence_requests", []),
                "additional_evidence": record.get("additional_evidence", []),
                "input_fingerprints": context_inputs.get(n, {
                    "feature_evidence_sha256": sha256(json.dumps(evidence, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
                    "prompt_sha256": sha256(feature_description_prompt(n, kind=kind).encode()).hexdigest(),
                    "provider": provider, "model": feature_model,
                }),
            }
        for field, heading, unit in [("sources","Applies to","Populated nodes"), ("targets","Points to","Incoming edges")]:
            if p[field]:
                value_heading = f"{unit} (% of node type)" if field == "sources" else unit
                values = [(link(f"../structure.html#type-{t}", t),
                           f"{count:,} ({p['coverage'].get(t, 0):.1%})" if field == "sources"
                           else f"{count:,}") for t, count in p[field].items()]
                body += f"<h2>{heading}</h2>" + table(["Node type", value_heading], values)
        if kind == "edge" and p["endpoint_pairs"]:
            body += "<h2>Observed edge connections</h2><p>Counts show recorded edges for each source and target node-type pair.</p>"
            body += table(["Source node type", "Target node type", "Edges"], [
                (link(f"../structure.html#type-{item['source_type']}", item["source_type"]),
                 link(f"../structure.html#type-{item['target_type']}", item["target_type"]),
                 f"{item['edge_count']:,}") for item in p["endpoint_pairs"]
            ])
            if p["degree_summary"]:
                body += "<h2>Targets per connected source node</h2><p>Summary for source nodes with at least one recorded edge.</p>"
                body += table(["Source node type", "Source nodes", "Minimum", "Median", "Maximum"], [
                    (link(f"../structure.html#type-{node_type}", node_type),
                     f"{summary['source_nodes']:,}", f"{summary['min']:,}",
                     f"{summary['median']:g}", f"{summary['max']:,}")
                    for node_type, summary in p["degree_summary"].items()
                ])
        if p["frequent"]:
            body += f'<h2>Frequent values</h2><p>{p["distinct"]:,} distinct values. Whitespace is shown in quotes.</p>' + table(
                ["Value", "Occurrences", "% of populated values"],
                [(e(json.dumps(v, ensure_ascii=False)), f"{count:,}",
                  f"{count / p['value_count']:.1%}" if p["value_count"] else "—")
                 for v, count in p["frequent"]])
        related = associations.get(n, [])
        if related:
            correlated: dict[str, dict[str, Any]] = {}
            for group in related:
                for item in group["positive"]:
                    if item["phi"] < 0.50:
                        continue
                    for other in item["features"]:
                        previous = correlated.get(other)
                        if previous is None or item["phi"] > previous["phi"]:
                            correlated[other] = {"phi": item["phi"], "node_type": group["node_type"]}
            summary = sorted(correlated.items(), key=lambda entry: (-entry[1]["phi"], entry[0]))[:3]
            if summary:
                body += (
                    '<section class="correlated-features"><h2>Correlated features</h2><ul>'
                    + "".join(
                        f'<li>{link(other + ".html", other)} '
                        f'<small>{e(item["node_type"])} · φ {item["phi"]:+.2f}</small></li>'
                        for other, item in summary
                    )
                    + "</ul></section>"
                )
            else:
                body += (
                    '<section class="correlated-features"><h2>Correlated features</h2>'
                    '<p>No features meet the strong positive association threshold (φ ≥ +0.50).</p>'
                    '</section>'
                )
            sections = []
            for group in related:
                rows_for_type = []
                for _relation, items in (("Positive", group["positive"]), ("Inverse", group["inverse"])):
                    for item in items:
                        names = ", ".join(link(other + ".html", other) for other in item["features"])
                        present = (f'{item["both_present"]:,} / {item["other_present"]:,} '
                                   f'({item["target_when_other_present"]:.1%})')
                        absent = (f'{item["target_only"]:,} / {item["other_absent"]:,} '
                                  f'({item["target_when_other_absent"]:.1%})')
                        rows_for_type.append((names, f'{item["phi"]:+.2f}', present, absent))
                if rows_for_type:
                    sections.append(
                        f'<h3>{e(group["node_type"])} nodes</h3>'
                        + table(["Compared feature(s)", "φ", f"{e(n)} present when compared feature is present",
                                 f"{e(n)} present when compared feature is absent"], rows_for_type)
                    )
            if sections:
                body += (
                    '<details class="feature-associations"><summary>Presence/absence associations</summary>'
                    '<p>Each comparison is calculated separately across all nodes of the listed type. '
                    'Present means the feature has an assigned value; absent means no assignment. '
                    'φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). '
                    'Only non-constant pairs with at least 10 present and 10 absent nodes per feature, '
                    'and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. '
                    'These are descriptive associations, not causal claims. '
                    '<a href="../../../api/architecture.html#measured-feature-associations">Read the scoring method</a>.</p>'
                    + "".join(sections) + "</details>"
                )
        body += _feature_application_section(page_application, n, set(files))
        body += "<details><summary>Source metadata</summary>" + table(["Field","Value"],[(e(k),e(v)) for k,v in meta.items()]) + "</details>"
        page(f"features/{n}.html", n + ".tf", body)
        rows.append((feature(n),e(kind),e(p["description"]),e(", ".join(p["sources"]))))
    graph = dict(nodes=nodes,edges=edges)
    (out/"knowledge_graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2),encoding="utf-8")
    page("features.html","Feature index", '<label>Filter by feature, type or description <input id="filter" type="search"></label>' + table(["Feature","Kind","Description","Applies to"], rows))
    outline = _render_structure_pages(api, page, cfg, nodes, graph, order, profiles)
    _render_text_page(api, page, cfg, files, profiles)
    overview_description = _overview_section(overview_notes, context_data)
    provenance_description = _provenance_section(application)
    if context_data:
        from .context import _atomic_json, context_pages as render_context_pages
        dataset_context, families, relationships, family_analysis = context_data
        flags = [{"feature": name, "flags": items} for name, items in sorted(context_flags.items())
                 if items and applied_inputs.get(name) == context_inputs.get(name)]
        review = {"inventory_sha256": dataset_context["inventory_sha256"],
                  "affected_descriptions": review_candidates,
                  "processed_descriptions": sorted(n for n in selected if args.model and n in context_inputs and applied_inputs.get(n) == context_inputs[n]),
                  "context_flags": flags, "feature_analysis": feature_audit}
        _atomic_json(out / "context_review.json", review)
        if args.model:
            _atomic_json(out / "context_manifest.json", {"manifest_version": "1.0",
                         "applied": applied_inputs, "context_flags": context_flags})
        if inventory is None:
            raise RuntimeError("Context audit requires a loaded context inventory")
        rendered_context_pages = render_context_pages(
            inventory, dataset_context, families, relationships, review, family_analysis,
        )
        audit_body = rendered_context_pages.pop("audit.html", "")
        if context_pages_enabled:
            titles = {"dataset.html": "Dataset architecture and glossary",
                      "relationships.html": "Feature relationship index"}
            for filename, body in rendered_context_pages.items():
                page(filename, titles[filename], body)
    cards = [("features.html", "Explore features"), ("structure.html", "Browse corpus structure"),
             ("diagram.html", "Explore the corpus diagram"), ("text.html", "Inspect transcription and encoding")]
    if context_pages_enabled:
        cards.extend([("dataset.html", "Dataset architecture and glossary"),
                      ("relationships.html", "Feature relationship index")])
    if not audit_body:
        audit_body = _fallback_audit_body(feature_audit, application)
    page("audit.html", "Audit report", audit_body)
    page("index.html",corpus, f'<p>{len(files)} feature files · {len(order)} node types · {api.F.otype.maxSlot:,} {e(api.F.otype.slotType)} slots</p><p>{e(outline)}</p>' + provenance_description + overview_description + '<div class="cards">' + "".join(link(url,title) for url,title in cards) + "</div>")


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
    parser.add_argument("--app-dir", type=Path, metavar="DIR",
                        help="Text-Fabric app directory to include in dataset inference (defaults to the corpus repository's app directory)")
    parser.add_argument("--dataset-instructions", type=Path, metavar="FILE",
                        help="Optional UTF-8 instruction file for dataset-level context inference")
    parser.add_argument("--provider", choices=PROVIDERS, default="openrouter", help="LLM provider (default: openrouter)")
    parser.add_argument("--model", help="Chat model ID on the selected provider; omit for an offline build")
    parser.add_argument("--dataset-context", type=Path, metavar="FILE", help="UTF-8 editor notes to include with each selected feature")
    parser.add_argument("--overview-notes", type=Path, metavar="FILE", help="UTF-8 editor-supplied prose to include on the corpus overview page")
    parser.add_argument("--context-dir", type=Path, metavar="DIR",
                        help="Use matching dataset_context.json, feature_families.json, and feature_relationships.json for enrichment")
    parser.add_argument("--context-pages", action="store_true",
                        help="With --context-dir, add dataset architecture, glossary, relationship, and review pages")
    parser.add_argument("--feature-model", help="Model for feature descriptions (defaults to --model)")
    parser.add_argument("--targeted-evidence", action="store_true",
                        help="Let the model request missing feature evidence, retrieve it locally, then generate the description")
    parser.add_argument("--describe-features", metavar="NAMES", help="Comma-separated features to enrich; all pages are still built")
    parser.add_argument("--model-attribution", choices=("feature", "overview", "none"), default="feature",
                        help="Retained for CLI compatibility; model details now appear beside inferred content")
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
        if args.dataset_instructions and not args.analyze_context:
            parser.error("--dataset-instructions requires --analyze-context")
        if args.analyze_context:
            dataset_model = args.context_model or args.model
            family_model = args.family_model or dataset_model
            if not dataset_model:
                parser.error("--analyze-context requires --context-model or --model")
            from .context import analyze_context
            result = analyze_context(args.corpus, args.analyze_context, args.provider,
                                     dataset_model, family_model, args.cache, args.app_dir,
                                     args.dataset_instructions)
            logger.info("Context artifacts written to %s", args.analyze_context)
            logger.info("Inventory SHA-256: %s", result["inventory_sha256"])
            return
        if args.export_inventory:
            export_inventory(args.corpus, args.export_inventory, args.app_dir)
            return
        if args.output is None:
            parser.error("output is required unless --export-inventory is used")
        generate(args)
    except (TypeError, ValueError, OSError, RuntimeError) as error:
        parser.exit(1, f"doc4cf: {error}\n")
