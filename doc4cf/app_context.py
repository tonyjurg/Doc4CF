"""Extract inference context from a Text-Fabric app directory without executing it."""
from __future__ import annotations

import ast
from datetime import date, datetime
import hashlib
import json
from pathlib import Path
import re
from typing import Any
from urllib.parse import urlparse

import yaml


_MAX_DOCSTRING = 1800
_MAX_APP_FILES = 100
_MAX_APP_CONTEXT_CHARS = 32000
_MAX_FILE_BYTES = 256 * 1024
_MAX_LINKED_DOC_FILES = 80
_MAX_LINKED_DOC_BYTES = 64 * 1024
_MAX_LINKED_DOC_FILE_BYTES = 12 * 1024
_MAX_YAML_NODES = 5000
_SENSITIVE_NAME_PARTS = ("password", "passwd", "secret", "token", "credential", "api_key", "apikey",
                         "private_key", "privatekey")
# Whole-word name parts: matching these as substrings would hit e.g. "keyword".
_SENSITIVE_NAME_WORDS = frozenset({"key", "keys", "auth", "authorization", "cookie", "cookies",
                                   "bearer", "session", "private", "pwd", "pass"})
_OPAQUE_SECRET = re.compile(r"[A-Za-z0-9+/=_-]{32,}")
_URL_USERINFO = re.compile(r"(://)[^/\s:@]+:[^/\s@]+@")
_TOKEN_PATTERNS = re.compile(
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----"
    r"|\bgh[pousr]_[A-Za-z0-9]{20,}|\bgithub_pat_[A-Za-z0-9_]{20,}"
    r"|\bxox[abprs]-[A-Za-z0-9-]{10,}|\bsk-[A-Za-z0-9_-]{20,}"
    r"|\b(?:AKIA|ASIA)[A-Z0-9]{16}\b|\bAIza[A-Za-z0-9_-]{30,}"
)
_REDACTED = "<redacted>"


class _TooLarge(ValueError):
    """Raised when untrusted configuration exceeds the node budget."""


def _is_sensitive_name(name: str) -> bool:
    """Return True when an identifier or key looks like it names a credential."""
    lowered = name.lower()
    if any(part in lowered for part in _SENSITIVE_NAME_PARTS):
        return True
    spaced = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    words = re.split(r"[^A-Za-z0-9]+", spaced.lower())
    return any(word in _SENSITIVE_NAME_WORDS for word in words)


def _is_sensitive_value(value: str) -> bool:
    """Return True when the whole value is one long opaque token."""
    return bool(_OPAQUE_SECRET.fullmatch(value.strip()))


def _clip(value: str, limit: int = _MAX_DOCSTRING) -> str:
    value = " ".join(value.split())
    return value if len(value) <= limit else value[:limit].rsplit(" ", 1)[0] + " …"


def _scrub(value: str) -> str:
    """Mask credentials embedded in free text such as docstrings."""
    value = _URL_USERINFO.sub(r"\1" + _REDACTED + "@", value)
    return _TOKEN_PATTERNS.sub(_REDACTED, value)


def _clean_text(value: str, limit: int) -> str:
    if _is_sensitive_value(value):
        return _REDACTED
    return _clip(_scrub(value), limit)


def _clean_config_text(value: str, limit: int = 1000) -> str:
    """Bound and redact config strings without changing meaningful whitespace."""
    if _is_sensitive_value(value):
        return _REDACTED
    value = _scrub(value)
    return value if len(value) <= limit else value[:limit] + " …"


def _clean_document_text(value: str, limit: int) -> str:
    if _is_sensitive_value(value):
        return _REDACTED
    value = _scrub(value.replace("\r\n", "\n").replace("\r", "\n"))
    return value if len(value) <= limit else value[:limit] + "\n…"


