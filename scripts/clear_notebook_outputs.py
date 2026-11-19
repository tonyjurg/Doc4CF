"""Clear saved Jupyter cell output before sharing notebooks, or check CI state."""

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Clear saved code-cell outputs and execution counts from notebooks."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if any notebook has saved code-cell output; do not modify files.",
    )
    args = parser.parse_args()

    dirty: list[Path] = []
    cleared = 0
    for path in sorted(NOTEBOOKS.glob("*.ipynb")):
        notebook = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "code":
                continue
            if cell.get("outputs", []):
                changed = True
                cell["outputs"] = []
            if cell.get("execution_count") is not None:
                changed = True
                cell["execution_count"] = None
        if not changed:
            continue
        dirty.append(path)
        if not args.check:
            path.write_text(
                json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
                encoding="utf-8",
                newline="",
            )
            cleared += 1

    if args.check:
        if dirty:
            print("Notebooks contain saved outputs or execution counts:")
            for path in dirty:
                print(f"  {path.relative_to(ROOT)}")
            print("Run: python scripts/clear_notebook_outputs.py")
            return 1
        print("Notebook outputs and execution counts are clear.")
        return 0

    print(f"Cleared saved outputs and execution counts in {cleared} notebook(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
