"""DSS context edits must be measured, repeatable, and scoped to its inventory."""
import json
from html import unescape
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from doc4cf.context import inventory_digest
from doc4cf import generator as g
from scripts.apply_dss_context_notes import (
    CL_DESCRIPTION, CL_SOURCE, LEXO_APP_SOURCE, LEXO_DESCRIPTION, LEXO_SOURCE,
    apply_notes, apply_site_notes, preserve_measurements,
)


class DSSContextNotes(unittest.TestCase):
    def prepare_sites(self, folder):
        baseline, output = folder / "baseline", folder / "output"
        for path in (baseline, output):
            (path / "features").mkdir(parents=True)
            (path / "markdown/features").mkdir(parents=True)
            (path / "context_review.json").write_text(json.dumps({"inventory_sha256": "same"}))
        facts = '<details><summary>Source metadata</summary><p>Measured source facts</p></details>'
        association = '<section class="correlated-features"><h2>Correlated features</h2><p>Measured relation</p></section>'
        model = '<section class="inferred-description"><h2>Description</h2><p>New model prose</p></section>'
        limit = '<aside class="association-limits"><p>Limited comparison</p></aside>'
        g.write_page(baseline, "features/cl.html", "cl.tf", association + facts, "Dead Sea Scrolls")
        g.write_page(output, "features/cl.html", "cl.tf", model + limit + facts, "Dead Sea Scrolls")
        (baseline / "markdown/features/cl.md").write_text(
            '# cl.tf\n\nSource facts\n\n## Applies to\n\nword\n\n## Correlated features\n\nMeasured relation\n')
        (output / "markdown/features/cl.md").write_text(
            '# cl.tf\n\n## Generated description\n\nNew model prose\n\n*AI-assisted credit*\n\n## Applies to\n\nword\n')
        return baseline, output

    def prepare(self, folder):
        inventory = {"dataset": {"acronym": "dss"}, "features": {
            "occ": {"kind": "edge", "sources": {"lex": 2}, "targets": {"word": 4}, "distinct_values": 0},
            "g_cons": {"metadata": {"dateWritten": "2026-11-04T12:00:08+00:00Z"}},
            "g_lex_etcbc": {"metadata": {"dateWritten": "2026-11-04T12:00:08+00:00Z"}},
        }}
        dataset = {"inventory_sha256": inventory_digest(inventory), "dataset_profile": "DSS profile",
                   "conventions": [], "needs_review": True, "ambiguities": [
                       "Feature occ reports distinct_values 0 so its presence is unclear.",
                       "Some dss-additions feature metadata carry createdDate/dateWritten in 2026, possibly future.",
                       "An unrelated unresolved question.",
                   ]}
        for name, value in (("inventory", inventory), ("dataset_context", dataset)):
            (folder / f"{name}.json").write_text(json.dumps(value), encoding="utf-8")
        return inventory

    def test_edits_are_idempotent_and_preserve_other_uncertainties(self):
        with TemporaryDirectory() as temporary:
            folder = Path(temporary)
            self.prepare(folder)
            apply_notes(folder)
            path = folder / "dataset_context.json"
            dataset = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(dataset["ambiguities"], ["An unrelated unresolved question."])
            self.assertEqual(len(dataset["conventions"]), 2)
            self.assertTrue(dataset["needs_review"])
            before = path.read_bytes()
            apply_notes(folder)
            self.assertEqual(path.read_bytes(), before)

    def test_stale_inventory_is_rejected_before_any_edit(self):
        with TemporaryDirectory() as temporary:
            folder = Path(temporary)
            inventory = self.prepare(folder)
            inventory["features"]["occ"]["sources"]["lex"] = 3
            (folder / "inventory.json").write_text(json.dumps(inventory), encoding="utf-8")
            path = folder / "dataset_context.json"
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, "does not match"):
                apply_notes(folder)
            self.assertEqual(path.read_bytes(), before)

    def test_feature_provenance_edit_keeps_metadata_and_model_credit(self):
        with TemporaryDirectory() as temporary:
            output = Path(temporary)
            (output / "features").mkdir()
            corpus = "Dead Sea Scrolls"
            g.write_page(output, "index.html", "Corpus", "", corpus)
            badge = g.ai_indicator("OpenRouter", "requested", "actual-model", "Interpretation")
            g.write_page(output, "features/cl.html", "cl.tf",
                         f'<section class="inferred-description"><h2>Description {badge}</h2>'
                         '<p>Mixed family provenance.</p></section>'
                         '<details><summary>Source metadata</summary><p>Original feature source</p></details>', corpus)
            g.write_page(output, "audit.html", "Audit report", "", corpus)
            g.write_markdown_feature(
                output / "markdown", "cl", "node", "UTF-8", "str", "Original feature source",
                "Mixed family provenance.", {"word": 2}, {"word": 1.0}, [("cmn", 2)],
                2, [], {}, {"provider": "OpenRouter", "model": "actual-model"},
                {"source": "Original feature source"})
            apply_site_notes(output)
            for name in ("features/cl.html", "markdown/features/cl.md"):
                text = (output / name).read_text(encoding="utf-8")
                self.assertIn(CL_DESCRIPTION, unescape(text))
                self.assertIn(CL_SOURCE, text)
                self.assertIn("Reviewed description", text)
                self.assertIn("actual-model", text.replace(r"\-", "-"))
                self.assertIn("Original feature source", text)
                self.assertNotIn("Mixed family provenance", text)
            before = {p: p.read_bytes() for p in output.rglob("*") if p.is_file()}
            apply_site_notes(output)
            self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_matching_measurements_are_retained_alongside_new_prose(self):
        with TemporaryDirectory() as temporary:
            baseline, output = self.prepare_sites(Path(temporary))
            self.assertTrue(preserve_measurements(baseline, output))
            for filename in ("features/cl.html", "markdown/features/cl.md"):
                text = (output / filename).read_text(encoding="utf-8")
                self.assertIn("Measured relation", text)
                self.assertIn("New model prose", text)
                self.assertNotIn("Limited comparison", text)
            before = {p: p.read_bytes() for p in output.rglob("*") if p.is_file()}
            self.assertTrue(preserve_measurements(baseline, output))
            self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_lexo_note_names_the_lexical_format_and_retains_model_credit(self):
        with TemporaryDirectory() as temporary:
            output = Path(temporary)
            (output / "features").mkdir()
            g.write_page(output, "index.html", "Corpus", "", "Dead Sea Scrolls")
            badge = g.ai_indicator("OpenRouter", "requested", "actual-model", "Interpretation")
            g.write_page(output, "features/lexo.html", "lexo.tf",
                         f'<section class="inferred-description"><h2>Description {badge}</h2>'
                         '<p>Default word text format.</p></section>'
                         '<details><summary>Source metadata</summary><p>Original source facts</p></details>',
                         "Dead Sea Scrolls")
            g.write_page(output, "audit.html", "Audit report", "", "Dead Sea Scrolls")
            g.write_markdown_feature(
                output / "markdown", "lexo", "node", "UTF-8", "str", "Original source facts",
                "Default word text format.", {"word": 2}, {"word": 1.0}, [("w", 2)],
                1, [], {}, {"provider": "OpenRouter", "model": "actual-model"},
                {"source": "Original source facts"})
            apply_site_notes(output)
            for filename in ("features/lexo.html", "markdown/features/lexo.md"):
                text = (output / filename).read_text(encoding="utf-8")
                self.assertIn(LEXO_DESCRIPTION, unescape(text))
                self.assertIn(LEXO_SOURCE, text)
                self.assertIn(LEXO_APP_SOURCE, text)
                self.assertIn("Reviewed description", text)
                self.assertIn("actual-model", text.replace(r"\-", "-"))
                self.assertIn("Original source facts", text)
                self.assertNotIn("Default word text format.", text)

    def test_changed_inventory_or_measured_facts_prevent_carry_forward(self):
        for change in ("inventory", "facts"):
            with self.subTest(change=change), TemporaryDirectory() as temporary:
                baseline, output = self.prepare_sites(Path(temporary))
                if change == "inventory":
                    (baseline / "context_review.json").write_text(json.dumps({"inventory_sha256": "old"}))
                else:
                    page = output / "features/cl.html"
                    page.write_text(page.read_text(encoding="utf-8").replace("Measured source facts", "Changed source facts"), encoding="utf-8")
                before = {p: p.read_bytes() for p in output.rglob("*") if p.is_file()}
                self.assertFalse(preserve_measurements(baseline, output))
                self.assertEqual(before, {p: p.read_bytes() for p in before})


if __name__ == "__main__":
    unittest.main()
