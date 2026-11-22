"""Regression checks for documentation roots."""
import json
import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from doc4cf import app_context


class DocumentationRoots(unittest.TestCase):
    def test_allowed_directories_and_project_markers(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            (root / "pyproject.toml").write_text("", encoding="utf-8")
            for relative in ("app/readme.md", "docs/f.md", "doc/f.rst", "documentation/f.txt", "README.md"):
                self.assertEqual(app_context._local_doc_path(relative, root, "docs"), root / relative)
            for relative in (".hidden.md", "docs/.hidden/f.md", "private/f.txt", "../outside.md"):
                self.assertIsNone(app_context._local_doc_path(relative, root, "docs"))

    def test_documentation_symlinks_are_not_followed(self):
        with TemporaryDirectory() as tmp:
            corpus, app = self.tree(tmp, "tf")
            root = app.parent
            try:
                os.symlink(root / "top.md", root / "docs" / "alias.md")
                os.symlink(root / "Documents", root / "docs" / "alias", target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            for relative in ("docs/alias.md", "docs/alias/private.txt"):
                self.assertIsNone(app_context._local_doc_path(relative, root, "docs"))
            self.assertTrue(corpus.is_dir())

    def tree(self, tmp, marker):
        root = Path(tmp) / "proj"
        (root / "app").mkdir(parents=True)
        (root / "docs").mkdir()
        (root / "Documents").mkdir()
        (root / ".ssh").mkdir()
        if marker:
            (root / marker).mkdir()
        for rel in ("docs/ok.md", "Documents/private.txt", ".ssh/notes.txt", "top.md"):
            (root / rel).write_text(f"CONTENT_{rel}", encoding="utf-8")
        (root / "app" / "config.yaml").write_text(
            'docs:\n  a: docs/ok.md\n  b: Documents/private.txt\n  c: .ssh/notes.txt\n  d: top.md\n', encoding="utf-8")
        corpus = root / "tf" / "1.0"
        corpus.mkdir(parents=True, exist_ok=True)
        return corpus, root / "app"

    def test_only_docs_app_and_root_files_in_a_project_root(self):
        with TemporaryDirectory() as tmp:
            corpus, app = self.tree(tmp, "tf")
            blob = json.dumps(app_context.extract_app_context(corpus, app, ["f"], {}))
            self.assertIn("CONTENT_docs/ok.md", blob)
            self.assertIn("CONTENT_top.md", blob)
            self.assertNotIn("CONTENT_Documents", blob)
            self.assertNotIn("CONTENT_.ssh", blob)

    def test_directories_that_are_not_projects_are_never_searched(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp) / "home"
            (root / "tf_app").mkdir(parents=True)
            (root / "docs").mkdir()
            (root / "docs" / "ok.md").write_text("HOME_DOC", encoding="utf-8")
            (root / "tf_app" / "config.yaml").write_text("docs:\n  a: docs/ok.md\n", encoding="utf-8")
            corpus = Path(tmp) / "elsewhere" / "tf" / "1.0"
            corpus.mkdir(parents=True)
            blob = json.dumps(app_context.extract_app_context(corpus, root / "tf_app", ["f"], {}))
            self.assertNotIn("HOME_DOC", blob)


class MalformedUrls(unittest.TestCase):
    def test_malformed_urls_in_app_config_do_not_abort_extraction(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp) / "proj"
            (root / "app").mkdir(parents=True)
            (root / "tf" / "1.0").mkdir(parents=True)
            (root / "app" / "config.yaml").write_text(
                "docs:\n  featureBase: 'http://[::1/<feature>'\n  page: 'http://[bad'\n  other: ['http://[x']\n",
                encoding="utf-8")
            result = app_context.extract_app_context(root / "tf" / "1.0", None, ["word"], {})
            self.assertIn("docs", result["configuration"])


if __name__ == "__main__":
    unittest.main()
