"""Unit tests for the helpers extracted from generate()."""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from doc4cf import generator


class ValidateOptions(unittest.TestCase):
    files = {"otype": {}, "oslots": {}, "word": {}}

    def args(self, **kw):
        return SimpleNamespace(model=kw.pop("model", None), **kw)

    def test_defaults_select_every_feature(self):
        self.assertEqual(generator._validate_options(self.args(), self.files), set(self.files))

    def test_feature_selection_is_stripped_and_checked(self):
        self.assertEqual(
            generator._validate_options(self.args(model="m", describe_features=" word , otype"), self.files),
            {"word", "otype"})
        with self.assertRaisesRegex(ValueError, "Unknown or empty feature names"):
            generator._validate_options(self.args(model="m", describe_features="nope"), self.files)

    def test_inconsistent_options_are_rejected(self):
        for kw, text in [({"feature_model": "x"}, "--feature-model requires --model"),
                         ({"context_pages": True}, "--context-pages requires --context-dir"),
                         ({"describe_features": "word"}, "require --model"),
                         ({"targeted_evidence": True, "model": "m"}, "--targeted-evidence requires")]:
            with self.subTest(kw=kw), self.assertRaisesRegex(ValueError, text):
                generator._validate_options(self.args(**kw), self.files)


class Manifest(unittest.TestCase):
    def test_missing_corrupt_and_wrong_shaped_manifests_are_empty(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "context_manifest.json"
            self.assertEqual(generator._load_manifest(path), ({}, {}))
            path.write_text("{not json", encoding="utf-8")
            self.assertEqual(generator._load_manifest(path), ({}, {}))
            path.write_text(json.dumps({"applied": [], "context_flags": "x"}), encoding="utf-8")
            self.assertEqual(generator._load_manifest(path), ({}, {}))
            path.write_text(json.dumps({"applied": {"a": {"model": "m"}}, "context_flags": {"a": []}}), encoding="utf-8")
            self.assertEqual(generator._load_manifest(path), ({"a": {"model": "m"}}, {"a": []}))


class ReviewCandidates(unittest.TestCase):
    def test_reports_new_and_changed_inputs(self):
        current = {"new": {"prompt_sha256": "1"}, "same": {"prompt_sha256": "1", "model": "m"},
                   "changed": {"prompt_sha256": "2", "model": "m2"}}
        applied = {"same": {"prompt_sha256": "1", "model": "m"},
                   "changed": {"prompt_sha256": "1", "model": "m"}}
        found = {item["feature"]: item["reasons"]
                 for item in generator._review_candidates(current, applied, True)}
        self.assertEqual(found["new"], ["No previously applied contextual description"])
        self.assertNotIn("same", found)
        self.assertEqual(found["changed"], ["feature prompt changed", "feature model changed"])

    def test_model_and_provider_changes_are_ignored_without_a_model(self):
        found = generator._review_candidates(
            {"f": {"model": "b"}}, {"f": {"model": "a"}}, False)
        self.assertEqual(found, [])


class Sections(unittest.TestCase):
    def test_overview_escapes_editor_notes(self):
        html = generator._overview_section("one <b>\n\ntwo", None)
        self.assertIn("<p>one &lt;b&gt;</p><p>two</p>", html)
        self.assertEqual(generator._overview_section("", None), "")

    def test_provenance_links_and_skips(self):
        app = {"configuration": {"provenanceSpec": {
            "doi": "10.1/x y", "url": "https://example.org/a", "bad": "http://[::1",
            "template": "https://x/{a}", "empty": ""}, "writing": "grc"}}
        html = generator._provenance_section(app)
        self.assertIn('href="https://doi.org/10.1/x%20y"', html)
        self.assertIn('href="https://example.org/a"', html)
        self.assertIn("http://[::1", html)
        self.assertNotIn('href="http://[::1', html)
        self.assertNotIn("{a}", html)
        self.assertIn("Writing", html)
        self.assertEqual(generator._provenance_section(None), "")

    def test_fallback_audit_lists_files_and_features(self):
        audit = {"word": {"provider": "P", "requested_model": "m", "responding_model": None,
                          "uncertainties": [], "evidence_requests": [], "additional_evidence": [],
                          "input_fingerprints": {"model": "m"}}}
        app = {"source_files": [{"path": "app/config.yaml", "sha256": "ab"}]}
        html = generator._fallback_audit_body(audit, app)
        for text in ("app/config.yaml", "Unavailable", "None recorded", "No additional evidence was requested."):
            self.assertIn(text, html)


if __name__ == "__main__":
    unittest.main()