def _normalize_yaml(value: Any, depth: int = 0, budget: list[int] | None = None) -> Any:
    """Copy a YAML tree into plain, bounded, redacted JSON-safe values.

    YAML aliases share one object between many places, so walking the loaded
    tree can visit exponentially many nodes. ``budget`` counts every visited
    node and raises :class:`_TooLarge` when the allowance is spent.
    """
    if budget is None:
        budget = [_MAX_YAML_NODES]
    budget[0] -= 1
    if budget[0] < 0:
        raise _TooLarge("configuration exceeds the node budget")
    if depth > 10:
        return "<nested configuration omitted>"
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, str):
        return _clean_config_text(value)
    if isinstance(value, list):
        return [_normalize_yaml(item, depth + 1, budget) for item in value[:200]]
    if isinstance(value, dict):
        normalized = {}
        for key, item in list(value.items())[:200]:
            name = str(key)
            if _is_sensitive_name(name):
                normalized[name] = _REDACTED
            else:
                normalized[name] = _normalize_yaml(item, depth + 1, budget)
        return normalized
    return _clean_text(str(value), 500)


def _source_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _selected_config(config: Any) -> dict[str, Any]:
    if not isinstance(config, dict):
        return {}
    # Keep the complete configuration tree so datasets can add their own
    # meaningful app keys without requiring changes to Doc4CF. Normalize YAML
    # scalars and redact values that look like credentials.
    return _normalize_yaml(config)


def _call_name(node: ast.expr) -> str:
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
    return ".".join(reversed(parts))


def _target_name(node: ast.expr) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{_target_name(node.value)}.{node.attr}"
    if isinstance(node, ast.Subscript):
        is_literal, value = _json_literal(node.slice)
        suffix = repr(value) if is_literal else "<dynamic>"
        return f"{_target_name(node.value)}[{suffix}]"
    return type(node).__name__


def _json_literal(node: ast.expr) -> tuple[bool, Any]:
    try:
        value = ast.literal_eval(node)
    except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
        return False, None

    def normalize(item, depth=0):
        if depth > 8:
            raise ValueError("literal nesting limit")
        if item is None or isinstance(item, (bool, int, float)):
            return item
        if isinstance(item, str):
            return _clean_text(item, 500)
        if isinstance(item, (list, tuple)):
            return [normalize(part, depth + 1) for part in item[:100]]
        if isinstance(item, (set, frozenset)):
            return sorted((normalize(part, depth + 1) for part in item), key=str)
        if isinstance(item, dict) and all(isinstance(key, str) for key in item):
            return {key: _REDACTED if _is_sensitive_name(key) else normalize(part, depth + 1)
                    for key, part in list(item.items())[:100]}
        raise TypeError("not a JSON-safe literal")

    try:
        return True, normalize(value)
    except (TypeError, ValueError, RecursionError):
        return False, None


def _literal_settings(body: list[ast.stmt]) -> list[dict[str, Any]]:
    settings = []
    for node in ast.walk(ast.Module(body=body, type_ignores=[])):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        value_node = node.value
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if value_node is None or not isinstance(value_node, (ast.Dict, ast.List, ast.Tuple, ast.Constant)):
            continue
        for target in targets:
            target_name = _target_name(target)
            if _is_sensitive_name(target_name):
                continue
            is_literal, value = _json_literal(value_node)
            if not is_literal:
                continue
            settings.append({"line": node.lineno, "target": target_name, "value": value})
    settings.sort(key=lambda item: (item["line"], item["target"]))
    return settings


