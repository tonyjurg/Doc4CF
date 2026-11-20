# readingu.tf

[← Corpus index](../index.md)

reading of a sign using cuneiform unicode characters

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The readingu feature records the reading of a sign using cuneiform Unicode characters. It is a node-level feature sourced from sign nodes, with 199,359 attested sign sources and 362 distinct values. Frequent values include 𒀀 (11,702), 𒈠 (11,449), x (8,729), 𒈾 (8,533), 𒀭 (5,982), 𒄿 (4,948), 𒆠 (4,823), 𒊭 (4,737), 𒋗 (4,500), 𒉌 (4,312), 𒇷 (4,140), and 𒄠 (3,839). It belongs to the sign_renderings feature family alongside reading, readingr, grapheme, graphemer, and graphemeu as ASCII, non-ASCII, and cuneiform Unicode rendering layers.\n

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 199,359 (98.1%) |

## Frequent values

362 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "𒀀" | 11,702 | 5.9% |
| "𒈠" | 11,449 | 5.7% |
| "x" | 8,729 | 4.4% |
| "𒈾" | 8,533 | 4.3% |
| "𒀭" | 5,982 | 3.0% |
| "𒄿" | 4,948 | 2.5% |
| "𒆠" | 4,823 | 2.4% |
| "𒊭" | 4,737 | 2.4% |
| "𒋗" | 4,500 | 2.3% |
| "𒉌" | 4,312 | 2.2% |
| "𒇷" | 4,140 | 2.1% |
| "𒄠" | 3,839 | 1.9% |

## Correlated features

- [reading](reading.md) sign · φ +1.00

- [readingr](readingr.md) sign · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | readingu present when compared feature is present | readingu present when compared feature is absent |
| --- | --- | --- | --- |
| [reading](reading.md), [readingr](readingr.md) | +1.00 | 199,359 / 199,359 (100.0%) | 0 / 3,860 (0.0%) |
| [afterr](afterr.md) | +0.18 | 174,174 / 175,844 (99.1%) | 25,185 / 27,375 (92.0%) |
| [after](after.md) | +0.15 | 167,369 / 169,025 (99.0%) | 31,990 / 34,194 (93.6%) |
| [grapheme](grapheme.md), [graphemer](graphemer.md), [graphemeu](graphemeu.md) | -0.84 | 122 / 3,011 (4.1%) | 199,237 / 200,208 (99.5%) |
| [comment](comment.md) | -0.50 | 0 / 971 (0.0%) | 199,359 / 202,248 (98.6%) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | reading of a sign using cuneiform unicode characters |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
