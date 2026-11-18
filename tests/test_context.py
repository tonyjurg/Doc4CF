"""Table-driven validation and offline context-pipeline regression tests."""
from copy import deepcopy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from doc4cf import context


DATASET = {
    "dataset_profile": "A corpus profile.",
    "conventions": [{"claim": "Values are recorded", "status": "verified", "evidence": ["features/word"]}],
    "ambiguities": ["Some meanings are unspecified."],
    "needs_review": False,
}
FAMILY = {
    "id": "lexical_core", "label": "Lexical", "purpose": "Lexical information",
    "features": ["word"], "status": "inferred", "evidence": ["features/word"],
    "needs_review": False,
}
RELATIONSHIP = {
    "source_feature": "word", "target_feature": "lemma", "relationship": "has lemma",
    "status": "verified", "evidence": ["features/word"], "needs_review": False,
}
FEATURE_RESPONSE = {
    "description": "The word feature stores tokens.", "feature_references": ["lemma"],
    "value_references": [{"feature": "word", "value": "logos"}],
    "uncertainties": [], "context_flags": [{
        "issue": "Editorial scope is unclear.", "status": "missing_evidence", "evidence": ["notes/scope"],
    }],
}
PROVENANCE = {
    "provider": "openai", "requested_model": "model-a", "responding_model": "model-b",
    "prompt_version": "context-analysis-1",
}


def invalid_cases(valid, mutations):
    """Yield labeled invalid copies for concise table-driven assertions."""
    for case in mutations:
        label, mutate = case[:2]
        error_type = case[2] if len(case) == 3 else ValueError
        value = deepcopy(valid)
        mutate(value)
        yield label, value, error_type


class PrimitiveValidators(unittest.TestCase):
    def test_keys_cases(self):
        cases = [("complete", {"a": 1, "b": 2}, None),
                 ("optional", {"a": 1, "b": 2, "c": 3}, None),
                 ("missing", {"a": 1}, ValueError),
                 ("unexpected", {"a": 1, "b": 2, "x": 4}, ValueError),
                 ("non-object", [], TypeError)]
        for label, value, error_type in cases:
            with self.subTest(label=label):
                if error_type is None:
                    context._keys(value, ("a", "b"), ("c",))
                else:
                    with self.assertRaises(error_type):
                        context._keys(value, ("a", "b"), ("c",))

    def test_string_string_list_and_status_cases(self):
        cases = [
            ("non-empty string", context._string, ("text", "claim"), None),
            ("blank string", context._string, ("  ", "claim"), ValueError),
            ("wrong string type", context._string, (4, "claim"), TypeError),
            ("empty string list", context._string_list, ([], "evidence"), None),
            ("string list", context._string_list, (["path/a", "path/b"], "evidence"), None),
            ("wrong string-list type", context._string_list, ("path/a", "evidence"), TypeError),
            ("blank list item", context._string_list, (["path/a", " "], "evidence"), ValueError),
            ("non-string list item", context._string_list, ([3], "evidence"), TypeError),
            ("verified status", context._status, ("verified",), None),
            ("invalid status", context._status, ("approved",), ValueError),
            ("non-string status", context._status, (None,), TypeError),
        ]
        for label, validator, args, accepted in cases:
            with self.subTest(label=label):
                if accepted is None:
                    validator(*args)
                else:
                    with self.assertRaises(accepted):
                        validator(*args)


