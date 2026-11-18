# Contributing

Thanks for helping improve Doc4CF. Changes should keep generated references deterministic, preserve corpus feature names, and validate all model-supplied context before using it.

## Development setup

Use Python 3.13 or newer and install the project with its development tools:

```sh
python -m pip install -e ".[dev]"
```

To run the local checks before opening a pull request:

```sh
ruff check .
mypy doc4cf
python -m unittest discover -s tests -p 'test_*.py'
```

Install and enable the pre-commit hooks with:

```sh
pre-commit install
```

The hooks run Ruff and Mypy. CI also runs the unit tests on every pull request.

## Pull requests

- Keep changes focused and include regression tests for bug fixes and validation paths.
- Do not commit corpus API keys, private corpus data, generated caches, or local build output.
- Describe behavior changes, the checks you ran, and any limitations in the pull request.
- For security issues, follow the private reporting instructions in [SECURITY.md](SECURITY.md).