def _function_summary(node: ast.FunctionDef | ast.AsyncFunctionDef) -> dict[str, Any]:
    arguments = node.args
    params = [arg.arg for arg in [*arguments.posonlyargs, *arguments.args, *arguments.kwonlyargs]]
    if arguments.vararg:
        params.append("*" + arguments.vararg.arg)
    if arguments.kwarg:
        params.append("**" + arguments.kwarg.arg)
    calls = []
    for item in ast.walk(node):
        if not isinstance(item, ast.Call):
            continue
        name = _call_name(item.func)
        capture_arguments = (name.startswith("app.") or name in {
            "displaySetup", "displayReset", "loadModule", "atfApi", "types.MethodType", "Fs",
        })
        args = []
        for value in item.args:
            is_literal, literal = _json_literal(value) if capture_arguments else (False, None)
            args.append(literal if is_literal else "<dynamic>")
        keywords: dict[str, Any] = {}
        for keyword in item.keywords:
            if keyword.arg is None:
                keywords["**"] = _call_name(keyword.value)
            elif _is_sensitive_name(keyword.arg):
                keywords[keyword.arg] = _REDACTED
            else:
                is_literal, literal = _json_literal(keyword.value) if capture_arguments else (False, None)
                keywords[keyword.arg] = literal if is_literal else "<dynamic>"
        calls.append({"call": name, "arguments": args, "keywords": keywords})
    calls.sort(key=lambda item: (item["call"], str(item["arguments"]), str(item["keywords"])))
    control_flow = []
    for branch in (item for item in ast.walk(node) if isinstance(item, ast.If)):
        branch_calls = []
        for item in ast.walk(ast.Module(body=branch.body, type_ignores=[])):
            if isinstance(item, ast.Call):
                branch_calls.append(_call_name(item.func))
        control_flow.append({
            "line": branch.lineno,
            "condition": _clean_text(ast.unparse(branch.test), 500),
            "calls": sorted(set(branch_calls))[:30],
            "static_assignments": _literal_settings(branch.body)[:30],
        })
    # Include only statically recoverable settings and direct dispatch values.
    dispatch = []
    for item in ast.walk(node):
        if isinstance(item, ast.Compare) and isinstance(item.left, ast.Name):
            values = [_clean_text(value.value, 200) for value in item.comparators
                      if isinstance(value, ast.Constant) and isinstance(value.value, str)]
            if values:
                dispatch.append({"parameter": item.left.id, "values": values})
    return {
        "name": node.name,
        "parameters": params,
        "docstring": _clean_text(ast.get_docstring(node) or "", _MAX_DOCSTRING),
        "calls": calls[:60],
        "control_flow": control_flow[:30],
        "dispatch": dispatch[:20],
        "static_assignments": _literal_settings(node.body),
    }


def _python_summary(path: Path, relative_path: str) -> dict[str, Any]:
    source = path.read_text(encoding="utf-8-sig")
    try:
        tree = ast.parse(source, filename=relative_path)
    except (MemoryError, RecursionError) as error:
        raise SyntaxError(type(error).__name__) from error
    classes = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        methods = [_function_summary(item) for item in node.body
                   if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))]
        classes.append({
            "name": node.name,
            "bases": [_call_name(base) for base in node.bases],
            "methods": methods,
        })
    functions = [_function_summary(node) for node in tree.body
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    constants = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, (ast.Constant, ast.List, ast.Tuple)):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.isupper():
                    if _is_sensitive_name(target.id):
                        continue
                    is_literal, literal = _json_literal(node.value)
                    if is_literal:
                        constants[target.id] = literal
    return {
        "path": relative_path,
        "module_docstring": _clean_text(ast.get_docstring(tree) or "", _MAX_DOCSTRING),
        "classes": classes,
        "functions": functions,
        "constants": constants,
    }


