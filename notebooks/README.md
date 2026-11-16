# Rebuild the example documentation

Open these notebooks from a Doc4CF checkout in Jupyter with a Python 3.13+ kernel:

- [N1904](generate_N1904.ipynb): version 1.0.0, 61 features, with optional [editorial context](contexts/N1904.txt).
- [Dead Sea Scrolls](generate_DSS.ipynb): base version 2.0.4, 79 features.
- [Old Babylonian letters](generate_OldBabylonian.ipynb): version 1.0.6, 67 features.

Each notebook pins the source revision, installs Doc4CF, analyzes and lets you inspect reusable context, generates the full site with that context, copies the source license, checks completeness, and provides an optional step to replace the checked-in example. Install Jupyter with `python -m pip install jupyterlab`, then start it with `python -m jupyterlab` from the repository root.

The default build is offline after installing dependencies and fetching the corpus. Set `USE_LLM = True` to run context analysis first, review its JSON artifacts, and then generate context-aware feature descriptions and optional dataset/relationship/review pages. N1904 selects `nvidia/nemotron-3.5-super-vl:free`; the other notebooks select `openrouter/free`. Free model availability can change; select another available model if needed. No paid fallback is configured. Keys come from the environment or a hidden prompt. Successful analysis and feature responses are cached locally; rerun the interrupted cell after a transient failure or quota reset. New LLM prose is not guaranteed to match previous output.

Each enriched notebook makes two context-analysis requests before generating one description request per feature. Set `TARGETED_EVIDENCE = True` to add a planning request per feature so Doc4CF can retrieve rare values or examples from the corpus. This can increase free-tier usage. OpenRouter and OpenAI use strict JSON Schema output when supported, with a JSON-mode fallback and local validation.

The N1904 editorial context was moved unchanged from `examples/promt_augmentation_N1904` to `contexts/N1904.txt`. Its full contents accompany each N1904 feature profile in an enriched build, as editorial background rather than measured facts. DSS and Old Babylonian have no additional context file by default; each notebook lets you set `CONTEXT` to a UTF-8 notes file.

Builds and downloaded corpora live in ignored `.testdata/` directories, and responses in `.doc4cf-cache/`. Notebook outputs are deliberately cleared. No key, conversation history, or local cache is needed to view a generated site.
