"""Regression checks for corpora with unfamiliar names and no text configuration."""
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest

from doc4cf import generate


class CorpusWithoutConfig(unittest.TestCase):
    def test_arbitrary_slot_and_text_field(self):
        with TemporaryDirectory() as root:
            source = Path(root) / "input"
            site = Path(root) / "site"
            source.mkdir()
            (source / "otype.tf").write_text(
                "@node\n@valueType=str\n@name=Inscribed objects\n\n1-3\tbead\n4\tstrand\n", encoding="utf-8")
            (source / "oslots.tf").write_text("@edge\n\n4\t1-3\n", encoding="utf-8")
            (source / "etching.tf").write_text("@node\n@valueType=str\n\na\nb\nc\n", encoding="utf-8")
            (source / "text.tf").write_text("@node\n@valueType=str\n\na\nb\nc\n", encoding="utf-8")
            generate(SimpleNamespace(corpus=source, output=site, model=None, project_home="../../index.html"))
            self.assertTrue((site / "doc4cf-logo.svg").is_file())
            for page in site.rglob("*.html"):
                prefix = "../" if page.parent.name == "features" else ""
                self.assertIn(f'<header><a class="header-logo" href="{prefix}index.html"', page.read_text(encoding="utf-8"))
            self.assertTrue((site / "features/etching.html").is_file())
            text_feature = (site / "features/text.html").read_text(encoding="utf-8")
            self.assertIn("<h1>text.tf</h1>", text_feature)
            self.assertIn('href="../../../index.html"', text_feature)
            structure = (site / "structure.html").read_text(encoding="utf-8")
            self.assertIn('class="structure-choices"', structure)
            self.assertGreater(structure.index('class="graph-download"'), structure.index('id="type-bead"'))
            self.assertIn("Inscribed objects", (site / "index.html").read_text(encoding="utf-8"))
            text = (site / "text.html").read_text(encoding="utf-8")
            self.assertIn("features/etching.html", text)
            self.assertIn("a · b · c", text)
            self.assertFalse((source / "otext.tf").exists())
            self.assertFalse((site / "features/otext.html").exists())


if __name__ == "__main__":
    unittest.main()