def _walk_config(value: Any, path: str = "configuration"):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from _walk_config(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk_config(item, f"{path}[{index}]")
    else:
        yield path, value


def _local_doc_path(value: str, repo_root: Path, key_path: str, feature: str | None = None) -> Path | None:
    """Resolve only explicitly configured documentation pointers inside the checkout."""
    candidate = value
    for marker in ("<feature>", "{feature}", "${feature}"):
        candidate = candidate.replace(marker, feature or "__feature__")
    candidate = candidate.strip()
    parsed = urlparse(candidate)
    if parsed.scheme in {"http", "https"}:
        if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
            return None
        parts = [part for part in parsed.path.split("/") if part]
        if len(parts) < 5 or parts[2] not in {"blob", "tree"}:
            return None
        relative_parts = parts[4:]
        if parts[2] == "tree":
            return None
        relative = Path(*relative_parts)
    else:
        relative = Path(candidate)
        if not relative.name or relative.is_absolute() or ".." in relative.parts:
            return None
    if "__feature__" in str(relative):
        return None
    # Page names in app configs commonly omit the Markdown suffix.
    if not relative.suffix and "featurepage" in key_path.lower():
        relative = Path("docs/features") / relative.with_suffix(".md")
    elif not relative.suffix and "docpage" in key_path.lower():
        relative = Path("docs") / relative.with_suffix(".md")
    path = (repo_root / relative).resolve()
    if not path.is_relative_to(repo_root) or path.suffix.lower() not in {".md", ".rst", ".txt"}:
        return None
    return path


def _linked_documentation(
    repo_root: Path, config: dict[str, Any], feature_names: list[str],
) -> tuple[dict[str, Any], list[dict[str, str]], list[str]]:
    """Harvest bounded, local docs explicitly referenced by app config."""
    refs = list(_walk_config(config))
    paths: dict[str, set[str]] = {name: set() for name in feature_names}
    dataset_paths: set[str] = set()
    for key_path, value in refs:
        if not isinstance(value, str) or not any(part in key_path.lower() for part in ("doc", "feature")):
            continue
        if any(marker in value for marker in ("<feature>", "{feature}", "${feature}")):
            for feature in feature_names:
                path = _local_doc_path(value, repo_root, key_path, feature)
                if path and path.is_file():
                    paths[feature].add(path.relative_to(repo_root).as_posix())
        else:
            path = _local_doc_path(value, repo_root, key_path)
            if path and path.is_file():
                dataset_paths.add(path.relative_to(repo_root).as_posix())
    documents: dict[str, Any] = {"dataset": [], "features": {}}
    hashes: list[dict[str, str]] = []
    skipped: list[str] = []
    loaded_docs: dict[str, dict[str, str]] = {}
    remaining = _MAX_LINKED_DOC_BYTES
    seen: set[str] = set()

    def read_doc(relative: str) -> dict[str, str] | None:
        nonlocal remaining
        if relative in loaded_docs:
            return loaded_docs[relative]
        if relative in seen:
            return None
        seen.add(relative)
        path = repo_root / relative
        try:
            size = path.stat().st_size
        except OSError:
            skipped.append(relative)
            return None
        if (len(seen) > _MAX_LINKED_DOC_FILES or size > _MAX_LINKED_DOC_FILE_BYTES
                or size > remaining or path.is_symlink()):
            skipped.append(relative)
            return None
        try:
            raw = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError):
            skipped.append(relative)
            return None
        remaining -= len(raw.encode("utf-8"))
        digest = _source_hash(path)
        hashes.append({"path": relative, "sha256": digest})
        doc = {"path": relative, "sha256": digest,
               "text": _clean_document_text(raw, _MAX_LINKED_DOC_FILE_BYTES)}
        loaded_docs[relative] = doc
        return doc

    for relative in sorted(dataset_paths):
        doc = read_doc(relative)
        if doc:
            documents["dataset"].append(doc)
    for feature in feature_names:
        selected = []
        for relative in sorted(paths[feature]):
            doc = read_doc(relative)
            if doc:
                selected.append(doc)
        if selected:
            documents["features"][feature] = selected
    if skipped:
        skipped = sorted(set(skipped))
    return documents, hashes, skipped


