# Doc4CF

![Work in progress](https://img.shields.io/badge/status-work%20in%20progress-orange)

Doc4CF generates an offline, interactive HTML reference for a single Context-Fabric corpus version. After cloning this repository, open an example locally in a browser: [Nestle 1904 Greek New Testament](examples/N1904/index.html), [ETCBC Dead Sea Scrolls](examples/DSS/index.html), or [Old Babylonian letters](examples/OldBabylonian/index.html).

## Build

From the Doc4CF checkout, activate a Python 3.13+ virtual environment. Give the generator the directory containing the actual TF files and a dedicated output directory.

```sh
python -m pip install .
git clone --depth 1 https://github.com/CenterBLC/N1904.git
doc4cf N1904/tf/1.0.0 site
```

Open `site/index.html`. All navigation, search and graph exploration work with local files. Context-Fabric may build a compiled cache next to the corpus, so use a writable copy. Build into a fresh output directory when switching corpora.

## Distribute and install privately

In an activated Python 3.13+ virtual environment, run:

```sh
python -m pip install build
python -m build
```

Share the wheel from `dist/` with recipients. They can run `python -m pip install path/to/doc4cf-0.1.0-py3-none-any.whl` and then `doc4cf --help`. Pip resolves Context-Fabric during installation. The wheel includes the JavaScript, CSS, and SVG logos; readers need only the generated site and a browser.

## Build the API reference

Install the optional documentation dependencies and build the current source version locally:

```sh
python -m pip install -e ".[docs]"
python scripts/build_api_docs.py --current-only --output .testdata/api
```

GitHub Pages builds the same Sphinx reference and adds published release versions to the selector.

## Software setup, levels of inference, and usage examples

The [install guide](install-guide.html) covers setup, usage, and optional LLM descriptions. The [software design page](software-design.html) explains how Doc4CF uses Context-Fabric to combine feature documentation with a knowledge graph. The [versioned Python API reference](https://tonyjurg.github.io/Doc4CF/api/) is generated from the current source and published releases with Sphinx.

The current optional AI enrichment workflow, evidence safeguards, and review artifacts are described in [AI_STRATEGY.md](AI_STRATEGY.md).

Export a deterministic, model-free inventory for review or downstream analysis with `doc4cf path/to/corpus/tf/VERSION --export-inventory inventory.json`. The versioned inventory and AI context artifact schemas ship under `doc4cf/schemas/`.

Generate reusable dataset and feature-family context with `doc4cf path/to/corpus/tf/VERSION --analyze-context reviewed-context --provider openrouter --context-model MODEL_ID --family-model MODEL_ID`. This writes the inventory plus dataset, feature-family, and feature-relationship JSON artifacts. Analysis is an explicit, cacheable command; it does not build or change the HTML site. See the [install guide](install-guide.html#runtime-options) for details.

After reviewing the artifacts, use `--context-dir reviewed-context` on a normal site build to enrich feature descriptions with global and relevant family context. Add `--context-pages` for dataset architecture/glossary, relationship, and review pages. The build rejects stale context and model-declared feature/value references that do not exist in the current corpus. It records affected descriptions and context flags in `context_review.json`; unchanged requests reuse the cache. Omitting `--context-dir` keeps the existing feature-only behavior.

Use `--overview-notes FILE` to add editor-supplied dataset prose to `index.html`. When reviewed context artifacts are also supplied with `--context-dir`, the overview combines those notes with the inventory analysis, evidence-labeled conventions, and any review questions. The rendered page labels the sources separately so model interpretations remain distinguishable from editor-supplied description.

For richer per-feature evidence, add `--targeted-evidence`. The model can request rare values or representative examples; Doc4CF retrieves those deterministically from the loaded corpus before generating the final description. Both planning and description responses are cached. See the [install guide](install-guide.html#runtime-options).

Context analysis uses strict JSON Schema output with OpenRouter and OpenAI when the selected model supports it. Doc4CF falls back to JSON mode for those endpoints when schema output is rejected, and validates every response locally.

When a corpus is loaded from a repository layout such as `repository/tf/version`, inventory export and context analysis also detect the sibling `app/` directory. They include its YAML configuration as structured data and static summaries of Python app methods, dispatch cases, literal settings, and calls. Python files are parsed with the AST and are never imported or executed. The generated overview displays configured provenance fields directly; the dataset inference can use the rest of the app context to explain presentation and runtime behavior. App source hashes are part of the inventory fingerprint, so edits to app behavior invalidate context generated from the older app. Use `--app-dir PATH` to select an app directory explicitly or when the app is stored elsewhere.

For dataset-level analysis, `--dataset-instructions FILE` adds optional UTF-8 operator guidance to the inference prompt. This option requires `--analyze-context`; it can refine the analysis focus and wording but cannot override the required output schema or evidence rules. The instruction text participates in the response-cache key, and its SHA-256 is saved in dataset-analysis provenance. The N1904 notebook exposes the same setting as `DATASET_INSTRUCTIONS`.

Context artifacts also record provider, requested and responding model IDs, and prompt version alongside the inventory hash. The dataset architecture page shows this provenance when available.

See the [complete runtime option reference](install-guide.html#runtime-options) and [Python and notebook example for all five providers](install-guide.html#from-python).

## Optional generated descriptions

[Sign in to OpenRouter and create an API key](https://openrouter.ai/settings/keys). Store it in your local `OPENROUTER_API_KEY` environment variable and supply an OpenRouter model ID accessible to your account:

```sh
doc4cf N1904/tf/1.0.0 site --model openrouter/free
```

Select a chat model supported by the provider and set its environment variable:

| `--provider` | API key |
| --- | --- |
| `openrouter` (default) | `OPENROUTER_API_KEY` |
| `openai` | `OPENAI_API_KEY` |
| `groq` | `GROQ_API_KEY` |
| `gemini` | `GEMINI_API_KEY` |
| `anthropic` (Claude) | `ANTHROPIC_API_KEY` |

For a worked editorial review workflow, see [Try your dataset notes on three features](install-guide.html#editor-notes). Pass UTF-8 editor notes with `--dataset-context FILE` and limit enrichment with `--describe-features lemma,tense,frame`. Each uncached request includes the full notes and one feature profile. Every feature page is built; unselected pages contain corpus data only. Reuse the cache when switching from the trial to the full build.

For a corpus documented with one model, use `--model-attribution overview` to list distinct responding models once on the corpus homepage. Use `none` to omit provider and model names, or `feature` (default) to credit them beside each generated description. Every mode keeps the **Generated description** heading. Changing the display setting reuses the same cached responses.

```sh
doc4cf N1904/tf/1.0.0 site --provider openai --model MODEL_ID --model-attribution overview
```

This sends the corpus title and each feature's profile (including common values) to the selected provider. The CLI sends one request per uncached feature (61 for a complete uncached N1904 build). The OpenRouter example selects the free router; other model choices may incur charges. Generated paragraphs appear separately from source metadata. Successful requests are cached by model, prompt and evidence in `.doc4cf-cache`; rerun after an interrupted request to reuse completed responses. Keys stay in the build process. All three checked-in examples include descriptions generated by free OpenRouter models. The Old Babylonian example uses `nvidia/nemotron-3.5-super-vl:free` for 66 feature descriptions; `volume` remains deterministic. N1904 and DSS retain their existing generated descriptions. The notebooks provide the workflows to rebuild the examples; model enrichment is controlled by each notebook's settings. Each generated paragraph identifies the responding model. The sites can be read offline.

**Data handling.** Feature profiles include sample values from the corpus text. Before using a model, confirm that the corpus licence allows sending excerpts to a third party, and check the provider's data-retention and training terms, which can differ on free endpoints. Use an offline build (omit `--model`) for restricted material.

## Why corpus documentation matters

The [guide to using corpus documentation](query-guide.html) shows how to use observed feature coverage, values, containment and directed edges to write search templates. It includes tested examples for N1904, DSS and Old Babylonian.

## Reading the output

- Feature pages live in `features/<feature-name>.html` and preserve the spelling of the TF filename. For example, `text.tf` produces `features/text.html`, while `text.html` at the corpus root documents text rendering and encoding. Previous `feature-<name>.html` links need updating.
- The feature index covers node, edge and configuration files. Feature pages show populated source-node counts, target-edge counts where applicable, frequent values, and the original metadata.
- The structure browser follows Context-Fabric's large-to-small node-type order and separately reports the declared reference sections. Pick a type or feature and follow a relationship to refocus the graph. The JSON export uses the node dictionary, typed IDs and directed “valid on” relations of [TF_Knowledge_Graph](https://github.com/tonyjurg/TF_Knowledge_Graph). Doc4CF also represents configuration files as `config_feature` nodes and omits the reference export’s per-edge `freqDetail` field.
- Text and encoding shows declared rendering formats, contributing features and up to twelve nodes of each format’s target type rendered through Context-Fabric. Without declared formats it lists populated string fields on slots, ranked by coverage, with samples in slot order. Byte encoding is checked across whole files. Unicode normalization is reported only for the frequent-value sample.

## Example corpora

See the [example methods comparison](example-methods.html) for the inference levels, generated-description coverage, and current notebook defaults for all three examples.

The [three generation notebooks](notebooks/README.md) explain how to rebuild each example, from a pinned corpus revision to the complete static site. They include offline and free OpenRouter options, safe key entry, validation, and an optional publication step. The N1904 notebook uses the [N1904 editorial context](notebooks/contexts/N1904.txt) for enriched descriptions.

### N1904 validation

The example uses the [CenterBLC Nestle 1904 dataset](https://github.com/CenterBLC/N1904), version 1.0.0. It contains 137,779 word slots, ten node types and six rendering formats. Corpus credits appear in each feature's metadata. The upstream license is included with the example.

```sh
python tests/verify_n1904.py N1904/tf/1.0.0 site
```

This project builds on [Doc4TF](https://github.com/tonyjurg/Doc4TF)'s feature-by-feature documentation design and uses [Context-Fabric](https://github.com/Context-Fabric/context-fabric) for corpus access.

### Interactive corpus diagram

Open [the N1904 diagram](examples/N1904/diagram.html) from the overview or structure browser. Select a feature or node type to see its immediate neighbors. Use **Open reference** for its documentation or **Show whole corpus** to restore the overview.

The center column ranks types by the mean number of distinct slots per node, with the slot type last and alphabetical ties. Features are placed around the mean rank of the types on which they have observed values. Each connected type has equal weight. Features with no observed coverage appear at the bottom. This ordering summarizes relative scale; a line represents feature applicability rather than hierarchical containment.


### Dead Sea Scrolls example

The [DSS example](examples/DSS/index.html) uses the base TF corpus version 2.0.4 from [ETCBC/dss at revision 3a9ab5b](https://github.com/ETCBC/dss/tree/3a9ab5b5df4dba72f2179016e8163b61c0a1752d/tf/2.0.4). Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook created the source data. Jarod Jacobs, Martijn Naaijer, and Dirk Roorda converted them. Doc4CF generated the feature statistics, examples, and diagram offline. The dataset is licensed under [CC BY-NC 4.0](examples/DSS/DATA-LICENSE.txt).

```sh
git clone https://github.com/ETCBC/dss.git
git -C dss checkout 3a9ab5b5df4dba72f2179016e8163b61c0a1752d
doc4cf dss/tf/2.0.4 site-dss
```


### Old Babylonian example

The [Old Babylonian letters example](examples/OldBabylonian/index.html) uses the default corpus version 1.0.6 from [Nino-cunei/oldbabylonian at revision cd8ffe8](https://github.com/Nino-cunei/oldbabylonian/tree/cd8ffe826a598af4715fd724387d9834ec1300d8/tf/1.0.6). Dirk Roorda and J. Cale Johnson prepared the corpus from Cuneiform Digital Library Initiative data. The example includes the [upstream license](examples/OldBabylonian/DATA-LICENSE.txt).

```sh
git clone https://github.com/Nino-cunei/oldbabylonian.git
git -C oldbabylonian checkout cd8ffe826a598af4715fd724387d9834ec1300d8
doc4cf oldbabylonian/tf/1.0.6 site-oldbabylonian
```

## License

The Doc4CF software is licensed under the MIT License in [LICENSE](LICENSE). Corpus data and corpus-derived example content are governed by the separate license notice included with each example; the software license does not replace those data licenses.

## Authorship

Doc4CF is authored and maintained by Tony Jurg, with OpenAI Codex credited as an AI coding contributor.

## Tools used

[OpenAI Codex](https://chatgpt.com/codex) has assisted with selected code and documentation changes and with preparing pull requests. Tony Jurg reviews and accepts the changes made with this assistance. Codex-assisted commits use GitHub's co-author trailer, `Co-authored-by: Codex <codex@openai.com>`, when Codex contributed to the committed changes.

## Project website

The rebuild commands above write to separate output directories. To generate a site under `examples/<corpus>/`, add `--project-home ../../index.html` for a project link in each page’s footer. The header logo links to the corpus overview. Rebuilding over a checked-in example without `--model` replaces its enriched feature pages with offline output.

Open [the project homepage](index.html) locally to browse the corpus library. When you are ready to publish:

1. Make the repository public and select **Settings → Pages → Build and deployment → Source → GitHub Actions**.
2. For the first deployment, open **Actions → Deploy documentation to GitHub Pages → Run workflow**, choose **main**, and run it.
3. When the deploy job succeeds, follow its **github-pages** environment link. The expected project URL is `https://tonyjurg.github.io/Doc4CF/`. The homepage links to N1904, DSS, and Old Babylonian under `examples/`.

Subsequent pushes to `main` that change the website, examples, or Pages workflow deploy automatically. While the repository is private, the workflow builds the same site artifact and skips deployment. It publishes the checked-in HTML and its assets without rebuilding the corpora or calling OpenRouter.
