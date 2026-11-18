"""Extract inference context from a Text-Fabric app directory without executing it."""
from __future__ import annotations

import ast
from datetime import date, datetime
import hashlib
from pathlib import Path
from typing import Any

import yaml


_MAX_DOCSTRING = 1800
_MAX_APP_FILES = 100
_MAX_APP_CONTEXT_CHARS = 32000
_SENSITIVE_NAME_PARTS = ("password", "secret", "token", "credential", "api_key", "apikey")


def _clip(value: str, limit: int = _MAX_DOCSTRING) -> str:
    value = " ".join(value.split())
    return value if len(value) <= limit else value[:limit].rsplit(" ", 1)[0] + " …"


def _normalize_yaml(value: Any, depth: int = 0) -> Any:
    if depth > 10:
        return "<nested configuration omitted>"
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, str):
        return _clip(value, 1000)
    if isinstance(value, list):
        return [_normalize_yaml(item, depth + 1) for item in value[:200]]
    if isinstance(value, dict):
        normalized = {}
        for key, item in list(value.items())[:200]:
            name = str(key)
            if any(part in name.lower() for part in _SENSITIVE_NAME_PARTS):
                normalized[name] = "<redacted>"
            else:
                normalized[name] = _normalize_yaml(item, depth + 1)
        return normalized
    return _clip(str(value), 500)


def _source_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
            return _clip(item, 500)
        if isinstance(item, (list, tuple)):
            return [normalize(part, depth + 1) for part in item[:100]]
        if isinstance(item, (set, frozenset)):
            return sorted((normalize(part, depth + 1) for part in item), key=str)
        if isinstance(item, dict) and all(isinstance(key, str) for key in item):
            return {key: normalize(part, depth + 1) for key, part in list(item.items())[:100]}
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
            if any(part in target_name.lower() for part in _SENSITIVE_NAME_PARTS):
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
            elif any(part in keyword.arg.lower() for part in _SENSITIVE_NAME_PARTS):
                keywords[keyword.arg] = "<redacted>"
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
    tree = ast.parse(source, filename=relative_path)
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
                    if any(part in target.id.lower() for part in _SENSITIVE_NAME_PARTS):
                        continue
                    try:
                        constants[target.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
                        pass
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
    all_files = sorted(path for path in app.rglob("*") if path.is_file()
                       and (path.suffix.lower() in {".yaml", ".yml", ".py"}))
    files = all_files[:_MAX_APP_FILES]
    if not files:
        return None
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
        except (OSError, UnicodeError, yaml.YAMLError):
            parsed_config = {"parse_status": "YAML could not be parsed safely"}
        if config_path == primary_config:
            configuration = parsed_config
        else:
            additional_configuration[relative_path] = parsed_config
    python_files = []
    for path in files:
        relative_path = path.relative_to(repo_root).as_posix()
        if path.suffix.lower() != ".py":
            continue
        try:
            python_files.append(_python_summary(path, relative_path))
        except (OSError, UnicodeError, SyntaxError) as error:
            python_files.append({"path": relative_path, "parse_status": f"Python AST unavailable: {type(error).__name__}"})
    result: dict[str, Any] = {"configuration": configuration,
              "additional_configuration": additional_configuration,
              "python_behavior": python_files, "source_files": file_hashes}
    if len(all_files) > len(files):
        result["omitted_file_count"] = len(all_files) - len(files)
    omitted_behavior = []
    while len(str(result)) > _MAX_APP_CONTEXT_CHARS and python_files:
        omitted_behavior.append(python_files.pop()["path"])
        result["python_behavior"] = python_files
    if omitted_behavior:
        result["omitted_python_behavior"] = list(reversed(omitted_behavior))
    return result