def _feature_application_links(
    config: dict[str, Any], feature_names: list[str], feature_metadata: dict[str, dict[str, Any]],
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Connect configured feature references and text-format placeholders to features."""
    leaves = list(_walk_config(config))
    result = {}
    for feature in feature_names:
        refs = []
        documentation_links = []
        for path, value in leaves:
            if (isinstance(value, str) and "featurebase" in path.lower()
                    and any(marker in value for marker in ("<feature>", "{feature}", "${feature}"))):
                template = value
                for marker in ("<feature>", "{feature}", "${feature}"):
                    template = template.replace(marker, feature)
                parsed = urlparse(template)
                local_doc = _local_doc_path(value, repo_root, path, feature) if repo_root else None
                if (parsed.scheme in {"http", "https"} and parsed.netloc and not parsed.username
                        and local_doc is not None and local_doc.is_file()):
                    documentation_links.append({
                        "configuration_path": path,
                        "source_path": local_doc.relative_to(repo_root).as_posix(),
                        "url": template,
                    })
            values = value if isinstance(value, list) else [value]

            def refers_to_feature(item: Any, feature_name: str = feature) -> bool:
                if item == feature_name:
                    return True
                if not isinstance(item, str):
                    return False
                parsed = urlparse(item)
                if parsed.scheme in {"http", "https"}:
                    return False
                tokens = re.findall(r"[A-Za-z0-9_@.-]+", item)
                return feature_name in tokens or "{" + feature_name + "}" in item

            if any(refers_to_feature(item) for item in values):
                refs.append({"path": path, "value": value})
        formats = []
        for metadata_feature, metadata in feature_metadata.items():
            for key, value in metadata.items():
                if not key.startswith("fmt:") or not isinstance(value, str):
                    continue
                placeholders = re.findall(r"\{([^{}]+)\}", value)
                if feature in placeholders:
                    formats.append({"metadata_path": f"features.{metadata_feature}.metadata.{key}",
                                    "template": value, "placeholders": placeholders,
                                    "uses_this_feature": True})
        if refs or formats or documentation_links:
            result[feature] = {"configuration_references": refs, "text_formats": formats,
                               "documentation_links": documentation_links}
    return result


def extract_app_context(
    corpus: Path, app_dir: Path | None = None, feature_names: list[str] | None = None,
    feature_metadata: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any] | None:
    """Summarize nearby app configuration and Python behavior as untrusted evidence.

    ``corpus`` is normally ``<repository>/tf/<version>``. Its sibling app
    directory is discovered automatically. Python files are parsed, never
    imported or executed.
    """
    corpus = Path(corpus).resolve()
    app = Path(app_dir).resolve() if app_dir else corpus.parent.parent / "app"
    if app_dir is not None and not app.is_dir():
        raise FileNotFoundError(f"Text-Fabric app directory does not exist: {app}")
    if not app.is_dir():
        return None
    repo_root = app.parent
    candidates, skipped = _eligible_files(app)
    if not candidates:
        return None
    all_files = candidates[:_MAX_APP_FILES]
    omitted_count = len(candidates) - len(all_files)
    yaml_files = [path for path in all_files if path.suffix.lower() in {".yaml", ".yml"}]
    configuration: dict[str, Any] = {}
    additional_configuration = {}
    file_hashes = [{"path": path.relative_to(repo_root).as_posix(), "sha256": _source_hash(path)}
                   for path in all_files]
    primary_config = app / "config.yaml"
    if primary_config not in yaml_files and yaml_files:
        primary_config = yaml_files[0]
    for config_path in yaml_files:
        relative_path = config_path.relative_to(repo_root).as_posix()
        try:
            loaded = yaml.safe_load(config_path.read_text(encoding="utf-8-sig")) or {}
            parsed_config = _selected_config(loaded)
        except (OSError, UnicodeError, yaml.YAMLError, RecursionError):
            parsed_config = {"parse_status": "YAML could not be parsed safely"}
        except _TooLarge:
            parsed_config = {"parse_status": "YAML configuration too large to summarize"}
        if config_path == primary_config:
            configuration = parsed_config
        else:
            additional_configuration[relative_path] = parsed_config
    python_files = []
    for path in all_files:
        relative_path = path.relative_to(repo_root).as_posix()
        if path.suffix.lower() != ".py":
            continue
        try:
            python_files.append(_python_summary(path, relative_path))
        except (OSError, UnicodeError, SyntaxError, ValueError) as error:
            python_files.append({"path": relative_path, "parse_status": f"Python AST unavailable: {type(error).__name__}"})
    result: dict[str, Any] = {"configuration": configuration,
              "additional_configuration": additional_configuration,
              "python_behavior": python_files, "source_files": file_hashes}
    names = sorted(feature_names or [])
    all_configuration = dict(configuration)
    if additional_configuration:
        all_configuration["additional_configuration"] = additional_configuration
    docs, doc_hashes, skipped_docs = _linked_documentation(repo_root, all_configuration, names)
    if docs["dataset"] or docs["features"]:
        result["linked_documentation"] = docs
    result["feature_application_links"] = _feature_application_links(
        all_configuration, names, feature_metadata or {}, repo_root)
    known_hashes = {item["path"] for item in file_hashes}
    file_hashes.extend(item for item in doc_hashes if item["path"] not in known_hashes)
    if skipped_docs:
        result["skipped_documentation"] = skipped_docs
    if omitted_count:
        result["omitted_file_count"] = omitted_count
    if skipped:
        result["skipped_files"] = skipped
    _enforce_size_cap(result)
    return result


def _eligible_files(app: Path) -> tuple[list[Path], list[str]]:
    """List regular YAML/Python files that really live inside ``app``.

    Symbolic links are never followed (a cloned repository could point them
    at files outside the app directory) and oversized files are skipped
    before they are read, hashed, or parsed.
    """
    root = app.resolve()
    eligible: list[Path] = []
    skipped: list[str] = []
    for path in sorted(app.rglob("*")):
        if path.suffix.lower() not in {".yaml", ".yml", ".py"}:
            continue
        relative = path.relative_to(app.parent).as_posix()
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root):
            skipped.append(f"{relative} (symbolic link or outside app directory)")
        elif path.stat().st_size > _MAX_FILE_BYTES:
            skipped.append(f"{relative} (larger than {_MAX_FILE_BYTES} bytes)")
        else:
            eligible.append(path)
    return eligible, skipped[:_MAX_APP_FILES]


def _size(result: dict[str, Any]) -> int:
    return len(json.dumps(result, ensure_ascii=False, default=str))


def _enforce_size_cap(result: dict[str, Any]) -> None:
    """Shrink ``result`` in place until it fits the prompt-size allowance.

    Linked-document text and derived links are reduced first, followed by
    Python summaries and additional configuration, preserving the primary
    configuration wherever possible.
    """
    linked = result.get("linked_documentation", {})
    for collection in (linked.get("features", {}).values(), [linked.get("dataset", [])]):
        for documents in collection:
            for document in documents:
                if _size(result) <= _MAX_APP_CONTEXT_CHARS:
                    break
                text = document.get("text", "")
                overflow = _size(result) - _MAX_APP_CONTEXT_CHARS
                document["text"] = text[:max(0, len(text) - overflow - 32)] + " …"
    while _size(result) > _MAX_APP_CONTEXT_CHARS and linked.get("features"):
        name = next(reversed(linked["features"]))
        linked["features"].pop(name)
        result.setdefault("omitted_feature_documentation", []).append(name)
    while _size(result) > _MAX_APP_CONTEXT_CHARS and linked.get("dataset"):
        linked["dataset"].pop()
        result.setdefault("omitted_dataset_documentation", 0)
        result["omitted_dataset_documentation"] += 1
    feature_links = result.get("feature_application_links", {})
    while _size(result) > _MAX_APP_CONTEXT_CHARS and feature_links:
        feature_links.pop(next(reversed(feature_links)))
        result["omitted_feature_application_links"] = True
    omitted_python = []
    python_files = result["python_behavior"]
    while _size(result) > _MAX_APP_CONTEXT_CHARS and python_files:
        omitted_python.append(python_files.pop()["path"])
    if omitted_python:
        result["omitted_python_behavior"] = list(reversed(omitted_python))
    additional = result["additional_configuration"]
    omitted_config = []
    while _size(result) > _MAX_APP_CONTEXT_CHARS and additional:
        largest = max(additional, key=lambda name: len(json.dumps(additional[name], default=str)))
        omitted_config.append(largest)
        del additional[largest]
    if omitted_config:
        result["omitted_additional_configuration"] = sorted(omitted_config)
    configuration = result["configuration"]
    for name in sorted(configuration, key=lambda key: -len(json.dumps(configuration[key], default=str))):
        if _size(result) <= _MAX_APP_CONTEXT_CHARS:
            break
        configuration[name] = "<omitted: too large>"
