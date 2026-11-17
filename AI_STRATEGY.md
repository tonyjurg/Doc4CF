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

Successful analysis and description responses are cached using their relevant corpus evidence, context, prompt version, provider, and model configuration. Reruns reuse unchanged results and keep completed work after an interrupted build. Truncated completions are retried with a larger output allowance. Structurally valid JSON that fails local evidence validation can receive up to two minimal correction requests before the build reports the failure.

The `context_manifest.json` and `context_review.json` outputs make the inputs and review status visible. Context artifact provenance records provider, requested and responding model IDs when available, and prompt version. Model attribution on generated pages can show a model beside each description, summarize models on the overview, or be omitted.

## Current examples

The checked-in N1904, DSS, and Old Babylonian sites demonstrate generated feature descriptions alongside deterministic corpus measurements. The Old Babylonian context-first example uses `nvidia/nemotron-3.5-super-vl:free`; the current generated set has model descriptions for 66 of 67 features, with `volume` remaining deterministic. Model descriptions are cached locally during generation, and the checked-in site does not require a model key or network access to browse.

The three notebooks under `notebooks/` are the runnable workflows for rebuilding examples from their pinned upstream corpus revisions. Their current settings determine whether a run is offline, context-only, or enriched with per-feature model descriptions.
