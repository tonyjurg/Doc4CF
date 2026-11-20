# operator.tf

[← Corpus index](../index.md)

the ! or x in a !() or x() construction

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The `operator` feature is a node-level sign feature in the AbB Old Babylonian Cuneiform corpus that records the operator character in ATF `!()` or `x()` constructions attached to signs. It is attested on 122 sign nodes and has exactly two distinct values: `!` with 117 occurrences and `x` with 5 occurrences. The sign status flags family also lists parallel features `operatorr` and `operatoru`, tentatively indicating ASCII, non-ASCII, and cuneiform-Unicode rendering layers, but the inventory provides no normalization or conversion rules between them. The feature's precise semantic relationship to other sign-condition features—`missing`, `supplied`, `uncertain`, `damage`, `excised`, `det`, `langalt`, `question`, `collated`, `remarkable`, and `flags`—remains unspecified.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 122 (0.1%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "!" | 117 | 95.9% |
| "x" | 5 | 4.1% |

## Correlated features

- [operatorr](operatorr.md) sign · φ +1.00

- [operatoru](operatoru.md) sign · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | operator present when compared feature is present | operator present when compared feature is absent |
| --- | --- | --- | --- |
| [operatorr](operatorr.md), [operatoru](operatoru.md) | +1.00 | 122 / 122 (100.0%) | 0 / 203,097 (0.0%) |
| [grapheme](grapheme.md), [graphemer](graphemer.md), [graphemeu](graphemeu.md) | +0.20 | 122 / 3,011 (4.1%) | 0 / 200,208 (0.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | the ! or x in a !() or x() construction |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
