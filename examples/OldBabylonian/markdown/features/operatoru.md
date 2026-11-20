# operatoru.tf

[← Corpus index](../index.md)

the ! or x in a !() or x() construction, represented as =, ␣

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The operatoru feature is a node-level feature scoped to signs. Its source description characterizes it as the ! or x in a !() or x() construction, represented as = or ␣ (space). In the corpus it occurs on 122 sign nodes, with 117 occurrences of = and 5 of ␣, and its targets field is empty. It belongs to the sign status and condition flag family alongside operator and operatorr. The inventory does not state normalization rules between these layers, whether ␣ denotes a literal space character, or the precise ATF semantics of the !() and x() constructions.\n

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

- [operatorr](operatorr.md) sign · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | operatoru present when compared feature is present | operatoru present when compared feature is absent |
| --- | --- | --- | --- |
| [operator](operator.md), [operatorr](operatorr.md) | +1.00 | 122 / 122 (100.0%) | 0 / 203,097 (0.0%) |
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
