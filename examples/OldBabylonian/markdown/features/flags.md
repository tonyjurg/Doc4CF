# flags.tf

[← Corpus index](../index.md)

sequence of flags after a sign

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The flags feature is a node-level feature on sign nodes that records the sequence of ATF flags appearing after a sign in the transliteration. It has 10 distinct values across 10,498 sign occurrences. Frequent values include the single flags '#', '?', '!', and '*', as well as multi-character combinations such as '#?', '?#', '#!', '!*', '?!*', and '#*'. The feature is part of the sign status and condition flag family, which also includes missing, supplied, uncertain, damage, excised, det, langalt, question, collated, remarkable, operator, operatorr, and operatoru. The precise interpretive rules for ordering or combining multiple flags are not specified.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 10,498 (5.2%) |

## Frequent values

10 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "#" | 9,830 | 93.6% |
| "?" | 421 | 4.0% |
| "#?" | 131 | 1.2% |
| "!" | 91 | 0.9% |
| "*" | 9 | 0.1% |
| "?#" | 7 | 0.1% |
| "#!" | 5 | 0.0% |
| "!*" | 2 | 0.0% |
| "?!*" | 1 | 0.0% |
| "#*" | 1 | 0.0% |

## Correlated features

- [damage](damage.md) sign · φ +0.97

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | flags present when compared feature is present | flags present when compared feature is absent |
| --- | --- | --- | --- |
| [damage](damage.md) | +0.97 | 9,974 / 9,974 (100.0%) | 524 / 193,245 (0.3%) |
| [question](question.md) | +0.23 | 560 / 560 (100.0%) | 9,938 / 202,659 (4.9%) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | sequence of flags after a sign |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
