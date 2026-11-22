"""Keep source-cited N1904 clarifications reproducible and distinct from model output."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from doc4cf import generator as g
from scripts.apply_n1904_editorial_notes import DESCRIPTION, SOURCE, apply_notes


class EditorialNotes(unittest.TestCase):
    def build(self, output, enriched, corpus="Greek New Testament (Nestle 1904)"):
        (output / "features").mkdir()
        g.write_page(output, "index.html", "Corpus", "<p>Corpus</p>", corpus)
        badge = g.ai_indicator("OpenRouter", "requested", "actual-model", "Generated interpretation")
        inferred = (f'<section class="inferred-description"><h2>Description {badge}</h2>'
                    '<p>May denote line numbers.</p></section>') if enriched else ""
        metadata = '<details><summary>Source metadata</summary>' + g.table(
            ["Field", "Value"], [("description", "ln")]) + '</details>'
        g.write_page(output, "features/ln.html", "ln.tf", "<p>ln</p>" + inferred + metadata, corpus)
        g.write_page(output, "features.html", "Features", g.table(
            ["Feature", "Kind", "Description"], [(g.feature("ln"), "node", "ln")]), corpus)
        g.write_page(output, "audit.html", "Audit report", "<p>Original uncertainty flags</p>", corpus)
        g.write_markdown_feature(output / "markdown", "ln", "node", "UTF-8", "str", "ln",
                                 "May denote line numbers.", {"word": 2}, {"word": 1.0}, [("92.24", 2)],
                                 2, [], {}, {"provider": "OpenRouter", "model": "actual-model"} if enriched else None,
                                 {"description": "ln"})
        g.write_markdown_index(output / "markdown", corpus, [("ln", "node", "ln", "word", [("92.24", 2)])])

    def test_clarification_handles_offline_and_enriched_sites_idempotently(self):
        for enriched in (False, True):
            with self.subTest(enriched=enriched), TemporaryDirectory() as temporary:
                output = Path(temporary)
                self.build(output, enriched)
                apply_notes(output)
                html = (output / "features/ln.html").read_text(encoding="utf-8")
                markdown = (output / "markdown/features/ln.md").read_text(encoding="utf-8")
                for text in (html, markdown):
                    self.assertIn(DESCRIPTION, text)
                    self.assertIn(SOURCE, text)
                    self.assertNotIn("line numbers", text)
                    self.assertIn("Reviewed description" if enriched else "Editorial description", text)
                self.assertIn("<td>description</td><td>ln</td>", html)
                if enriched:
                    self.assertIn("actual-model", html)
                    self.assertIn("AI-assisted", markdown)
                for name in ("index.md", "features.md"):
                    self.assertIn("Louw–Nida", (output / "markdown" / name).read_text(encoding="utf-8"))
                self.assertIn("Editorial clarifications", (output / "audit.html").read_text(encoding="utf-8"))
                before = {file: file.read_bytes() for file in output.rglob("*") if file.is_file()}
                apply_notes(output)
                self.assertEqual(before, {file: file.read_bytes() for file in before})

    def test_other_corpora_are_rejected(self):
        with TemporaryDirectory() as temporary:
            output = Path(temporary)
            self.build(output, False, corpus="Other corpus")
            with self.assertRaises(ValueError):
                apply_notes(output)


if __name__ == "__main__":
    unittest.main()
