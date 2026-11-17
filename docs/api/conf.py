"""Sphinx configuration for the Doc4CF API reference."""

import json
import os
import sys
import tomllib
from pathlib import Path

ROOT = Path(os.environ.get("DOC4CF_DOCS_SOURCE", Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(ROOT))

project = "Doc4CF"
author = "Tony Jurg"
release = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))[
    "project"
]["version"]
version = release

docs_version = os.environ.get("DOC4CF_DOCS_VERSION", f"Current (main · {release})")
docs_versions = json.loads(os.environ.get("DOC4CF_DOCS_VERSIONS", "[]"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
]
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_default_options = {"members": True, "member-order": "bysource"}

root_doc = "index"
templates_path = ["_templates"]
exclude_patterns = ["_build"]
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
    "sticky_navigation": True,
    "titles_only": True,
    "logo_only": True,
}
html_logo = "_static/doc4cf-logo.svg"
html_favicon = "_static/doc4cf-logo.svg"
html_title = docs_version
html_static_path = ["_static"]
html_css_files = ["doc4cf-api.css"]
html_context = {
    "docs_version": docs_version,
    "docs_versions": docs_versions,
    "repository_url": "https://github.com/tonyjurg/Doc4CF",
    "documentation_url": "https://tonyjurg.github.io/Doc4CF/",
}
rst_prolog = f".. |docs_version| replace:: {docs_version}\n.. |release| replace:: {release}\n"
