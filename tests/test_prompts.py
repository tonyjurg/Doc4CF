"""Prompt text stays byte-identical to preserve existing response-cache keys."""
import hashlib
import unittest

from doc4cf import context, generator


class PromptFiles(unittest.TestCase):
    def test_prompt_hashes_match_the_original_inline_text(self):
        expected = {
            "dataset context": (context.DATASET_SYSTEM, "c2b65a9b5551354290e842e8cf070069cea2c6df3ee024673faa75a350fa9526"),
            "family context": (context.FAMILY_SYSTEM, "7ad3458704ba89dc0222f0d9f8e0c619e00d80c0f70817d726f2deae8d33fd7c"),
            "feature context": (context.FEATURE_SYSTEM, "fe50727f0d35f1dd485fde0d9803aaf9bf2d008d1b0df75667c5b6c0d44cdae3"),
            "evidence plan": (context.EVIDENCE_SYSTEM, "b4aa393e7645213fea80e50a39fd0f94fe2129890bb02fb0f3f651c31371016a"),
            "feature description": (generator.FEATURE_SYSTEM, "d6d5579cacb1f3d101020d9053ad0fc71c82677dda2519e99e797c7dfe222f7f"),
        }
        for label, (prompt, digest) in expected.items():
            with self.subTest(prompt=label):
                self.assertEqual(hashlib.sha256(prompt.encode("utf-8")).hexdigest(), digest)


if __name__ == "__main__":
    unittest.main()
