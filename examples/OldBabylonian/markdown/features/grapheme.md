# grapheme.tf

[← Corpus index](../index.md)

grapheme of a sign

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The grapheme feature records the grapheme of a sign in the AbB Old Babylonian Cuneiform Text-Fabric corpus. It is a node feature attached to sign nodes, with 153 distinct values observed. Frequent values include ellipsis (1,617), ARAD (119), GAN2 (102), BI (54), DI (48), KU (46), ARAD2 (46), KI (42), NI (33), UD (31), and ZI (30). The feature belongs to the sign rendering layers alongside reading, though the precise semantic boundary between grapheme, reading, sym, and atf is unspecified in the inventory.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 3,011 (1.5%) |

## Frequent values

153 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "..." | 1,617 | 53.7% |
| "ARAD" | 119 | 4.0% |
| "GAN2" | 102 | 3.4% |
| "BI" | 54 | 1.8% |
| "DI" | 48 | 1.6% |
| "KU" | 46 | 1.5% |
| "ARAD2" | 46 | 1.5% |
| "KI" | 42 | 1.4% |
| "NI" | 33 | 1.1% |
| "UD" | 31 | 1.0% |
| "ZI" | 30 | 1.0% |
| "GA" | 29 | 1.0% |

## Correlated features

- [graphemer](graphemer.md) sign · φ +1.00

- [graphemeu](graphemeu.md) sign · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | grapheme present when compared feature is present | grapheme present when compared feature is absent |
| --- | --- | --- | --- |
| [graphemer](graphemer.md), [graphemeu](graphemeu.md) | +1.00 | 3,011 / 3,011 (100.0%) | 0 / 200,208 (0.0%) |
| [missing](missing.md) | +0.22 | 1,623 / 14,391 (11.3%) | 1,388 / 188,828 (0.7%) |
| [operator](operator.md), [operatorr](operatorr.md), [operatoru](operatoru.md) | +0.20 | 122 / 122 (100.0%) | 2,889 / 203,097 (1.4%) |
| [reading](reading.md), [readingr](readingr.md), [readingu](readingu.md) | -0.84 | 122 / 199,359 (0.1%) | 2,889 / 3,860 (74.8%) |
| [afterr](afterr.md) | -0.10 | 1,764 / 175,844 (1.0%) | 1,247 / 27,375 (4.6%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | grapheme of a sign |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
