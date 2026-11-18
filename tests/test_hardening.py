"""Regression tests for redirect handling, option validation, and link encoding."""
import importlib.util
import subprocess
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import ProxyHandler, Request, build_opener

from doc4cf import context, generator

REPO = Path(__file__).resolve().parents[1]


class NoRedirects(unittest.TestCase):
    def test_credentials_are_not_forwarded_to_a_redirect_target(self):
        received = []

        class Target(BaseHTTPRequestHandler):
            def do_POST(self):
                received.append(dict(self.headers))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"{}")

            def log_message(self, *args):
                pass

        target = HTTPServer(("127.0.0.1", 0), Target)

        class Redirector(BaseHTTPRequestHandler):
            def do_POST(self):
                self.rfile.read(int(self.headers.get("Content-Length", 0)))
                self.send_response(302)
                self.send_header("Location", f"http://127.0.0.1:{target.server_port}/landing")
                self.end_headers()

            def log_message(self, *args):
                pass

        redirector = HTTPServer(("127.0.0.1", 0), Redirector)
        for server in (target, redirector):
            threading.Thread(target=server.serve_forever, daemon=True).start()
            self.addCleanup(server.server_close)
            self.addCleanup(server.shutdown)

        # Same handler the module installs, without any proxy from the environment.
        opener = build_opener(ProxyHandler({}), generator._NoRedirect)
        request = Request(f"http://127.0.0.1:{redirector.server_port}/v1", data=b"{}",
                          headers={"Authorization": "Bearer secret", "x-api-key": "secret"})
        with self.assertRaises(HTTPError) as caught:
            opener.open(request, timeout=5)
        self.assertEqual(caught.exception.code, 302)
        self.assertEqual(received, [])

    def test_module_opener_uses_the_no_redirect_handler(self):
        self.assertTrue(any(isinstance(h, generator._NoRedirect) for h in generator._OPENER.handlers))


class OptionValidation(unittest.TestCase):
    def test_empty_feature_file_is_a_value_error(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "broken.tf"
            path.write_bytes(b"")
            with self.assertRaisesRegex(ValueError, "broken.tf is empty"):
                generator.header(path)

    def test_project_home_rejects_script_schemes(self):
        for value in ("javascript:alert(1)", "JavaScript:alert(1)", "data:text/html,x", "file:///etc/passwd"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                generator.check_project_home(value)

    def test_project_home_accepts_relative_and_http_links(self):
        for value in (None, "", "../", "index.html", "/docs/", "https://example.org/project", "http://example.org"):
            with self.subTest(value=value):
                self.assertEqual(generator.check_project_home(value), value)

    def test_write_page_refuses_a_script_link(self):
        with TemporaryDirectory() as tmp, self.assertRaises(ValueError):
            generator.write_page(Path(tmp), "x.html", "T", "<p>b</p>", "C", project_home="javascript:alert(1)")
        with TemporaryDirectory() as tmp:
            generator.write_page(Path(tmp), "x.html", "T", "<p>b</p>", "C", project_home="https://example.org")
            self.assertIn('href="https://example.org"', (Path(tmp) / "x.html").read_text(encoding="utf-8"))


class ContextLinks(unittest.TestCase):
    def test_feature_links_are_percent_encoded(self):
        inventory = {"structure": {"node_types_in_corpus_order": [{"name": "w", "node_count": 3, "is_slot_type": True}]}}
        dataset = {"dataset_profile": "profile", "inventory_sha256": "h", "needs_review": False,
                   "conventions": [{"claim": "c", "status": "verified", "evidence": ["p"]}]}
        families = [{"label": "L", "purpose": "P", "status": "inferred", "features": ["a b#c"], "evidence": []}]
        review = {"affected_descriptions": [], "context_flags": [], "processed_descriptions": []}
        pages = context.context_pages(inventory, dataset, families, [], review)
        self.assertIn('href="features/a%20b%23c.html"', pages["dataset.html"])
        self.assertIn(">a b#c</a>", pages["dataset.html"])


class ReleaseSource(unittest.TestCase):
    @staticmethod
    def load_script():
        spec = importlib.util.spec_from_file_location("build_api_docs", REPO / "scripts" / "build_api_docs.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_tag_is_resolved_to_a_commit_and_not_confused_with_a_branch(self):
        script = self.load_script()

        def git(cwd, *args):
            subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], cwd=cwd, check=True,
                           capture_output=True)

        with TemporaryDirectory() as tmp:
            upstream, workspace = Path(tmp) / "upstream", Path(tmp) / "workspace"
            (upstream / "docs" / "api").mkdir(parents=True)
            workspace.mkdir()
            (upstream / "docs" / "api" / "conf.py").write_text("# tagged\n", encoding="utf-8")
            git(upstream, "init", "-q", "-b", "main")
            git(upstream, "add", "-A")
            git(upstream, "commit", "-q", "-m", "release")
            git(upstream, "tag", "v1")
            (upstream / "docs" / "api" / "conf.py").write_text("# later\n", encoding="utf-8")
            git(upstream, "commit", "-q", "-am", "later")
            git(upstream, "branch", "v2")  # a branch that shares no name with the tag below
            with patch.object(script, "ROOT", upstream):
                source = script.release_source("v1", workspace)
                self.assertEqual((source / "docs" / "api" / "conf.py").read_text(encoding="utf-8"), "# tagged\n")
                with self.assertRaises(subprocess.CalledProcessError):
                    script.release_source("v2", Path(tmp) / "other")  # a branch, not a tag


if __name__ == "__main__":
    unittest.main()
