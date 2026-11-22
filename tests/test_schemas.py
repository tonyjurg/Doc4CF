"""Every shipped context artifact schema is syntactically valid and exercised."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource


SCHEMA_DIR = Path(__file__).resolve().parents[1] / "doc4cf" / "schemas"
DIGEST = "a" * 64
FLAG = {"issue": "A detail needs review.", "status": "missing_evidence", "evidence": ["inventory.features.word"]}
ANALYSIS = {
    "provider": "openai", "requested_model": "model-a", "responding_model": "model-b",
    "prompt_version": "context-analysis-1",
}


ARTIFACTS = {
    "dataset-inventory-1.0.schema.json": {
        "inventory_version": "1.0", "dataset": {"title": "Sample corpus"}, "corpus_label": "Sample corpus",
        "source": {"content_sha256": DIGEST, "declared_version": None},
        "structure": {"node_types_in_corpus_order": [{"name": "word", "node_count": 2, "is_slot_type": True}],
                      "slot_type": "word", "reference_sections": []},
        "features": {"word": {"kind": "node", "metadata": {"description": "A token"}, "encoding": "UTF-8",
                               "value_type": "str", "observed_node_types": ["word"], "sources": {"word": 2},
                               "targets": {}, "distinct_values": 2, "frequent_values": [
                                   {"value": "one", "count": 1}, {"value": "two", "count": 1}], "examples": ["one", "two"]}},
    },
    "dataset-context-1.0.schema.json": {
        "context_version": "1.0", "inventory_sha256": DIGEST, "dataset_profile": "A small sample corpus.",
        "conventions": [{"claim": "Tokens are recorded", "status": "verified", "evidence": ["features.word"]}],
        "ambiguities": [], "needs_review": False, "analysis": ANALYSIS,
    },
    "feature-families-1.0.schema.json": {
        "families_version": "1.0", "inventory_sha256": DIGEST, "analysis": ANALYSIS,
        "families": [{"id": "lexical", "label": "Lexical", "purpose": "Token values", "features": ["word"],
                      "status": "inferred", "evidence": ["features.word"], "needs_review": False}],
    },
    "feature-relationships-1.0.schema.json": {
        "relationships_version": "1.0", "inventory_sha256": DIGEST, "analysis": ANALYSIS,
        "relationships": [{"source_feature": "word", "target_feature": "lemma", "relationship": "has lemma",
                            "status": "inferred", "evidence": ["features.word"], "needs_review": True}],
    },
    "context-manifest-1.0.schema.json": {
        "manifest_version": "1.0", "applied": {"word": {
            "dataset_context_sha256": DIGEST, "feature_context_sha256": DIGEST,
            "feature_evidence_sha256": DIGEST, "provider": "openai", "model": "model-a",
            "evidence_mode": "compact", "prompt_sha256": DIGEST,
        }}, "context_flags": {"word": [FLAG]},
    },
    "context-review-1.0.schema.json": {
        "inventory_sha256": DIGEST, "affected_descriptions": [{"feature": "word", "reasons": ["context changed"]}],
        "processed_descriptions": ["word"], "context_flags": [{"feature": "word", "flags": [FLAG]}],
    },
}


INVALID_MUTATIONS = {
    "dataset-inventory-1.0.schema.json": lambda value: value.__setitem__("corpus_label", ""),
    "dataset-context-1.0.schema.json": lambda value: value.__setitem__("context_version", "2.0"),
    "feature-families-1.0.schema.json": lambda value: value["families"][0].__setitem__("id", "Bad"),
    "feature-relationships-1.0.schema.json": lambda value: value["relationships"][0].__setitem__("status", "maybe"),
    "context-manifest-1.0.schema.json": lambda value: value["applied"]["word"].__setitem__("evidence_mode", "verbose"),
    "context-review-1.0.schema.json": lambda value: value.__setitem__("inventory_sha256", "stale"),
}


class ShippedSchemas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schemas = {path.name: json.loads(path.read_text(encoding="utf-8"))
                       for path in sorted(SCHEMA_DIR.glob("*.schema.json"))}
        cls.registry = Registry().with_resources(
            (schema["$id"], Resource.from_contents(schema)) for schema in cls.schemas.values()
        )

    def test_all_six_schemas_are_valid_and_accept_matching_artifacts(self):
        self.assertEqual(set(self.schemas), set(ARTIFACTS))
        for filename, schema in self.schemas.items():
            with self.subTest(schema=filename):
                Draft202012Validator.check_schema(schema)
                Draft202012Validator(schema, registry=self.registry).validate(ARTIFACTS[filename])

    def test_each_schema_rejects_a_malformed_artifact(self):
        for filename, schema in self.schemas.items():
            malformed = deepcopy(ARTIFACTS[filename])
            INVALID_MUTATIONS[filename](malformed)
            with self.subTest(schema=filename), self.assertRaises(ValidationError):
                Draft202012Validator(schema, registry=self.registry).validate(malformed)

    def test_review_schema_accepts_feature_audit_records(self):
        artifact = deepcopy(ARTIFACTS["context-review-1.0.schema.json"])
        artifact["feature_analysis"] = {"word": {"provider": "OpenAI", "uncertainties": [], "context_flags": []}}
        validator = Draft202012Validator(self.schemas["context-review-1.0.schema.json"], registry=self.registry)
        validator.validate(artifact)
        artifact["feature_analysis"]["word"] = "not an audit record"
        with self.assertRaises(ValidationError):
            validator.validate(artifact)


if __name__ == "__main__":
    unittest.main()