class ArtifactValidators(unittest.TestCase):
    def test_dataset_context_table(self):
        invalid = [
            ("missing profile", lambda value: value.pop("dataset_profile")),
            ("blank profile", lambda value: value.__setitem__("dataset_profile", " ")),
            ("bad ambiguity list", lambda value: value.__setitem__("ambiguities", [None]), TypeError),
            ("review must be boolean", lambda value: value.__setitem__("needs_review", 1), TypeError),
            ("conventions must be an array", lambda value: value.__setitem__("conventions", {}), TypeError),
            ("bad convention status", lambda value: value["conventions"][0].__setitem__("status", "approved")),
            ("extra convention key", lambda value: value["conventions"][0].__setitem__("extra", True)),
        ]
        context.validate_dataset_context(DATASET)
        for label, value, error_type in invalid_cases(DATASET, invalid):
            with self.subTest(label=label), self.assertRaises(error_type):
                context.validate_dataset_context(value)

    def test_family_and_relationship_context_table(self):
        valid = {"families": [FAMILY], "relationships": [RELATIONSHIP]}
        context.validate_family_context(valid, {"word", "lemma"})
        context.validate_family_context({"families": [], "relationships": []}, {"word"})
        invalid = [
            ("bad family id", lambda value: value["families"][0].__setitem__("id", "Bad-ID")),
            ("unknown family feature", lambda value: value["families"][0].__setitem__("features", ["ghost"])),
            ("bad family review flag", lambda value: value["families"][0].__setitem__("needs_review", "no"), TypeError),
            ("bad family evidence", lambda value: value["families"][0].__setitem__("evidence", [""])),
            ("bad relationship status", lambda value: value["relationships"][0].__setitem__("status", "unknown")),
            ("unknown relationship endpoint", lambda value: value["relationships"][0].__setitem__("target_feature", "ghost")),
            ("relationship not an array", lambda value: value.__setitem__("relationships", None), TypeError),
        ]
        for label, value, error_type in invalid_cases(valid, invalid):
            with self.subTest(label=label), self.assertRaises(error_type):
                context.validate_family_context(value, {"word", "lemma"})

    def test_analysis_provenance_table(self):
        invalid = [
            ("unsupported provider", lambda value: value.__setitem__("provider", "unknown")),
            ("provider must be a string", lambda value: value.__setitem__("provider", []), TypeError),
            ("empty model", lambda value: value.__setitem__("requested_model", "")),
            ("empty responding model", lambda value: value.__setitem__("responding_model", " ")),
            ("missing prompt", lambda value: value.pop("prompt_version")),
        ]
        context.validate_analysis_provenance(PROVENANCE)
        value = deepcopy(PROVENANCE)
        value["responding_model"] = None
        context.validate_analysis_provenance(value)
        for label, value, error_type in invalid_cases(PROVENANCE, invalid):
            with self.subTest(label=label), self.assertRaises(error_type):
                context.validate_analysis_provenance(value)

    def test_feature_response_table(self):
        feature_names = {"word", "lemma"}
        values = {"word": {"logos"}, "lemma": {"logos"}}
        context.validate_feature_response(FEATURE_RESPONSE, feature_names, values)
        invalid = [
            ("unknown feature reference", lambda value: value.__setitem__("feature_references", ["ghost"])),
            ("unattested value", lambda value: value["value_references"][0].__setitem__("value", "unknown")),
            ("value has wrong type", lambda value: value["value_references"][0].__setitem__("value", []), TypeError),
            ("unknown value feature", lambda value: value["value_references"][0].__setitem__("feature", "ghost")),
            ("bad context flag", lambda value: value["context_flags"][0].__setitem__("status", "maybe")),
            ("bad uncertainty list", lambda value: value.__setitem__("uncertainties", [""])),
            ("extra value reference key", lambda value: value["value_references"][0].__setitem__("source", "guess")),
            ("context flags must be array", lambda value: value.__setitem__("context_flags", {}), TypeError),
        ]
        for label, value, error_type in invalid_cases(FEATURE_RESPONSE, invalid):
            with self.subTest(label=label), self.assertRaises(error_type):
                context.validate_feature_response(value, feature_names, values)

    def test_evidence_plan_table(self):
        valid = {"requests": [{"kind": "rare_values", "rationale": "Show rare forms", "count": 3}]}
        context._validate_evidence_plan(valid)
        invalid = [
            ("too many requests", lambda value: value.__setitem__("requests", [
                {"kind": "rare_values", "rationale": "a", "count": 1},
                {"kind": "representative_examples", "rationale": "b", "count": 1},
                {"kind": "other", "rationale": "c", "count": 1},
            ])),
            ("duplicate kind", lambda value: value["requests"].append(deepcopy(value["requests"][0]))),
            ("unsupported kind", lambda value: value["requests"][0].__setitem__("kind", "other")),
            ("kind must be a string", lambda value: value["requests"][0].__setitem__("kind", None), TypeError),
            ("blank rationale", lambda value: value["requests"][0].__setitem__("rationale", " ")),
            ("boolean count", lambda value: value["requests"][0].__setitem__("count", True)),
            ("count must be an integer", lambda value: value["requests"][0].__setitem__("count", "2"), TypeError),
            ("out of range count", lambda value: value["requests"][0].__setitem__("count", 6)),
            ("requests must be an array", lambda value: value.__setitem__("requests", None), TypeError),
        ]
        for label, value, error_type in invalid_cases(valid, invalid):
            with self.subTest(label=label), self.assertRaises(error_type):
                context._validate_evidence_plan(value)


