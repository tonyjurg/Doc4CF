# Rebuild the example documentation

Open these notebooks from a Doc4CF checkout in Jupyter with a Python 3.13+ kernel:

- [N1904](generate_N1904.ipynb): version 1.0.0, 61 features, with optional [editorial context](contexts/N1904.txt).
- [Dead Sea Scrolls](generate_DSS.ipynb): base version 2.0.4, 79 features.
- [Old Babylonian letters](generate_OldBabylonian.ipynb): version 1.0.6, 67 features.

Each notebook pins the source revision, installs Doc4CF, checks the corpus, and provides an optional step to update its checked-in example. Their default workflows differ: DSS builds offline; N1904 prepares a dataset-context overview with one model request and skips the site build; Old Babylonian runs the full context and feature-description workflow. Install Jupyter with `python -m pip install jupyterlab`, then start it with `python -m jupyterlab` from the repository root.

To create a Markdown companion for any corpus, run the CLI build with `--markdown`. The export follows Doc4TF's lightweight corpus index and one-page-per-feature structure, with Doc4CF's short feature descriptions, common values, calculated measurements, and optional inferred descriptions. The index stays concise while each feature file can hold more computed detail and explicitly attributed interpretation. This is a formatting option on the same build and adds no separate model requests.

The N1904 notebook also exposes `MARKDOWN = True`. For its full build, set `OVERVIEW_ONLY = False`; use `USE_LLM = True` to include context-aware descriptions or `False` for measured documentation only. The enriched path loads the corpus once to prepare and cache descriptions, then renders the complete HTML and Markdown reference once. Its checks report feature-page coverage and generated-description coverage separately. `CONTEXT_PAGES` controls the dataset and relationship pages.

After rendering, the N1904 workflow applies a source-cited clarification for `ln` from the pinned upstream Louw–Nida tutorial. The feature page labels an edited inference **Reviewed description**, or adds an **Editorial description** in an offline build. Its source metadata and raw model cache stay unchanged; the audit page records the clarification. This step is reproducible through `scripts/apply_n1904_editorial_notes.py`.

For a side-by-side explanation of inference levels and how these notebook defaults compare with the checked-in examples, see the [example methods page](../example-methods.html).

For an offline full-site build, set `USE_LLM = False` in DSS and Old Babylonian. In N1904, also set `OVERVIEW_ONLY = False`; its default overview-only mode makes one OpenRouter request and does not build a site. To run N1904's full context-aware feature workflow, set `OVERVIEW_ONLY = False` and `USE_LLM = True`. The notebooks select `nvidia/nemotron-3.5-super-vl:free` for N1904 and Old Babylonian, and `openrouter/free` for DSS. Free model availability can change; select another available model if needed. No paid fallback is configured. Keys come from the environment or a hidden prompt. Successful analysis and feature responses are cached locally; rerun the interrupted cell after a transient failure or quota reset. New LLM prose is not guaranteed to match previous output.

The full enriched workflow makes two context-analysis requests before generating one description request per feature. N1904's default overview-only run makes a single dataset-context request instead. Set `TARGETED_EVIDENCE = True` to add a planning request per feature so Doc4CF can retrieve rare values or examples from the corpus. This can increase free-tier usage. OpenRouter and OpenAI use strict JSON Schema output when supported, with a JSON-mode fallback and local validation.

Dataset-level analysis can take an optional UTF-8 instruction file through the `DATASET_INSTRUCTIONS` notebook setting or the CLI `--dataset-instructions` option. The supplemental instructions can guide focus or phrasing; the core evidence and output rules remain in force. The exact instruction text is hashed into the analysis cache key and recorded in the dataset artifact provenance.

Feature descriptions use separate prompts for node and edge features, with more specific prompts for the Text-Fabric structural features `otype`, `otext`, and `oslots`. Descriptions target roughly 45–75 words. They may offer a cautious interpretation when measured values, metadata, or app configuration support it, and should mark uncertain meanings with wording such as “may” or “might.” Edge prompts receive measured endpoint-type and links-per-source summaries. Changing a prompt changes the corresponding request hash, so a later inference run may need new responses for affected features.

The N1904 editorial context is in `contexts/N1904.txt`. It guides audience and terminology but does not supply measured facts or override the feature prompt's length, evidence, and value-selection rules. DSS and Old Babylonian have no additional context file by default; each notebook lets you set `CONTEXT` to a UTF-8 notes file.

Builds and downloaded corpora live in ignored `.testdata/` directories, and responses in `.doc4cf-cache/`. Notebook outputs are not cleared automatically. Before sharing or committing, run `python scripts/clear_notebook_outputs.py`; it clears code-cell outputs and execution counts while preserving code and Markdown. CI checks this on pushes and pull requests and fails if saved outputs remain. Actions run after a push, so they cannot clean the file before it reaches GitHub; required checks can block a PR merge, while a direct push has already landed. No key, conversation history, or local cache is needed to view a generated site.
