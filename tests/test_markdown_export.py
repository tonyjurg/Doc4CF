"""Regression checks for markdown export."""
import re
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from doc4cf import generator


HOSTILE = ('<script>X</script> ![beacon](https://evil.example/p.png) [click](https://evil.example/a) '
           '<img src=x onerror=X> `code` *em* | pipe\nnewline')


class MarkdownExport(unittest.TestCase):
    def test_list_markers_are_literal_text(self):
        for value, expected in (("- item", r"\- item"), ("+ item", r"\+ item"),
                                ("1. item", r"1\. item"), ("> quote", "&gt; quote")):
            with self.subTest(value=value):
                self.assertEqual(generator.markdown_text(value), expected)

    def test_text_helpers_neutralise_markup(self):
        text = generator.markdown_text(HOSTILE)
        self.assertNotIn("<", text)
        self.assertNotIn("\n", text)
        for token in ("![", "](", "[click]"):
            self.assertNotRegex(text, r"(?<!\\)" + re.escape(token))

    def test_code_span_cannot_be_closed_early(self):
        for value in ("a`b", "``x", "`", "a``b`c", "a|b", r"a\|b"):
            span = generator.markdown_code(value)
            fence = re.match(r"`+", span).group(0)
            inner = span[len(fence):-len(fence)].replace("\\|", "|").strip()
            self.assertEqual(inner, value)
            runs = [len(run) for run in re.findall(r"`+", value)]
            self.assertTrue(all(run != len(fence) for run in runs))

    def test_common_values_are_escaped_by_the_index_writer(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            generator.write_markdown_index(out, "Corpus", [
                ("word", "node", "Words", "word", [('` ![beacon](https://evil.example) | <img>', 4)])])
            for name in ("index.md", "features.md"):
                text = (out / name).read_text(encoding="utf-8")
                self.assertIn('``"` ![beacon](https://evil.example) \\| <img>"`` (4)', text)
                self.assertEqual(text.count("\\|"), 1)

    def test_written_pages_contain_no_active_markup(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            name = 'evil"](https://evil.example)<b>'
            generator.write_markdown_feature(
                out, name, "node", "UTF-8", "str", HOSTILE, HOSTILE, {name: 3}, {name: 1.0},
                [(HOSTILE, 3)], 3, [], {}, {"provider": HOSTILE, "model": HOSTILE}, {"description": HOSTILE})
            generator.write_markdown_index(out, HOSTILE, [(name, "node", HOSTILE, HOSTILE, [(HOSTILE, 3)])])
            for path in list(out.rglob("*.md")):
                # Text inside inline code spans is displayed literally by Markdown renderers.
                text = re.sub(r"(`+).+?\1", "", path.read_text(encoding="utf-8"))
                self.assertNotIn("<script", text, path.name)
                self.assertNotIn("<img", text, path.name)
                self.assertNotIn("![", text, path.name)
                self.assertNotIn("](https://evil", text, path.name)
                # Only our own tags and links may remain.
                for tag in re.findall(r"<[^>]+>", text):
                    self.assertIn(tag, ("<details>", "</details>", "<summary>", "</summary>"), path.name)


if __name__ == "__main__":
    unittest.main()
