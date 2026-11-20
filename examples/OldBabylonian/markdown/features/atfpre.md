# atfpre.tf

[← Corpus index](../index.md)

atf of cluster openings at sign

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The atfpre feature records ATF cluster openings at sign nodes in the AbB Old Babylonian Cuneiform corpus. It is a node-level feature sourced from sign nodes, observed on 21,769 of the corpus's 203,219 signs. The feature captures ATF markup that precedes a sign within a cluster, such as bracket or brace openings. It has 19 distinct values. Frequent opening values include '[' (6,942), '_' (6,405), '{' (5,548), '_{' (1,009), '(' (927), '[(' (256), '<' (224), '[{' (202), '_[' (110), '<<' (68), '_[' (38), and '[_{' (17). It belongs to the sign_surroundings family alongside atfpost and afteru.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 21,769 (10.7%) |

## Frequent values

19 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "[" | 6,942 | 31.9% |
| "_" | 6,405 | 29.4% |
| "{" | 5,548 | 25.5% |
| "_{" | 1,009 | 4.6% |
| "(" | 927 | 4.3% |
| "[(" | 256 | 1.2% |
| "<" | 224 | 1.0% |
| "[{" | 202 | 0.9% |
| "[_" | 110 | 0.5% |
| "<<" | 68 | 0.3% |
| "_[" | 38 | 0.2% |
| "[_{" | 17 | 0.1% |

## Correlated features

- [atfpost](atfpost.md) sign · φ +0.60

- [det](det.md) sign · φ +0.54

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | atfpre present when compared feature is present | atfpre present when compared feature is absent |
| --- | --- | --- | --- |
| [atfpost](atfpost.md) | +0.60 | 14,118 / 21,969 (64.3%) | 7,651 / 181,250 (4.2%) |
| [det](det.md) | +0.54 | 6,794 / 6,796 (100.0%) | 14,975 / 196,423 (7.6%) |
| [missing](missing.md) | +0.44 | 8,662 / 14,391 (60.2%) | 13,107 / 188,828 (6.9%) |
| [after](after.md) | -0.22 | 12,891 / 169,025 (7.6%) | 8,878 / 34,194 (26.0%) |
| [reading](reading.md), [readingr](readingr.md), [readingu](readingu.md) | -0.12 | 20,311 / 199,359 (10.2%) | 1,458 / 3,860 (37.8%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [text-orig-full rendering format](../../text.html#format-15716cf41c30) | `{atfpre}{atf}{atfpost}{after}` Uses: [atfpre](atfpre.md), [atf](atf.md), [atfpost](atfpost.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | atf of cluster openings at sign |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
