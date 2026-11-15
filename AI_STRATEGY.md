# Doc4CF AI enrichment strategy

## Purpose

AI enrichment is an optional layer over Doc4CF's deterministic corpus reference. The corpus remains the source of observed facts: feature names, metadata, node coverage, value frequencies, examples, and Text-Fabric structure are extracted locally. A model may interpret that evidence, but generated interpretations stay visibly separate from source metadata and are never presented as verified facts without evidence.

OpenRouter is the recommended default route, with the existing OpenAI, Anthropic, Gemini, and Groq providers retained. Builds without a model remain fully offline. API keys stay in the build process; generated sites do not need a key or network access.

## Enrichment flow

1. **Extract evidence locally.** Build a compact, deterministic inventory for the complete dataset. Keep actual Text-Fabric containment separate from conceptual feature families. Include metadata, kind, observed node types, value type, distinct and frequent values, and selected examples. Record corpus identity/version and a content hash.
2. **Interpret the dataset.** Use the inventory and dataset-level metadata to propose a dataset profile, annotation conventions, feature families, and cross-feature relationships. Mark each interpretation as verified, inferred, or needing review, and retain its supporting evidence. Ask the model to identify missing evidence rather than silently guessing.
3. **Persist reviewable context.** Store separate, versioned `dataset_context.json`, `feature_families.json`, and `feature_relationships.json` artifacts. These are inspectable files, not hidden chat history. Context generation is an explicit command and can be reviewed or rerun independently.
4. **Enrich individual features.** Compose each request from global context, only the relevant family and relationships, deterministic feature evidence, and explicit output/evidence rules. Preserve human-authored descriptions as authoritative source material. Support a short feature-page description and, later, optional extended Markdown.
5. **Validate and export.** Check machine-readable intermediate responses against a schema and validate all mentioned feature/value references against the inventory. Keep claims and uncertainty distinguishable. Invalid or unsupported outputs are flagged; they do not overwrite source metadata. Export accepted descriptions separately into the generated reference.

## Reliability and reuse

- Cache dataset analysis by corpus version/content hash, inventory, prompt version, and model configuration.
- Cache each feature result by the same relevant context plus its evidence, prompt version, and model configuration. Reuse unchanged results on ordinary reruns.
- Retry transient errors and honor rate-limit responses; retain completed cache entries if a run stops.
- Request structured JSON for context artifacts where the endpoint/model supports it, then validate locally regardless. Treat provider support as variable and fail clearly on malformed output.
- Use low-temperature settings for consistent documentation. Keep global-analysis and feature-description model settings independently configurable.
- Never promote inferred relationships to authoritative corpus facts automatically. A discovered contradiction should mark context for review and identify affected feature results.
- Keep deterministic feature statistics and documentation usable when AI is disabled or unavailable.

## Proposed independent PRs

Each PR should deliver a useful capability on its own and preserve the offline path. Later PRs can build on the stable artifact formats established earlier.

### PR 1 — Deterministic inventory and artifact contract (implemented)

The `--export-inventory FILE` command exports a local-only inventory with corpus identity/version, content hash, feature metadata and measured profiles. Versioned JSON Schemas for the inventory, dataset context, feature families, and feature relationships live under `doc4cf/schemas/`; interpretations carry evidence/status fields. No model calls or site generation are involved.

### PR 2 — Dataset and family context analysis (implemented)

The explicit `--analyze-context DIR` command writes the inventory and three context artifacts without building the HTML site. `--context-model` and `--family-model` allow separate model selection. JSON mode is requested from compatible endpoints and all results are validated locally before artifact export. Valid analysis responses are resumably cached by full inventory, provider, model, and prompt version; malformed or structurally invalid responses are not cached.

### PR 3 — Context-aware feature descriptions and validation (implemented)

Normal feature enrichment can consume the saved artifacts with `--context-dir`, passing global context and only the relevant family/relationships alongside local feature evidence. It preserves source descriptions as authoritative input, returns structured JSON with declared feature/value references and uncertainties, and validates references against the current corpus before caching or rendering. A stale inventory hash is rejected. Omitting context artifacts retains the existing feature-only enrichment flow.

### PR 4 — Incremental review and supplementary documentation (implemented)

The build writes a context manifest and `context_review.json`, compares dataset/family/relationship/evidence/prompt/model inputs per feature, and reports descriptions whose inputs changed. Versioned schemas for the manifest and review report are in `doc4cf/schemas/`. Context-aware feature responses can flag contradictions, inconsistencies, and missing evidence; the build reports these without changing the reusable context artifacts. Cache keys keep unchanged feature requests reusable. `--context-pages` adds optional dataset architecture/glossary, relationship index, and review pages linked from the overview. Pages label model interpretations and show supplied evidence paths.

## Current implementation

Today Doc4CF supports optional per-feature descriptions through OpenRouter by default, plus OpenAI, Anthropic, Gemini, and Groq. It sends a feature profile and optional editor notes, caches completed responses, supports selecting features for enrichment, and leaves deterministic site generation available without a model. The staged PRs above extend that feature-by-feature flow into reusable dataset-level context; they do not replace it.
