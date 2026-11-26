# Doc4CF AI enrichment

## Purpose and boundaries

AI enrichment is an optional interpretation layer over Doc4CF's deterministic corpus reference. Doc4CF reads the corpus locally to measure feature metadata, node coverage, values, examples, containment, and relationships. A language model can summarize and interpret this evidence, but its prose remains separate from source metadata and is not treated as verified corpus fact by default.

The workflow is designed to remain useful without a model. Inventory export, deterministic site generation, browsing, and search work offline. API keys are read by the build process and are not written into generated pages. Corpus data and its license remain the responsibility of the corpus publisher.

## Current workflow

1. **Measure the corpus.** `doc4cf CORPUS --export-inventory FILE` exports a deterministic, versioned inventory with corpus identity, a content hash, feature metadata, observed coverage, frequent values, and examples. This stage makes no model request.
2. **Create reusable context.** `doc4cf CORPUS --analyze-context DIR` writes the inventory and dataset, feature-family, and feature-relationship artifacts. Dataset and family analysis can use separately selected models. Artifacts are inspectable JSON files with schemas, evidence paths, status labels, and provenance.
3. **Review the context.** Inspect the generated dataset profile, families, relationships, evidence, ambiguities, and review flags. The artifacts are explicit inputs to later builds; they are not hidden conversation state.
4. **Generate descriptions.** A site build using `--context-dir DIR` supplies the dataset context and relevant family/relationship context together with measured feature evidence. `--dataset-context FILE` can add editorial guidance. `--describe-features` can limit model requests while still building every feature page. `--targeted-evidence` optionally lets the model request a bounded set of extra values or examples, which Doc4CF then retrieves from the corpus itself.
5. **Validate and inspect.** Responses use structured JSON where supported and are validated locally. Feature and value references must match the current inventory. Stale context is rejected. `--context-pages` adds dataset, relationship, and review pages; `context_review.json` records processed descriptions, affected inputs, and context flags.

The optional `--markdown` output mirrors Doc4TF's lightweight index-and-feature-file structure. It carries the same measured summaries and any selected, validated model descriptions into Markdown, with source text kept separate from inferred prose and model attribution retained. Exporting this format reuses the site build's responses rather than creating additional model calls. Keeping each feature's material in its own file also makes it straightforward to add further calculated fields and clearly labeled interpretations over time.

For exact commands and options, see the [install guide](install-guide.html#runtime-options) and the [README](README.md). The corpus notebooks demonstrate pinned data revisions, local caches, optional model enrichment, validation, and publication workflows.

## Evidence and safety rules

- Corpus observations are authoritative for measured claims. Descriptions preserve the source feature description and distinguish observations from interpretation.
- Model input is treated as untrusted data, not as instructions. Models must use supplied evidence, preserve identifiers exactly, and identify uncertainty instead of inventing facts.
- Context artifacts label claims as verified, inferred, or needing review and retain evidence paths. Conceptual feature families are kept separate from observed Text-Fabric structure.
- Generated references are checked against the corpus inventory. Unsupported names or values trigger bounded correction attempts; invalid responses are not cached as successful results or rendered as accepted descriptions.
- A flagged contradiction, inconsistency, or missing evidence is surfaced for human review. Model output does not silently rewrite source metadata or reviewed context artifacts.
- Descriptions and context analysis require editorial review before publication. Model output can be incomplete or wrong even when it passes structural validation.

## Reliability and reuse

OpenRouter is the default provider. OpenAI, Anthropic, Gemini, and Groq are also supported. Provider and model choices are configurable; context analysis and feature descriptions can use different models. Availability, limits, output quality, and structured-output support vary by provider and model.

Successful analysis and description responses are cached using their relevant corpus evidence, context, prompt version, provider, and model configuration. Reruns reuse unchanged results and keep completed work after an interrupted build. Uncached context analysis and feature descriptions with the configured free Nemotron model start with larger completion allowances to reduce avoidable truncation retries while preserving existing cache entries. Truncated completions are retried with a larger output allowance. Structurally valid JSON that fails local evidence validation can receive up to two minimal correction requests before the build reports the failure.

The `context_manifest.json` and `context_review.json` outputs make the inputs and review status visible. Context artifact provenance records provider, requested and responding model IDs when available, and prompt version. Model attribution on generated pages can show a model beside each description, summarize models on the overview, or be omitted.

## Current examples

The checked-in sites include AI-assisted feature descriptions alongside deterministic corpus measurements: N1904 has 61 of 61, DSS has 79 of 79, and Old Babylonian has 66 of 67, with `volume` remaining deterministic. N1904 and DSS include complete Markdown companions. See the [example methods comparison](example-methods.html) for measured coverage and the inference layers visible in each site. The checked-in sites do not require a model key or network access to browse.

The three notebooks under `notebooks/` are the runnable workflows for rebuilding examples from their pinned upstream corpus revisions. Their current settings determine whether a run is offline, context-only, or enriched with per-feature model descriptions.

The N1904 reference now has model-assisted descriptions for all 61 features. Its workflow applies source-cited editorial clarifications for `ln` and `verse`, distinguishing a starting-verse annotation from containment. Reviewed prose is labeled separately from an unedited inference, while the source metadata, raw model cache, and original uncertainty flags remain available for traceability.
