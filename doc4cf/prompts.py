"""Read the versioned prompt text shipped with Doc4CF."""
from pathlib import Path


_PROMPT_DIR = Path(__file__).with_name("prompts")
_DESCRIPTION_DIR = Path(__file__).with_name("descriptions")


def load_prompt(filename: str) -> str:
    """Load a UTF-8 prompt, dropping only its file-ending newline.

    Prompt constants historically had no final newline. Keeping that invariant
    preserves the request bytes and cache keys when the text lives in files.
    """
    return (_PROMPT_DIR / filename).read_text(encoding="utf-8").removesuffix("\n")


def load_description(filename: str) -> str:
    """Load an editable standard feature description from its text file."""
    return (_DESCRIPTION_DIR / filename).read_text(encoding="utf-8").removesuffix("\n")
