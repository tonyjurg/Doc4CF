# ln.tf

[← Corpus index](../index.md)

ATF line number of a numbered line, without prime

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The feature ln stores the ATF line number of a numbered line, excluding any prime mark. It is a node feature sourced from line nodes, with 26,406 observed sources and 39 distinct values. Frequent values begin at 1 (2,764 occurrences) and continue through 12 (1,019 occurrences), reflecting sequential line numbering. The supplied context indicates that ln overlaps conceptually with lnno, which may carry primes or column numbers, but the inventory provides no disambiguation or co-occurrence rules between the two features.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [line](../../structure.html#type-line) | 26,406 (96.5%) |

## Frequent values

39 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 2,764 | 10.5% |
| 2 | 2,623 | 9.9% |
| 3 | 2,392 | 9.1% |
| 4 | 2,245 | 8.5% |
| 5 | 2,146 | 8.1% |
| 6 | 2,042 | 7.7% |
| 7 | 1,923 | 7.3% |
| 8 | 1,782 | 6.7% |
| 9 | 1,632 | 6.2% |
| 10 | 1,449 | 5.5% |
| 11 | 1,241 | 4.7% |
| 12 | 1,019 | 3.9% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### line nodes

| Compared feature(s) | φ | ln present when compared feature is present | ln present when compared feature is absent |
| --- | --- | --- | --- |
| [lnc](lnc.md) | -1.00 | 0 / 969 (0.0%) | 26,406 / 26,406 (100.0%) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | ATF line number of a numbered line, without prime |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
