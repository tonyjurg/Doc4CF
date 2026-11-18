"""Build current and published-release Doc4CF API documentation."""

import argparse
import hashlib
import html.parser
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import venv
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "tonyjurg/Doc4CF"


class VersionOptions(html.parser.HTMLParser):
    """Collect version-selector options from a rendered HTML page."""

    def __init__(self):
        super().__init__()
        self.options = []

    def handle_starttag(self, tag, attrs):
        if tag == "option":
            self.options.append(dict(attrs))


def git(*args: str) -> str:
    """Run a Git command against the repository without invoking a shell."""
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def safe_version_path(tag: str) -> str:
    """Return a stable path segment for a release tag."""
    if re.fullmatch(r"v?\d+(?:\.\d+)+(?:[-+][A-Za-z0-9.-]+)?", tag):
        return tag
    return "tag-" + hashlib.sha256(tag.encode("utf-8")).hexdigest()[:16]


def published_release_tags() -> list[str]:
    """Return published GitHub release tags, newest first."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "doc4cf-api-docs",
    }
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    releases = []
    page = 1
    while True:
        request = Request(
            f"https://api.github.com/repos/{REPOSITORY}/releases"
            f"?per_page=100&page={page}",
            headers=headers,
        )
        with urlopen(request, timeout=30) as response:
            batch = json.load(response)
        releases.extend(
            item for item in batch
            if not item.get("draft") and item.get("published_at")
        )
        if len(batch) < 100:
            break
        page += 1
    releases.sort(key=lambda item: item["published_at"], reverse=True)
    return list(dict.fromkeys(item["tag_name"] for item in releases))


def verify_selector(page: Path, entries: list[dict], selected: Path) -> None:
    """Reject missing version options, broken links, or the wrong selected entry."""
    parser = VersionOptions()
    parser.feed(page.read_text(encoding="utf-8"))
    expected = [(entry["output"] / "index.html").resolve() for entry in entries]
    actual = [(page.parent / option["value"]).resolve() for option in parser.options]
    if actual != expected or any(not target.is_file() for target in actual):
        raise RuntimeError(f"Broken API version selector in {page}")
    selected_links = [
        target
        for target, option in zip(actual, parser.options, strict=True)
        if "selected" in option
    ]
    if selected_links != [(selected / "index.html").resolve()]:
        raise RuntimeError(f"Incorrect selected API version in {page}")


def build_one(source: Path, output: Path, label: str, entries: list[dict], python: Path) -> None:
    """Build one source revision with links to every available API version."""
    versions = [
        {
            "label": entry["label"],
            "relative_url": Path(
                os.path.relpath(entry["output"] / "index.html", output / "_static")
            ).as_posix(),
        }
        for entry in entries
    ]
    environment = {
        **os.environ,
        "DOC4CF_DOCS_SOURCE": str(source),
        "DOC4CF_DOCS_VERSION": label,
        "DOC4CF_DOCS_VERSIONS": json.dumps(versions),
    }
    subprocess.run(
        [
            str(python), "-m", "sphinx", "-E", "-W", "--keep-going",
            "-b", "html", str(source / "docs" / "api"), str(output),
        ],
        cwd=source,
        env=environment,
        check=True,
    )


def release_source(tag: str, workspace: Path) -> Path:
    """Check out a release tag into a temporary, detached repository clone."""
    source = workspace / "source"
    subprocess.run(
        ["git", "clone", "--quiet", "--no-hardlinks", "--no-checkout", str(ROOT), str(source)],
        check=True,
    )
    subprocess.run(["git", "checkout", "--quiet", "--detach", tag], cwd=source, check=True)
    if not (source / "docs" / "api" / "conf.py").is_file():
        raise RuntimeError(f"Release {tag} does not contain the Sphinx API documentation setup")
    return source


def docs_dependencies() -> list[str]:
    """Read Sphinx build dependencies from the project configuration."""
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    return project["optional-dependencies"]["docs"]


def build_release(source: Path, output: Path, tag: str, entries: list[dict], dependencies: list[str]) -> None:
    """Install a release in an isolated environment and build its API docs."""
    with tempfile.TemporaryDirectory(prefix="doc4cf-api-venv-") as temporary:
        environment = Path(temporary) / "venv"
        venv.EnvBuilder(with_pip=True).create(environment)
        python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        subprocess.run(
            [str(python), "-m", "pip", "install", "--disable-pip-version-check", str(source), *dependencies],
            check=True,
        )
        build_one(source, output, tag, entries, python)


def main() -> None:
    """Build current documentation and published releases into one static tree."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(".cache/pages-site/api"))
    parser.add_argument(
        "--current-only",
        action="store_true",
        help="Build only the current source without querying GitHub releases.",
    )
    args = parser.parse_args()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    tags = [] if args.current_only else published_release_tags()
    entries = [{
        "label": f"Current (main · {tomllib.loads((ROOT / 'pyproject.toml').read_text(encoding='utf-8'))['project']['version']})",
        "output": output,
        "revision": git("rev-parse", "HEAD"),
        "tag": None,
    }]
    for tag in tags:
        revision = git("rev-parse", f"refs/tags/{tag}^{{commit}}")
        if any(entry.get("tag") == tag for entry in entries):
            continue
        entries.append({
            "label": tag,
            "output": output / "versions" / safe_version_path(tag),
            "revision": revision,
            "tag": tag,
        })

    dependencies = docs_dependencies()
    with tempfile.TemporaryDirectory(prefix="doc4cf-api-build-", dir=output.parent) as temporary:
        stage = Path(temporary) / "api"
        entries[0]["output"] = stage
        for entry in entries[1:]:
            entry["output"] = stage / "versions" / safe_version_path(entry["tag"])
        build_one(ROOT, stage, entries[0]["label"], entries, Path(sys.executable))
        for entry in entries[1:]:
            with tempfile.TemporaryDirectory(prefix="doc4cf-api-release-") as temporary_release:
                workspace = Path(temporary_release)
                source = release_source(entry["tag"], workspace)
                build_release(source, entry["output"], entry["tag"], entries, dependencies)

        for entry in entries:
            if not (entry["output"] / "index.html").is_file():
                raise RuntimeError(f"Missing API documentation for {entry['label']}")
            for name in ("index.html", "modules.html"):
                verify_selector(entry["output"] / name, entries, entry["output"])
            for page in (entry["output"] / "_modules").rglob("*.html"):
                verify_selector(page, entries, entry["output"])
        (stage / "versions.json").write_text(
            json.dumps(
                [
                    {
                        "label": entry["label"],
                        "path": entry["output"].relative_to(stage).as_posix(),
                        "revision": entry["revision"],
                    }
                    for entry in entries
                ],
                indent=2,
            ) + "\n",
            encoding="utf-8",
        )
        if output.exists():
            # Never delete a directory that is not a previous API build (for example
            # "--output ." would otherwise remove the whole checkout).
            if any(output.iterdir()) and not (output / "versions.json").is_file():
                raise SystemExit(f"Refusing to delete {output}: not a previous Doc4CF API build")
            shutil.rmtree(output)
        shutil.move(str(stage), str(output))


if __name__ == "__main__":
    main()
