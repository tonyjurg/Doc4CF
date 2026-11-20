# operatorr.tf

[← Corpus index](../index.md)

the ! or x in a !() or x() construction, represented as =, ␣

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The operatorr feature is a node-level feature on sign nodes in the AbB Old Babylonian Cuneiform Text-Fabric corpus. It records the operator character in a !() or x() ATF construction, represented as '=' or a space character (␣). The feature has two distinct values: '=' occurs 117 times and '␣' occurs 5 times, and it is sourced from 122 sign nodes. It belongs to the Sign Status and Condition Flags feature family alongside features such as missing, supplied, uncertain, damage, excised, det, langalt, question, collated, remarkable, flags, operator, and operatoru.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 122 (0.1%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "=" | 117 | 95.9% |
| "␣" | 5 | 4.1% |

## Correlated features

- [operator](operator.md) sign · φ +1.00

- [operatoru](operatoru.md) sign · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | operatorr present when compared feature is present | operatorr present when compared feature is absent |
| --- | --- | --- | --- |
| [operator](operator.md), [operatoru](operatoru.md) | +1.00 | 122 / 122 (100.0%) | 0 / 203,097 (0.0%) |
| [grapheme](grapheme.md), [graphemer](graphemer.md), [graphemeu](graphemeu.md) | +0.20 | 122 / 3,011 (4.1%) | 0 / 200,208 (0.0%) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | the ! or x in a !() or x() construction, represented as =, ␣ |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
