# atfpost.tf

[← Corpus index](../index.md)

atf of cluster closings at sign

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The atfpost feature records the ATF text that closes a cluster at a sign node in the AbB Old Babylonian Cuneiform corpus. It is a node feature sourced on sign, with 20 distinct values observed. Frequent values include '_' (7,226), '}' (6,385), ']' (6,330), ')]' (918), ')' (264), '>' (222), '}_' (216), '}]' (179), '_]' (86), '>>' (68), ']_', 53), and '_}' (6). It participates in the text-orig-full rendering format ({atfpre}{atf}{atfpost}{after}) alongside atfpre, atf, and after. The feature family is Sign Surroundings and Cluster Boundaries, which also includes atfpre and afteru.\n

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 21,969 (10.8%) |

## Frequent values

20 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "_" | 7,226 | 32.9% |
| "}" | 6,385 | 29.1% |
| "]" | 6,330 | 28.8% |
| ")]" | 918 | 4.2% |
| ")" | 264 | 1.2% |
| ">" | 222 | 1.0% |
| "}_" | 216 | 1.0% |
| "}]" | 179 | 0.8% |
| "_]" | 86 | 0.4% |
| ">>" | 68 | 0.3% |
| "]_" | 53 | 0.2% |
| "_}" | 6 | 0.0% |

## Correlated features

- [atfpre](atfpre.md) sign · φ +0.60

- [det](det.md) sign · φ +0.53

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | atfpost present when compared feature is present | atfpost present when compared feature is absent |
| --- | --- | --- | --- |
| [atfpre](atfpre.md) | +0.60 | 14,118 / 21,769 (64.9%) | 7,851 / 181,450 (4.3%) |
| [det](det.md) | +0.53 | 6,794 / 6,796 (100.0%) | 15,175 / 196,423 (7.7%) |
| [missing](missing.md) | +0.40 | 8,092 / 14,391 (56.2%) | 13,877 / 188,828 (7.3%) |
| [after](after.md) | -0.31 | 10,842 / 169,025 (6.4%) | 11,127 / 34,194 (32.5%) |
| [reading](reading.md), [readingr](readingr.md), [readingu](readingu.md) | -0.14 | 20,360 / 199,359 (10.2%) | 1,609 / 3,860 (41.7%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [text-orig-full rendering format](../../text.html#format-15716cf41c30) | `{atfpre}{atf}{atfpost}{after}` Uses: [atfpre](atfpre.md), [atf](atf.md), [atfpost](atfpost.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | atf of cluster closings at sign |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:07Z |
