"""Regression checks for association bounds."""
import unittest
from array import array
from unittest import mock
from doc4cf import generator


class AssociationBounds(unittest.TestCase):
    def test_constant_and_sparse_features_do_not_consume_the_comparison_budget(self):
        assignments = {"constant": {"word": array("Q", range(1, 61))},
                       "rare": {"word": array("Q", [1, 2])},
                       "a": {"word": array("Q", range(1, 31))},
                       "b": {"word": array("Q", range(1, 31))}}
        limits = {}
        with mock.patch.object(generator, "_MAX_ASSOCIATION_FEATURES", 2):
            result = generator._feature_associations(assignments, {"word": 60}, ["word"], limits)
        self.assertEqual(result["a"][0]["positive"][0]["features"], ["b"])
        self.assertEqual(result["a"][0]["positive"][0]["phi"], 1.0)
        self.assertEqual(result["constant"], [])
        self.assertEqual(result["rare"], [])
        self.assertEqual(limits, {})
        self.assertEqual(generator._association_limit_notice(
            "constant", assignments["constant"], {"word": (4, {"a", "b"})}, {"word": 60}), "")

    def test_reduced_scope_is_reported_and_unselected_features_are_identified(self):
        assignments = {name: {"word": array("Q", range(1, 31))} for name in ("a", "b", "c")}
        limits = {}
        with mock.patch.object(generator, "_MAX_ASSOCIATION_FEATURES", 2):
            result = generator._feature_associations(assignments, {"word": 60}, ["word"], limits)
        self.assertEqual(limits, {"word": (3, {"a", "b"})})
        self.assertEqual(result["a"][0]["positive"][0]["phi"], 1.0)
        self.assertEqual(result["c"], [])
        included = generator._association_limit_notice("a", assignments["a"], limits)
        excluded = generator._association_limit_notice("c", assignments["c"], limits)
        self.assertIn("2 best-covered of 3", included)
        self.assertNotIn("excluded", included)
        self.assertIn("This feature was excluded", excluded)
        self.assertEqual(generator._association_limit_notice("a", {"phrase": []}, limits), "")

    def test_work_limit_can_disable_all_pair_comparisons(self):
        assignments = {name: {"word": array("Q", range(1, 31))} for name in ("a", "b")}
        limits = {}
        with mock.patch.object(generator, "_MAX_ASSOCIATION_WORK", 1):
            result = generator._feature_associations(assignments, {"word": 60}, ["word"], limits)
        self.assertEqual(result, {"a": [], "b": []})
        self.assertEqual(limits, {"word": (2, {"a"})})

    def test_feature_count_and_work_are_bounded(self):
        feature_ids = {f"f{i:03}": array("Q", range(1, 2001)) for i in range(150)}
        kept = generator._bounded_association_features(feature_ids)
        self.assertLessEqual(len(kept), generator._MAX_ASSOCIATION_FEATURES)
        entries = sum(len(ids) for ids in kept.values())
        self.assertLessEqual(entries * (len(kept) - 1) / 2, generator._MAX_ASSOCIATION_WORK)

    def test_large_inputs_prefer_best_covered_features(self):
        feature_ids = {"rare": array("Q", [1]), "common": array("Q", range(1, 1000))}
        self.assertEqual(list(generator._bounded_association_features(feature_ids)), ["common", "rare"])
        many = {f"f{i}": array("Q", range(1, 200_001)) for i in range(60)}
        kept = generator._bounded_association_features(many)
        self.assertLess(len(kept), 60)
        self.assertGreaterEqual(len(kept), 2)

    def test_full_computation_completes_with_many_features(self):
        nodes = 1500
        assignments = {f"f{i:03}": {"word": array("Q", range(1, nodes + 1))} for i in range(150)}
        result = generator._feature_associations(assignments, {"word": nodes * 2}, ["word"])
        self.assertEqual(set(result), set(assignments))
        self.assertEqual(result["f000"][0]["positive"][0]["phi"], 1.0)
        self.assertEqual(result["f149"], [])


if __name__ == "__main__":
    unittest.main()
