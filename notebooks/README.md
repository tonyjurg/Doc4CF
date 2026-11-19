# Rebuild the example documentation

Open these notebooks from a Doc4CF checkout in Jupyter with a Python 3.13+ kernel:

- [N1904](generate_N1904.ipynb): version 1.0.0, 61 features, with optional [editorial context](contexts/N1904.txt).
- [Dead Sea Scrolls](generate_DSS.ipynb): base version 2.0.4, 79 features.
- [Old Babylonian letters](generate_OldBabylonian.ipynb): version 1.0.6, 67 features.

Each notebook pins the source revision, installs Doc4CF, checks the corpus, and provides an optional step to update its checked-in example. Their default workflows differ: DSS builds offline; N1904 prepares a dataset-context overview with one model request and skips the site build; Old Babylonian runs the full context and feature-description workflow. Install Jupyter with `python -m pip install jupyterlab`, then start it with `python -m jupyterlab` from the repository root.

For a side-by-side explanation of inference levels and how these notebook defaults compare with the checked-in examples, see the [example methods page](../example-methods.html).

For an offline full-site build, set `USE_LLM = False` in DSS and Old Babylonian. In N1904, also set `OVERVIEW_ONLY = False`; its default overview-only mode makes one OpenRouter request and does not build a site. To run N1904's full context-aware feature workflow, set `OVERVIEW_ONLY = False` and `USE_LLM = True`. The notebooks select `nvidia/nemotron-3.5-super-vl:free` for N1904 and Old Babylonian, and `openrouter/free` for DSS. Free model availability can change; select another available model if needed. No paid fallback is configured. Keys come from the environment or a hidden prompt. Successful analysis and feature responses are cached locally; rerun the interrupted cell after a transient failure or quota reset. New LLM prose is not guaranteed to match previous output.

The full enriched workflow makes two context-analysis requests before generating one description request per feature. N1904's default overview-only run makes a single dataset-context request instead. Set `TARGETED_EVIDENCE = True` to add a planning request per feature so Doc4CF can retrieve rare values or examples from the corpus. This can increase free-tier usage. OpenRouter and OpenAI use strict JSON Schema output when supported, with a JSON-mode fallback and local validation.

Dataset-level analysis can take an optional UTF-8 instruction file through the `DATASET_INSTRUCTIONS` notebook setting or the CLI `--dataset-instructions` option. The supplemental instructions can guide focus or phrasing; the core evidence and output rules remain in force. The exact instruction text is hashed into the analysis cache key and recorded in the dataset artifact provenance.

The N1904 editorial context was moved unchanged from `examples/promt_augmentation_N1904` to `contexts/N1904.txt`. Its full contents accompany each N1904 feature profile in an enriched build, as editorial background rather than measured facts. DSS and Old Babylonian have no additional context file by default; each notebook lets you set `CONTEXT` to a UTF-8 notes file.

Builds and downloaded corpora live in ignored `.testdata/` directories, and responses in `.doc4cf-cache/`. Notebook outputs are deliberately cleared. No key, conversation history, or local cache is needed to view a generated site.