class ContextPipeline(unittest.TestCase):
    def setUp(self):
        self.inventory = {
            "features": {"word": {"kind": "node", "values": ["logos"]}, "lemma": {"kind": "node"}},
            "structure": {"node_types_in_corpus_order": [{"name": "word", "node_count": 4, "is_slot_type": True}]},
        }

    def write_artifacts(self, folder, inventory_hash):
        records = {
            "dataset_context.json": {
                "context_version": "1.0", "inventory_sha256": inventory_hash, **deepcopy(DATASET),
            },
            "feature_families.json": {
                "families_version": "1.0", "inventory_sha256": inventory_hash, "families": [FAMILY],
            },
            "feature_relationships.json": {
                "relationships_version": "1.0", "inventory_sha256": inventory_hash,
                "relationships": [RELATIONSHIP],
            },
        }
        for filename, value in records.items():
            (folder / filename).write_text(json.dumps(value), encoding="utf-8")

    def test_load_context_artifacts_validates_files_and_hashes(self):
        with TemporaryDirectory() as directory:
            folder = Path(directory)
            digest = context.inventory_digest(self.inventory)
            self.write_artifacts(folder, digest)
            dataset, families, relationships, analysis = context.load_context_artifacts(folder, self.inventory)
            self.assertEqual(dataset["dataset_profile"], DATASET["dataset_profile"])
            self.assertEqual(families, [FAMILY])
            self.assertEqual(relationships, [RELATIONSHIP])
            self.assertIsNone(analysis)
            self.write_artifacts(folder, "stale")
            with self.assertRaisesRegex(ValueError, "hash does not match"):
                context.load_context_artifacts(folder, self.inventory)

    def test_inventory_digest_is_canonical(self):
        self.assertEqual(context.inventory_digest({"b": 2, "a": 1}), context.inventory_digest({"a": 1, "b": 2}))

    def test_context_pages_escape_content_and_return_all_pages(self):
        dataset = {**deepcopy(DATASET), "inventory_sha256": "<hash>"}
        dataset["dataset_profile"] = "<script>alert(1)</script>"
        review = {"affected_descriptions": [], "processed_descriptions": [], "context_flags": []}
        pages = context.context_pages(self.inventory, dataset, [FAMILY], [RELATIONSHIP], review)
        self.assertEqual(set(pages), {"dataset.html", "relationships.html", "context-review.html"})
        self.assertIn("&lt;script&gt;", pages["dataset.html"])
        self.assertNotIn("<script>alert(1)</script>", pages["dataset.html"])

    def test_feature_context_hashes_change_with_evidence(self):
        dataset = {**deepcopy(DATASET), "inventory_sha256": "ignored"}
        base = context.feature_context_hashes(self.inventory, dataset, [FAMILY], [RELATIONSHIP], "openai", "m")
        changed_inventory = deepcopy(self.inventory)
        changed_inventory["features"]["word"]["values"].append("rhema")
        changed = context.feature_context_hashes(changed_inventory, dataset, [FAMILY], [RELATIONSHIP], "openai", "m")
        self.assertNotEqual(base["word"]["feature_evidence_sha256"], changed["word"]["feature_evidence_sha256"])
        self.assertEqual(base["lemma"]["evidence_mode"], "compact")

    def test_retrieve_requested_rare_values_from_loaded_api(self):
        api = SimpleNamespace(
            Fs=lambda _name: SimpleNamespace(items=lambda: [(1, "common"), (2, "common"), (3, "rare")]),
            F=SimpleNamespace(otype=SimpleNamespace(v=lambda _node: "word")),
            T=SimpleNamespace(text=lambda _nodes: "sample"),
        )
        result = context.retrieve_requested_evidence(
            api, "word", "rare_values", {"count": 1, "rationale": "Find uncommon values"}, "node",
        )
        self.assertEqual(result["items"], [{"value": "rare", "count": 1}])
        self.assertTrue(result["available"])

    def test_retrieve_requested_representative_examples_from_loaded_api(self):
        api = SimpleNamespace(
            Fs=lambda _name: SimpleNamespace(items=lambda: [(1, "common"), (2, "common"), (3, "rare")]),
            F=SimpleNamespace(otype=SimpleNamespace(v=lambda _node: "word")),
            T=SimpleNamespace(text=lambda _nodes: "sample passage"),
        )
        result = context.retrieve_requested_evidence(
            api, "word", "representative_examples", {"count": 1, "rationale": "Show a rare example"}, "node",
        )
        self.assertEqual(result["items"], [{
            "node": 3, "node_type": "word", "feature": "word", "value": "rare", "text": "sample passage",
        }])

    def test_contextual_description_compact_and_targeted_preconditions(self):
        record = {"data": {**deepcopy(FEATURE_RESPONSE)}, "model": "m"}
        with patch.object(context, "_analysis_record", return_value=record):
            result = context.contextual_description_record(
                {"name": "word"}, "m", Path("cache"), "openai", {"word", "lemma"}, {"word": {"logos"}},
            )
        self.assertEqual(result["text"], FEATURE_RESPONSE["description"])
        self.assertEqual(result["evidence_requests"], [])
        with self.assertRaisesRegex(TypeError, "needs the loaded corpus API"):
            context.contextual_description_record(
                {"name": "word"}, "m", Path("cache"), "openai", {"word"}, {}, targeted_evidence=True,
            )

    def test_contextual_description_targeted_flow_requests_and_uses_local_evidence(self):
        plan = {"data": {"requests": [{
            "kind": "representative_examples", "rationale": "Show a rare form", "count": 1,
        }]}}
        description = {"data": deepcopy(FEATURE_RESPONSE), "model": "m"}
        api = SimpleNamespace(
            Fs=lambda _name: SimpleNamespace(items=lambda: [(1, "logos")]),
            F=SimpleNamespace(otype=SimpleNamespace(v=lambda _node: "word")),
            T=SimpleNamespace(text=lambda _nodes: "logos in context"),
        )
        with patch.object(context, "_analysis_record", side_effect=[plan, description]) as analyze:
            result = context.contextual_description_record(
                {"name": "word"}, "m", Path("cache"), "openai", {"word", "lemma"},
                {"word": {"logos"}}, api=api, feature_kind="node", targeted_evidence=True,
            )
        self.assertEqual(analyze.call_count, 2)
        self.assertEqual(result["evidence_requests"], plan["data"]["requests"])
        self.assertEqual(result["additional_evidence"][0]["items"][0]["text"], "logos in context")

    def test_analyze_context_writes_validated_artifacts_without_loading_a_corpus(self):
        dataset_record = {"data": deepcopy(DATASET), "model": "dataset-model"}
        family_record = {"data": {"families": [FAMILY], "relationships": [RELATIONSHIP]}, "model": "family-model"}

        def export_stub(_corpus, output_path):
            output_path.write_text(json.dumps(self.inventory), encoding="utf-8")
            return deepcopy(self.inventory)

        with TemporaryDirectory() as directory, \
                patch.object(context, "export_inventory", side_effect=export_stub), \
                patch.object(context, "_analysis_record", side_effect=[dataset_record, family_record]):
            output = Path(directory)
            result = context.analyze_context(Path("unused-corpus"), output, "openai", "d", "f", output / "cache")
            self.assertEqual(result["dataset_model"], "dataset-model")
            self.assertTrue((output / "inventory.json").exists())
            self.assertEqual(json.loads((output / "dataset_context.json").read_text())[
                "context_version"], "1.0")
            self.assertEqual(json.loads((output / "feature_relationships.json").read_text())[
                "relationships"], [RELATIONSHIP])


