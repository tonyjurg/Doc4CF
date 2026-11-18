"""Keep example notebooks syntactically valid and aligned with the CLI."""
import ast
import json
from pathlib import Path
import re
import unittest


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


if __name__ == "__main__":
    unittest.main()
