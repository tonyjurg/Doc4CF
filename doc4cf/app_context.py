"""Extract inference context from a Text-Fabric app directory without executing it."""
from __future__ import annotations

import ast
from datetime import date, datetime
import hashlib
import json
from pathlib import Path
import re
from typing import Any

import yaml


_MAX_DOCSTRING = 1800
_MAX_APP_FILES = 100
_MAX_APP_CONTEXT_CHARS = 32000
_MAX_FILE_BYTES = 256 * 1024
_MAX_YAML_NODES = 5000
_SENSITIVE_NAME_PARTS = ("password", "passwd", "secret", "token", "credential", "api_key", "apikey",
                         "private_key", "privatekey")
# Whole-word name parts: matching these as substrings would hit e.g. "keyword".
_SENSITIVE_NAME_WORDS = frozenset({"key", "keys", "auth", "authorization", "cookie", "cookies",
                                   "bearer", "session", "private", "pwd", "pass"})
_URL_CREDENTIALS = re.compile(r"://[^/\s:@]+:[^/\s@]+@")
_OPAQUE_SECRET = re.compile(r"[A-Za-z0-9+/=_-]{32,}")
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
    """Return True for URLs with embedded credentials and long opaque tokens."""
    return bool(_URL_CREDENTIALS.search(value) or _OPAQUE_SECRET.fullmatch(value.strip()))


def _clip(value: str, limit: int = _MAX_DOCSTRING) -> str:
    value = " ".join(value.split())
    return value if len(value) <= limit else value[:limit].rsplit(" ", 1)[0] + " …"


def _clean_text(value: str, limit: int) -> str:
    return _REDACTED if _is_sensitive_value(value) else _clip(value, limit)


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
        return _clean_text(value, 1000)
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
    # Include only statically recoverable settings and direct dispatch values.
    dispatch = []
    for item in ast.walk(node):
        if isinstance(item, ast.Compare) and isinstance(item.left, ast.Name):
            values = [value.value for value in item.comparators if isinstance(value, ast.Constant)
                      and isinstance(value.value, str)]
            if values:
                dispatch.append({"parameter": item.left.id, "values": values})
    return {
        "name": node.name,
        "parameters": params,
        "docstring": _clip(ast.get_docstring(node) or ""),
        "calls": calls[:60],
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
        "module_docstring": _clip(ast.get_docstring(tree) or ""),
        "classes": classes,
        "functions": functions,
        "constants": constants,
    }


def extract_app_context(corpus: Path, app_dir: Path | None = None) -> dict[str, Any] | None:
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

    Python summaries go first, then additional configuration files, then the
    primary configuration, so the output stays bounded whatever the app holds.
    """
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