class ContextProviderPaths(unittest.TestCase):
    @staticmethod
    def reply(value, model="provider-model"):
        return {"choices": [{"finish_reason": "stop", "message": {"content": json.dumps(value)}}],
                "model": model}

    def test_object_response_provider_and_error_table(self):
        cases = [
            ("openai", self.reply(DATASET), DATASET, "provider-model"),
            ("anthropic", {"content": [{"type": "text", "text": json.dumps(DATASET)}],
                           "model": "claude", "stop_reason": "end_turn"}, DATASET, "claude"),
        ]
        for provider, reply, expected, model in cases:
            with self.subTest(provider=provider):
                self.assertEqual(context._object_response(provider, reply), (expected, model))
        invalid_json = self.reply(DATASET)
        invalid_json["choices"][0]["message"]["content"] = "{"
        empty = self.reply(DATASET)
        empty["choices"][0]["message"]["content"] = " "
        invalid = [
            ("invalid JSON", "openai", invalid_json, "invalid JSON"),
            ("empty response", "openai", empty, "empty context analysis"),
            ("non-object JSON", "openai", self.reply([1]), "JSON object", TypeError),
            ("incomplete Anthropic", "anthropic", {"content": [], "stop_reason": "max_tokens"}, "incomplete"),
        ]
        for case in invalid:
            label, provider, reply, message = case[:4]
            error_type = case[4] if len(case) == 5 else ValueError
            with self.subTest(label=label), self.assertRaisesRegex(error_type, message):
                context._object_response(provider, reply)

    def test_analysis_record_cache_hit_avoids_a_second_request(self):
        with TemporaryDirectory() as directory, patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            with patch.object(context, "request_with_completion_retry", return_value=self.reply(DATASET)) as request:
                result = context._analysis_record(
                    "system", {"input": "evidence"}, "openai", "model", Path(directory),
                    "dataset", context.validate_dataset_context,
                )
            self.assertEqual(result["data"], DATASET)
            self.assertEqual(request.call_count, 1)
            with patch.object(context, "request_with_completion_retry", side_effect=AssertionError("cache miss")):
                cached = context._analysis_record(
                    "system", {"input": "evidence"}, "openai", "model", Path(directory),
                    "dataset", context.validate_dataset_context,
                )
            self.assertEqual(cached, result)

    def test_analysis_record_corrects_invalid_but_parseable_response(self):
        invalid = deepcopy(DATASET)
        invalid["dataset_profile"] = None
        with TemporaryDirectory() as directory, patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}), \
                patch.object(context, "request_with_completion_retry",
                             side_effect=[self.reply(invalid), self.reply(DATASET)]) as request:
            result = context._analysis_record(
                "system", {"input": "evidence"}, "openai", "model", Path(directory),
                "dataset", context.validate_dataset_context,
            )
        self.assertEqual(result["data"], DATASET)
        self.assertEqual(request.call_count, 2)


if __name__ == "__main__":
    unittest.main()
