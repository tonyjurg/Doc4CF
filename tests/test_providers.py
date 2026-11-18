"""Provider selection and model-credit behavior using simulated API responses."""
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from doc4cf.generator import describe, main


class ProviderOptions(unittest.TestCase):
    def test_free_router_budget_and_incomplete_response_not_cached(self):
        with TemporaryDirectory() as tmp, patch.dict("os.environ", OPENROUTER_API_KEY="test"):
            cache = Path(tmp)
            incomplete = {"choices": [{"finish_reason": "length", "message": {"content": "Cut off"}}]}
            with patch("doc4cf.generator.urlopen",
                       side_effect=lambda *a, **k: io.BytesIO(json.dumps(incomplete).encode())) as send:
                with self.assertRaisesRegex(ValueError, "incomplete"):
                    describe({}, "openrouter/free", cache)
                first = json.loads(send.call_args_list[0].args[0].data)
                self.assertEqual(first["max_tokens"], 8192)
                self.assertEqual(first["reasoning"], {"effort": "low", "exclude": True})
                self.assertEqual(send.call_count, 3)  # initial request + two truncation retries
            self.assertEqual(list(cache.iterdir()), [])
            complete = {"choices": [{"finish_reason": "stop", "message": {"content": "Complete paragraph."}}]}
            with patch("doc4cf.generator.urlopen", return_value=io.BytesIO(json.dumps(complete).encode())):
                self.assertEqual(describe({}, "openrouter/free", cache), "Complete paragraph.")
            self.assertEqual(len(list(cache.glob("*.json"))), 1)

    def test_routing_and_provider_specific_cache(self):
        providers = (
            ("openrouter", "OPENROUTER_API_KEY", "openrouter.ai"),
            ("openai", "OPENAI_API_KEY", "api.openai.com"),
            ("groq", "GROQ_API_KEY", "api.groq.com"),
            ("gemini", "GEMINI_API_KEY", "generativelanguage.googleapis.com"),
        )
        with TemporaryDirectory() as tmp:
            for provider, variable, host in providers:
                with self.subTest(provider=provider), patch.dict("os.environ", {variable: provider}, clear=True):
                    reply = {"choices": [{"message": {"content": provider}}]}
                    response = io.BytesIO(json.dumps(reply).encode())
                    with patch("doc4cf.generator.urlopen", return_value=response) as send:
                        for _ in range(2):
                            self.assertEqual(describe({}, "same-model", Path(tmp), provider), provider)
                        send.assert_called_once()
                        req = send.call_args.args[0]
                        self.assertEqual(req.host, host)
                        self.assertEqual(req.get_header("Authorization"), "Bearer " + provider)

    def test_cli_model_credit(self):
        with TemporaryDirectory() as tmp:
            source = Path(tmp) / "input"
            out = Path(tmp) / "out"
            source.mkdir()
            (source / "otype.tf").write_text("@node\n@valueType=str\n\n1-2\tword\n3\tline\n")
            (source / "oslots.tf").write_text("@edge\n\n3\t1-2\n")
            for mode in ("feature", "overview", "none"):
                argv = ["doc4cf", str(source), str(out), "--provider", "groq", "--model", "test-model",
                        "--model-attribution", mode]
                with self.subTest(mode=mode), patch("sys.argv", argv), patch("doc4cf.generator.description_record", return_value={"text":"Example prose.", "model":"actual-model"}) as generate:
                    main()
                    self.assertEqual(generate.call_args.args[-1], "groq")
                    feature = (out / "features/otype.html").read_text(encoding="utf-8")
                    overview = (out / "index.html").read_text(encoding="utf-8")
                    self.assertIn("Generated description", feature)
                    self.assertIn("Example prose.", feature)
                    self.assertEqual("Groq · actual-model" in feature, mode == "feature")
                    self.assertEqual("Groq · actual-model" in overview, mode == "overview")
                    if mode == "none":
                        for page in out.rglob("*.html"):
                            self.assertNotIn("actual-model", page.read_text(encoding="utf-8"))

    def test_editorial_review_then_full_build(self):
        with TemporaryDirectory() as tmp, patch.dict("os.environ", OPENROUTER_API_KEY="test"):
            root = Path(tmp)
            source = root / "corpus"
            source.mkdir()
            (source / "otype.tf").write_text("@node\n@valueType=str\n\n1-2\tword\n3\tline\n")
            (source / "oslots.tf").write_text("@edge\n\n3\t1-2\n")
            notes = root / "notes.md"
            notes.write_text("Terminology: λόγος", encoding="utf-8-sig")
            out = root / "out"
            command = ["doc4cf", str(source), str(out), "--model", "openrouter/free",
                       "--cache", str(root / "cache"), "--model-attribution", "overview"]
            def run(*extra):
                with patch("sys.argv", command + ["--dataset-context", str(notes), *extra]):
                    main()

            evidence = []
            def respond(req, timeout):
                profile = json.loads(json.loads(req.data)["messages"][1]["content"])
                evidence.append(profile)
                reply = {"model": "model-" + profile["name"], "choices": [{"message": {"content": "Prose."}}]}
                return io.BytesIO(json.dumps(reply).encode())

            with patch("doc4cf.generator.urlopen", side_effect=respond):
                with self.assertRaises(SystemExit):
                    run("--describe-features", "missing")
                self.assertFalse(out.exists())
                run("--describe-features", "otype")
                self.assertEqual([p["name"] for p in evidence], ["otype"])
                self.assertEqual(evidence[0]["corpus_editor_notes"], "Terminology: λόγος")
                self.assertNotIn("Generated description", (out / "features/oslots.html").read_text(encoding="utf-8"))
                notes = notes.rename(root / "renamed.md")
                run()
                self.assertEqual([p["name"] for p in evidence], ["otype", "oslots"])
                overview = (out / "index.html").read_text(encoding="utf-8")
                self.assertIn("model-otype", overview)
                self.assertIn("model-oslots", overview)
                notes.write_text("Revised notes.", encoding="utf-8")
                run("--describe-features", "otype")
                self.assertEqual(len(evidence), 3)
                self.assertEqual(evidence[-1]["corpus_editor_notes"], "Revised notes.")

    def test_native_claude_messages_and_cache(self):
        from doc4cf.generator import description_record
        with TemporaryDirectory() as tmp, patch.dict("os.environ", {"ANTHROPIC_API_KEY": "test"}, clear=True):
            response = {"model": "claude-response", "content": [
                {"type": "thinking", "thinking": "private"}, {"type": "text", "text": "Description."}],
                "stop_reason": "end_turn"}
            with patch("doc4cf.generator.urlopen", return_value=io.BytesIO(json.dumps(response).encode())) as send:
                for _ in range(2):
                    record = description_record({"corpus_editor_notes": "A note"}, "claude-request", Path(tmp), "anthropic")
                    self.assertEqual(record, {"text": "Description.", "model": "claude-response"})
                send.assert_called_once()
                req = send.call_args.args[0]
                self.assertEqual(req.full_url, "https://api.anthropic.com/v1/messages")
                self.assertEqual(req.get_header("X-api-key"), "test")
                self.assertEqual(req.get_header("Anthropic-version"), "2023-06-01")
                self.assertIsNone(req.get_header("Authorization"))
                body = json.loads(req.data)
                self.assertIn("system", body)
                self.assertEqual([m["role"] for m in body["messages"]], ["user"])
                self.assertIn("A note", body["messages"][0]["content"])
