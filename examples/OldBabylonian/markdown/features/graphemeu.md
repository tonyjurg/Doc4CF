# graphemeu.tf

[← Corpus index](../index.md)

grapheme of a sign using cuneiform unicode characters

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The graphemeu feature records the grapheme of a sign using cuneiform Unicode characters. It is a node feature sourced from sign nodes (3011 targets) and belongs to the sign_renderings feature family alongside reading, readingr, readingu, grapheme, and graphemer. The feature has 131 distinct values; frequent cuneiform Unicode values include 𒀴 (119), 𒃷 (102), 𒁉 (54), 𒁲 (48), 𒆪 (46), 𒀵 (46), 𒆠 (42), 𒌓 (35), 𒉌 (33), 𒍣 (31), and 𒉿 (29). It is inferred to be a Unicode variant of graphemer. The precise semantic boundary between graphemeu and related layers such as reading, sym, and atf is not specified.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 3,011 (1.5%) |

## Frequent values

131 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "..." | 1,617 | 53.7% |
| "𒀴" | 119 | 4.0% |
| "𒃷" | 102 | 3.4% |
| "𒁉" | 54 | 1.8% |
| "𒁲" | 48 | 1.6% |
| "𒆪" | 46 | 1.5% |
| "𒀵" | 46 | 1.5% |
| "𒆠" | 42 | 1.4% |
| "𒌓" | 35 | 1.2% |
| "𒉌" | 33 | 1.1% |
| "𒍣" | 31 | 1.0% |
| "𒉿" | 29 | 1.0% |

## Correlated features

- [grapheme](grapheme.md) sign · φ +1.00

- [graphemer](graphemer.md) sign · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | graphemeu present when compared feature is present | graphemeu present when compared feature is absent |
| --- | --- | --- | --- |
| [grapheme](grapheme.md), [graphemer](graphemer.md) | +1.00 | 3,011 / 3,011 (100.0%) | 0 / 200,208 (0.0%) |
| [missing](missing.md) | +0.22 | 1,623 / 14,391 (11.3%) | 1,388 / 188,828 (0.7%) |
| [operator](operator.md), [operatorr](operatorr.md), [operatoru](operatoru.md) | +0.20 | 122 / 122 (100.0%) | 2,889 / 203,097 (1.4%) |
| [reading](reading.md), [readingr](readingr.md), [readingu](readingu.md) | -0.84 | 122 / 199,359 (0.1%) | 2,889 / 3,860 (74.8%) |
| [afterr](afterr.md) | -0.10 | 1,764 / 175,844 (1.0%) | 1,247 / 27,375 (4.6%) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | grapheme of a sign using cuneiform unicode characters |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
