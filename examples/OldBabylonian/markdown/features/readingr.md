# readingr.tf

[← Corpus index](../index.md)

reading of a sign using non-ascii characters

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The readingr feature records the reading of a cuneiform sign using non-ASCII characters, forming the non-ASCII layer of the sign_renderings family alongside reading and readingu. It is a node feature sourced from 199,359 sign nodes and exhibits 746 distinct values. Frequent readings include a, ma, x, na, i, ša, šu, d, li, am, ta, and ka. This layer sits between the ASCII reading and cuneiform-Unicode readingu variants, though the inventory does not specify normalization or conversion rules between these parallel representations.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 199,359 (98.1%) |

## Frequent values

746 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "a" | 11,672 | 5.9% |
| "ma" | 11,449 | 5.7% |
| "x" | 8,729 | 4.4% |
| "na" | 8,533 | 4.3% |
| "i" | 4,947 | 2.5% |
| "ša" | 4,737 | 2.4% |
| "šu" | 4,500 | 2.3% |
| "d" | 4,078 | 2.0% |
| "li" | 3,892 | 2.0% |
| "am" | 3,839 | 1.9% |
| "ta" | 3,431 | 1.7% |
| "ka" | 3,277 | 1.6% |

## Correlated features

- [reading](reading.md) sign · φ +1.00

- [readingu](readingu.md) sign · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | readingr present when compared feature is present | readingr present when compared feature is absent |
| --- | --- | --- | --- |
| [reading](reading.md), [readingu](readingu.md) | +1.00 | 199,359 / 199,359 (100.0%) | 0 / 3,860 (0.0%) |
| [afterr](afterr.md) | +0.18 | 174,174 / 175,844 (99.1%) | 25,185 / 27,375 (92.0%) |
| [after](after.md) | +0.15 | 167,369 / 169,025 (99.0%) | 31,990 / 34,194 (93.6%) |
| [grapheme](grapheme.md), [graphemer](graphemer.md), [graphemeu](graphemeu.md) | -0.84 | 122 / 3,011 (4.1%) | 199,237 / 200,208 (99.5%) |
| [comment](comment.md) | -0.50 | 0 / 971 (0.0%) | 199,359 / 202,248 (98.6%) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | reading of a sign using non-ascii characters |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
