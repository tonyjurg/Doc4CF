"""Structural Text-Fabric features have separate defaults and model guidance."""
from types import SimpleNamespace
import unittest

from doc4cf.generator import (
    FEATURE_SYSTEM,
    feature_description_prompt,
    profile,
    standard_feature_description,
)
from doc4cf.prompts import load_prompt


class StructuralFeatureDescriptions(unittest.TestCase):
    def test_standard_descriptions_are_feature_specific_and_editable(self):
        descriptions = {
            name: standard_feature_description(name)
            for name in ("otype", "otext", "oslots")
        }
        self.assertTrue(all(text.strip() for text in descriptions.values()))
        self.assertEqual(len(set(descriptions.values())), 3)
        self.assertIn("node type", descriptions["otype"])
        self.assertIn("Text API", descriptions["otext"])
        self.assertIn("slot nodes", descriptions["oslots"])

    def test_feature_prompts_specialize_each_structural_feature(self):
        prompts = {
            name: feature_description_prompt(name)
            for name in ("otype", "otext", "oslots")
        }
        self.assertTrue(all(prompt.startswith(FEATURE_SYSTEM) for prompt in prompts.values()))
        self.assertEqual(len(set(prompts.values())), 3)
        self.assertIn("node-type map", prompts["otype"])
        self.assertIn("configuration", prompts["otext"])
        self.assertIn("edge map", prompts["oslots"])
        self.assertEqual(feature_description_prompt("ordinary_feature"), FEATURE_SYSTEM)

    def test_profiles_keep_node_edge_and_config_evidence_distinct(self):
        node_types = {1: "word", 2: "word", 3: "line"}
        api = SimpleNamespace(
            F=SimpleNamespace(otype=SimpleNamespace(
                v=lambda node: node_types[node], slotType="word")),
            Fs=lambda _name: SimpleNamespace(items=lambda: iter(node_types.items())),
            Es=lambda _name: SimpleNamespace(items=lambda: iter([(3, (1, 2))])),
        )
        otype = profile(api, "otype", {
            "kind": "node", "meta": {"description": "Header description"},
        }, ["word", "line"])
        self.assertEqual(otype["sources"], {"word": 2, "line": 1})
        self.assertIn("node type", otype["description"])

        oslots = profile(api, "oslots", {"kind": "edge", "meta": {}}, ["word", "line"])
        self.assertEqual(oslots["sources"], {"line": 1})
        self.assertEqual(oslots["targets"], {"word": 2})

        configuration = {"sectionTypes": "book,chapter", "fmt:text-orig-full": "{word}"}
        otext = profile(api, "otext", {"kind": "config", "meta": configuration}, [])
        self.assertEqual(otext["configuration"], configuration)
        self.assertIn("Text API", otext["description"])

    def test_each_structural_guidance_is_a_separate_text_file(self):
        for name in ("otype", "otext", "oslots"):
            with self.subTest(name=name):
                self.assertTrue(load_prompt(f"feature-{name}.txt").strip())


if __name__ == "__main__":
    unittest.main()
