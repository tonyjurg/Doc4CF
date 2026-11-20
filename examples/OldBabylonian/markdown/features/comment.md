# comment.tf

[← Corpus index](../index.md)

$ comment to line or inline comment to slot ($ and $)

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The comment feature is a node-level annotation in the AbB Old Babylonian Cuneiform corpus that records comments attached to signs or lines, grouped with the line-level remarks feature under Comments and Remarks. It is sourced from sign nodes with 971 observed targets and has 57 distinct values. Frequent values include "blank space" (256), "rest broken" (218), "beginning broken" (179), "single ruling" (163), "broken" (36), "illegible" (11), "rest blank" (9), "beginning destroyed" (7), "2 lines broken" (6), "2-3 lines broken" (5), "rest missing" (5), and "(uninscribed)" (5). The source description reads "$ comment to line or inline comment to slot ($ and $)", tentatively suggesting ATF dollar-sign commentary delimiters.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 971 (0.5%) |

## Frequent values

57 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "blank space" | 256 | 26.4% |
| "rest broken" | 218 | 22.5% |
| "beginning broken" | 179 | 18.4% |
| "single ruling" | 163 | 16.8% |
| "broken" | 36 | 3.7% |
| "illegible" | 11 | 1.1% |
| "rest blank" | 9 | 0.9% |
| "beginning destroyed" | 7 | 0.7% |
| "2 lines broken" | 6 | 0.6% |
| "rest missing" | 5 | 0.5% |
| "2-3 lines broken" | 5 | 0.5% |
| "(uninscribed)" | 5 | 0.5% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | comment present when compared feature is present | comment present when compared feature is absent |
| --- | --- | --- | --- |
| [reading](reading.md), [readingr](readingr.md), [readingu](readingu.md) | -0.50 | 0 / 199,359 (0.0%) | 971 / 3,860 (25.2%) |
| [afterr](afterr.md) | -0.18 | 2 / 175,844 (0.0%) | 969 / 27,375 (3.5%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | $ comment to line or inline comment to slot ($ and $) |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
