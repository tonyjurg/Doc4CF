# docnumber.tf

[← Corpus index](../index.md)

number of a document within a collection-volume

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The docnumber feature is a node-level feature on documents in the AbB Old Babylonian Cuneiform corpus. It records the number of a document within a collection-volume, as stated in the feature description. The feature has 312 distinct values and is sourced from 1,202 documents. Frequent values include "001" and "003" (10 occurrences each), "002" through "012" (8-9 occurrences each). It belongs to the Document Identity and Provenance feature family alongside collection, volume, ARK, pnumber, museumcode, docnote, excavation, srcfile, srcLn, and srcLnNum. Coverage is incomplete: 1,202 of 1,285 documents have a docnumber value, leaving 83 documents without one; whether these are truly absent or unparsed is unspecified.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [document](../../structure.html#type-document) | 1,202 (93.5%) |

## Frequent values

312 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "001" | 10 | 0.8% |
| "003" | 10 | 0.8% |
| "002" | 9 | 0.7% |
| "004" | 9 | 0.7% |
| "005" | 9 | 0.7% |
| "006" | 9 | 0.7% |
| "007" | 9 | 0.7% |
| "008" | 9 | 0.7% |
| "009" | 9 | 0.7% |
| "010" | 8 | 0.7% |
| "011" | 8 | 0.7% |
| "012" | 8 | 0.7% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### document nodes

| Compared feature(s) | φ | docnumber present when compared feature is present | docnumber present when compared feature is absent |
| --- | --- | --- | --- |
| [ARK](ARK.md) | -0.19 | 770 / 853 (90.3%) | 432 / 432 (100.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.document.featuresBare` | collection volume docnumber docnote |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | number of a document within a collection-volume |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
