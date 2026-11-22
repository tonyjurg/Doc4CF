"""Regression checks for model text."""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock
from doc4cf import context, generator
from doc4cf.context import validate_feature_response


class ModelTextLimits(unittest.TestCase):
    def test_fresh_and_cached_descriptions_use_the_same_text_checks(self):
        reply = {"model": "actual\u202emodel", "choices": [{"message": {"content": " a\u202eb\x00 "}}]}
        with TemporaryDirectory() as tmp, mock.patch.object(generator, "build_provider_request"), \
                mock.patch.object(generator, "request_with_completion_retry", return_value=reply) as request:
            cache = Path(tmp)
            first = generator.description_record({}, "m", cache, "openrouter")
            self.assertEqual(first, {"text": "ab", "model": "actualmodel"})
            entry = next(cache.glob("*.json"))
            for text, expected in (("c\u2066d", "cd"), ("שלום", "שלום")):
                entry.write_text(json.dumps({"text": text, "model": "model\u202e"}), encoding="utf-8")
                cached = generator.description_record({}, "m", cache, "openrouter")
                self.assertEqual(cached, {"text": expected, "model": "model"})
            for text in ("x" * 4001, "\u202e\x00"):
                entry.write_text(json.dumps({"text": text, "model": "m"}), encoding="utf-8")
                with self.assertRaises(ValueError):
                    generator.description_record({}, "m", cache, "openrouter")
            entry.unlink()
            legacy = entry.with_suffix(".txt")
            legacy.write_text("a\u202eb", encoding="utf-8")
            self.assertEqual(generator.description_record({}, "m", cache, "openrouter")["text"], "ab")
            legacy.write_text("x" * 4001, encoding="utf-8")
            with self.assertRaises(ValueError):
                generator.description_record({}, "m", cache, "openrouter")
            request.assert_called_once()

    def test_invalid_fresh_descriptions_are_not_cached(self):
        for content in ("x" * 4001, "\u202e\x00"):
            reply = {"choices": [{"message": {"content": content}}]}
            with TemporaryDirectory() as tmp, mock.patch.object(generator, "build_provider_request"), \
                    mock.patch.object(generator, "request_with_completion_retry", return_value=reply):
                with self.assertRaises(ValueError):
                    generator.description_record({}, "m", Path(tmp), "openrouter")
                self.assertEqual(list(Path(tmp).glob("*.json")), [])

    def test_cached_context_is_revalidated_without_model_requests(self):
        valid = self.response()
        reply = {"choices": [{"message": {"content": json.dumps(valid)}}]}
        def validator(data):
            validate_feature_response(data, {"a"}, {})
        with TemporaryDirectory() as tmp, mock.patch.object(context, "build_provider_request"), \
                mock.patch.object(context, "request_with_completion_retry", return_value=reply) as request:
            cache = Path(tmp)
            context._analysis_record("system", {}, "openrouter", "m", cache, "feature-descriptions", validator)
            entry = next(cache.rglob("*.json"))
            cached = json.loads(entry.read_text(encoding="utf-8"))
            cached["data"]["description"] = "unsafe\u202e"
            entry.write_text(json.dumps(cached), encoding="utf-8")
            with self.assertRaises(ValueError):
                context._analysis_record("system", {}, "openrouter", "m", cache, "feature-descriptions", validator)
            request.assert_called_once()

    def response(self, **changes):
        data = {"description": "A feature.", "feature_references": [], "value_references": [],
                "uncertainties": ["x"], "context_flags": []}
        data.update(changes)
        return data

    def test_clean_model_text_strips_overrides_and_rejects_runaway_text(self):
        self.assertEqual(generator.clean_model_text(" a\u202eb\u2066c\x00 "), "abc")
        self.assertEqual(generator.clean_model_text("שלום"), "שלום")
        with self.assertRaises(ValueError):
            generator.clean_model_text("x" * (generator.MAX_DESCRIPTION_CHARS + 1))

    def test_context_validators_reject_long_or_unsafe_strings(self):
        validate_feature_response(self.response(), {"a"}, {})
        for bad in (self.response(description="x" * 5000),
                    self.response(description="x\u202ey"),
                    self.response(uncertainties=["u"] * 101),
                    self.response(uncertainties=["u\u2067"])):
            with self.subTest(), self.assertRaises(ValueError):
                validate_feature_response(bad, {"a"}, {})


if __name__ == "__main__":
    unittest.main()
