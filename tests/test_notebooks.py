"""Keep example notebooks syntactically valid and aligned with the CLI."""
import ast
import json
from pathlib import Path
import re
import unittest
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

from doc4cf import context, generator


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb"))
GIT_OPTIONS = {"--detach", "--porcelain"}


def cli_options() -> set[str]:
    """Read the CLI switches directly from the argparse declarations."""
    source = ast.parse((ROOT / "doc4cf" / "generator.py").read_text(encoding="utf-8"))
    return {
        argument.value
        for node in ast.walk(source)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "add_argument"
        for argument in node.args
        if isinstance(argument, ast.Constant)
        and isinstance(argument.value, str)
        and argument.value.startswith("--")
    }


class NotebookConsistency(unittest.TestCase):
    def test_code_cells_compile_and_outputs_are_cleared(self):
        self.assertTrue(NOTEBOOKS, "Expected example notebooks")
        for path in NOTEBOOKS:
            notebook = json.loads(path.read_text(encoding="utf-8"))
            with self.subTest(notebook=path.name):
                for index, cell in enumerate(notebook["cells"]):
                    if cell["cell_type"] != "code":
                        continue
                    compile("".join(cell["source"]), f"{path.name}:cell{index}", "exec")
                    self.assertEqual(cell.get("outputs", []), [])

    def test_notebook_cli_switches_exist(self):
        known = cli_options()
        for path in NOTEBOOKS:
            notebook = json.loads(path.read_text(encoding="utf-8"))
            code = "\n".join(
                "".join(cell["source"])
                for cell in notebook["cells"]
                if cell["cell_type"] == "code"
            )
            used = set(re.findall(r"['\"](--[a-z][a-z-]+)['\"]", code))
            with self.subTest(notebook=path.name):
                self.assertEqual(used - known - GIT_OPTIONS, set())


class N1904BuildModes(unittest.TestCase):
    def run_build(self, temporary, use_llm, context_pages=True, quota=False):
        folder = Path(temporary)
        corpus = folder / "corpus"
        corpus.mkdir()
        for name in ("word", "lemma"):
            (corpus / f"{name}.tf").write_text("@node\n@valueType=str\n\nx\n", encoding="utf-8")
        notebook = json.loads((ROOT / "notebooks" / "generate_N1904.ipynb").read_text(encoding="utf-8"))
        source = "".join(notebook["cells"][12]["source"])
        import shutil
        import subprocess
        import sys
        namespace = {"OVERVIEW_ONLY": False, "USE_LLM": use_llm, "MARKDOWN": True,
                     "CONTEXT_PAGES": context_pages, "TARGETED_EVIDENCE": False,
                     "PROVIDER": "openrouter", "FEATURE_MODEL": "test/free", "CONTEXT": None,
                     "ROOT": ROOT, "CORPUS": corpus, "OUTPUT": folder / "site", "SOURCE": corpus,
                     "CONTEXT_DIR": folder / "context", "CACHE": folder / "cache",
                     "sys": sys, "subprocess": subprocess, "shutil": shutil}
        api = SimpleNamespace(F=SimpleNamespace(otype=SimpleNamespace(all=["word"], s=lambda _t: [1, 2])))
        response = SimpleNamespace(returncode=0, stdout="", stderr="")
        error = RuntimeError("OpenRouter daily free-model quota exhausted") if quota else None
        with patch.object(generator, "load_corpus", return_value=api), \
                patch.object(generator, "dataset_inventory", return_value={"corpus_label": "Corpus"}), \
                patch.object(generator, "_observed_values", return_value={}), \
                patch.object(generator, "profile", side_effect=lambda _a, name, *_rest: {"name": name, "kind": "node"}), \
                patch.object(context, "load_context_artifacts", return_value=({}, [], [], None)), \
                patch.object(context, "contextual_description_record", side_effect=error) as describe, \
                patch.object(subprocess, "run", return_value=response) as run, \
                patch.object(shutil, "copyfile"), patch("builtins.print"):
            exec(compile(source, "N1904:build", "exec"), namespace)  # noqa: S102 - exercise the repository's notebook cell
        self.assertEqual(run.call_count, 2)
        self.assertTrue(run.call_args_list[1].args[0][1].endswith("apply_n1904_editorial_notes.py"))
        return namespace, run.call_args_list[0].args[0], describe

    def test_offline_build_exports_markdown_without_model_calls(self):
        with TemporaryDirectory() as temporary:
            _, command, describe = self.run_build(temporary, False)
        self.assertIn("--markdown", command)
        self.assertNotIn("--model", command)
        describe.assert_not_called()

    def test_descriptions_are_prepared_before_one_site_build(self):
        with TemporaryDirectory() as temporary:
            state, command, describe = self.run_build(temporary, True)
        self.assertEqual(describe.call_count, 2)
        self.assertEqual(state["completed_features"], ["lemma", "word"])
        self.assertIn("--context-pages", command)
        self.assertIn("--describe-features", command)
        self.assertEqual(command[-1], "lemma,word")

    def test_zero_quota_fallback_respects_context_page_setting(self):
        for enabled in (False, True):
            with self.subTest(context_pages=enabled), TemporaryDirectory() as temporary:
                state, command, _ = self.run_build(temporary, True, enabled, quota=True)
            self.assertTrue(state["quota_exhausted"])
            self.assertEqual(state["completed_features"], [])
            self.assertNotIn("--model", command)
            self.assertEqual("--context-dir" in command, enabled)
            self.assertEqual("--context-pages" in command, enabled)


if __name__ == "__main__":
    unittest.main()
