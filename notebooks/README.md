# Rebuild the example documentation

Open these notebooks from a Doc4CF checkout in Jupyter with a Python 3.13+ kernel:

- [N1904](generate_N1904.ipynb): version 1.0.0, 61 features, with optional [editorial context](contexts/N1904.txt).
- [Dead Sea Scrolls](generate_DSS.ipynb): base version 2.0.4, 79 features.
- [Old Babylonian letters](generate_OldBabylonian.ipynb): version 1.0.6, 67 features.

Each notebook pins the source revision, installs Doc4CF, generates the full site, copies the source license, checks completeness, and provides an optional step to replace the checked-in example. Install Jupyter with `python -m pip install jupyterlab`, then start it with `python -m jupyterlab` from the repository root.

The default build is offline after installing dependencies and fetching the corpus. Set `USE_LLM = True` to add descriptions through OpenRouter. N1904 selects `nvidia/nemotron-3.5-super-vl:free` for a consistent model; the other notebooks select `openrouter/free`. Free model availability can change; if necessary, select another available `:free` model or the free router. No paid fallback is configured. Keys come from the environment or a hidden prompt. Successful responses are cached locally; rerun the generation cell after a transient failure or once a free quota resets. New LLM prose is not guaranteed to match previous output.

The N1904 context was moved unchanged from `examples/promt_augmentation_N1904` to `contexts/N1904.txt`. Its full contents accompany each N1904 feature profile in an enriched build. It is not used by offline builds. DSS and Old Babylonian have no additional context file.

Builds and downloaded corpora live in ignored `.testdata/` directories, and responses in `.doc4cf-cache/`. Notebook outputs are deliberately cleared. No key, conversation history, or local cache is needed to view a generated site.
