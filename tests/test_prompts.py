"""Prompt digests lock current text versions and guard cache-key changes."""
import hashlib
import unittest

from doc4cf import context, generator


class PromptFiles(unittest.TestCase):
    def test_prompt_hashes_match_the_current_versioned_text(self):
        expected = {
            "dataset context": (context.DATASET_SYSTEM, "99b029574c839473e9e51e4c8e0c7169097a6be87d0753ee9c76d6160379e7f4"),
            "family context": (context.FAMILY_SYSTEM, "7ad3458704ba89dc0222f0d9f8e0c619e00d80c0f70817d726f2deae8d33fd7c"),
            "feature context": (context.FEATURE_SYSTEM, "21a52d5c3552e6264e7ab465f32d5842f0b454826968a39dc730be32c1da74ff"),
            "evidence plan": (context.EVIDENCE_SYSTEM, "b4aa393e7645213fea80e50a39fd0f94fe2129890bb02fb0f3f651c31371016a"),
            "feature description": (generator.FEATURE_SYSTEM, "149ac9c058d0f700cb1a8c7640ca6861a71dcd37bddef56783f6bef476decd9b"),
        }
        for label, (prompt, digest) in expected.items():
            with self.subTest(prompt=label):
                self.assertEqual(hashlib.sha256(prompt.encode("utf-8")).hexdigest(), digest)


if __name__ == "__main__":
    unittest.main()
