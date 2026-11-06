"""Integration check for a generated Nestle 1904 v1.0.0 site."""
from html.parser import HTMLParser
import io
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import tempfile
from unittest.mock import patch

from doc4cf import describe


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.urls.append(attrs[key])


def verify(source, site):
    features = {path.stem for path in source.glob("*.tf")}
    assert len(features) == 61
    assert {p.stem for p in (site / "features").glob("*.html")} == features
    pages = {}
    for path in site.rglob("*.html"):
        pages[path.resolve()] = parser = Links()
        parser.feed(path.read_text(encoding="utf-8"))
    for page, parser in pages.items():
        for url in parser.urls:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            target = (page.parent / unquote(parts.path)).resolve() if parts.path else page
            assert target.is_file(), (page, url)
            if parts.fragment and target in pages:
                assert unquote(parts.fragment) in pages[target].ids, (page, url)
    graph = json.loads((site / "knowledge_graph.json").read_text(encoding="utf-8"))
    assert len(graph["nodes"]) == 71
    for edge in graph["edges"]:
        assert edge["from"] in graph["nodes"] and edge["to"] in graph["nodes"]
    assert graph["nodes"]["feature::frame"]["valid_on"] == ["otype::word"]
    text = (site / "text.html").read_text(encoding="utf-8")
    assert "biblos genesis" in text and "βίβλος".casefold() in text.casefold().replace("ί", "ί")
    structure = (site / "structure.html").read_text(encoding="utf-8")
    assert structure.index('id="type-book"') < structure.index('id="type-sentence"') < structure.index('id="type-word"')
    with tempfile.TemporaryDirectory() as temp, patch.dict("os.environ", OPENROUTER_API_KEY="test"):
        response = io.BytesIO(b'{"choices":[{"message":{"content":"Generated example"}}]}')
        with patch("doc4cf.generator.urlopen", return_value=response) as send:
            for _ in range(2):
                assert describe({"name":"lemma"}, "test/model", Path(temp)) == "Generated example"
            send.assert_called_once()
    print(f"Verified {len(pages)} pages, {len(graph['edges'])} graph relations, transcription samples and OpenRouter caching.")


if __name__ == "__main__":
    verify(*map(Path, sys.argv[1:]))
