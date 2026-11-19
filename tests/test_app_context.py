"""Hardening tests for harvesting a Text-Fabric app directory."""
import json
import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import yaml

from doc4cf import app_context


def make_corpus(tmp: str) -> tuple[Path, Path]:
    corpus = Path(tmp) / "repo" / "tf" / "1.0"
    app = Path(tmp) / "repo" / "app"
    corpus.mkdir(parents=True)
    app.mkdir(parents=True)
    (app / "config.yaml").write_text("provider: demo\nversion: 1\n", encoding="utf-8")
    return corpus, app


class AppContextHardening(unittest.TestCase):
    def test_symlinks_are_not_followed(self):
        with TemporaryDirectory() as tmp:
            corpus, app = make_corpus(tmp)
            outside = Path(tmp) / "outside.yaml"
            outside.write_text("marker: OUTSIDE_CONTENT\n", encoding="utf-8")
            outside_py = Path(tmp) / "outside.py"
            outside_py.write_text('"""OUTSIDE_DOC"""\n', encoding="utf-8")
            try:
                os.symlink(outside, app / "leak.yaml")
                os.symlink(outside_py, app / "leak.py")
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            result = app_context.extract_app_context(corpus)
            blob = json.dumps(result)
            self.assertNotIn("OUTSIDE_CONTENT", blob)
            self.assertNotIn("OUTSIDE_DOC", blob)
            self.assertEqual(len(result["skipped_files"]), 2)

    def test_alias_expansion_is_bounded(self):
        lines = ["l0: &l0 [x, x, x, x, x, x, x, x, x, x]"]
        for level in range(1, 12):
            lines.append(f"l{level}: &l{level} [{', '.join([f'*l{level - 1}'] * 10)}]")
        with TemporaryDirectory() as tmp:
            corpus, app = make_corpus(tmp)
            (app / "config.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")
            result = app_context.extract_app_context(corpus)
            self.assertIn("too large", result["configuration"]["parse_status"])

    def test_total_size_is_capped_for_yaml_only_apps(self):
        with TemporaryDirectory() as tmp:
            corpus, app = make_corpus(tmp)
            big = {f"key{i}": "word " * 190 for i in range(150)}
            (app / "config.yaml").write_text(yaml.safe_dump(big), encoding="utf-8")
            result = app_context.extract_app_context(corpus)
            self.assertLessEqual(len(json.dumps(result)), app_context._MAX_APP_CONTEXT_CHARS)

    def test_file_count_limit_applies_to_yaml_and_hashes(self):
        with TemporaryDirectory() as tmp:
            corpus, app = make_corpus(tmp)
            for i in range(150):
                (app / f"extra{i:03}.yaml").write_text(f"n: {i}\n", encoding="utf-8")
            result = app_context.extract_app_context(corpus)
            self.assertEqual(len(result["source_files"]), app_context._MAX_APP_FILES)
            self.assertEqual(result["omitted_file_count"], 151 - app_context._MAX_APP_FILES)
            self.assertLessEqual(len(result["additional_configuration"]) + 1, app_context._MAX_APP_FILES)

    def test_oversized_files_are_skipped_unread(self):
        with TemporaryDirectory() as tmp:
            corpus, app = make_corpus(tmp)
            (app / "huge.yaml").write_bytes(b"a: " + b"x" * (app_context._MAX_FILE_BYTES + 1) + b"\n")
            result = app_context.extract_app_context(corpus)
            self.assertEqual([item["path"] for item in result["source_files"]], ["app/config.yaml"])
            self.assertIn("huge.yaml", result["skipped_files"][0])

    def test_constants_are_json_safe_and_clipped(self):
        with TemporaryDirectory() as tmp:
            corpus, app = make_corpus(tmp)
            (app / "app.py").write_text(
                'MAGIC = b"abc"\nSIZES = (1, {2, 3})\nLONG = "' + "word " * 400 + '"\nOK = [1, 2]\n',
                encoding="utf-8")
            result = app_context.extract_app_context(corpus)
            json.dumps(result)
            constants = result["python_behavior"][0]["constants"]
            self.assertEqual(constants["OK"], [1, 2])
            self.assertEqual(constants["SIZES"], [1, [2, 3]])
            self.assertLessEqual(len(constants["LONG"]), 505)
            self.assertNotIn("MAGIC", constants)

    def test_credentials_are_redacted(self):
        with TemporaryDirectory() as tmp:
            corpus, app = make_corpus(tmp)
            (app / "app.py").write_text(
                'DB_URL = "postgres://admin:hunter2@db.corp/prod"\nPRIVATE_KEY_DATA = "AAAAKEY"\n'
                'SAFE = "plain text"\nKEYWORD = "kept"\n', encoding="utf-8")
            (app / "config.yaml").write_text(
                "endpoint: https://user:hunter2@api.corp/v1\nclient-key-data: AAAAKEY\nauth: abc123\n"
                "session_cookie: sid=deadbeef\nclientSecretValue: s3\nkeyword: kept\n"
                "blob: " + "A1b2" * 10 + "\n", encoding="utf-8")
            result = app_context.extract_app_context(corpus)
            text = json.dumps(result)
            for needle in ("hunter2", "AAAAKEY", "abc123", "deadbeef", "s3", "A1b2A1b2"):
                self.assertNotIn(needle, text)
            self.assertEqual(result["configuration"]["keyword"], "kept")
            constants = result["python_behavior"][0]["constants"]
            self.assertEqual(constants["SAFE"], "plain text")
            self.assertEqual(constants["KEYWORD"], "kept")

    def test_missing_explicit_app_dir_is_an_error(self):
        with TemporaryDirectory() as tmp:
            corpus, _ = make_corpus(tmp)
            with self.assertRaises(FileNotFoundError):
                app_context.extract_app_context(corpus, Path(tmp) / "nope")


if __name__ == "__main__":
    unittest.main()
