# lex_etcbc.tf

[← Corpus index](../index.md)

The consonantal representation of the lexeme of a word occurrence in BHSA transliteration

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 498,307 (99.5%) |

## Frequent values

5,479 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "" | 75,392 | 15.1% |
| "W" | 46,390 | 9.3% |
| "L" | 22,373 | 4.5% |
| "B" | 20,268 | 4.1% |
| "H" | 18,929 | 3.8% |
| "KL/" | 8,495 | 1.7% |
| ">T" | 7,699 | 1.5% |
| "MN" | 7,447 | 1.5% |
| "L>" | 5,988 | 1.2% |
| "<L" | 5,874 | 1.2% |
| ">CR" | 5,390 | 1.1% |
| "MLK/" | 5,194 | 1.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | lex_etcbc present when compared feature is present | lex_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [g_nme_etcbc](g_nme_etcbc.md) | +0.22 | 451,081 / 451,081 (100.0%) | 47,226 / 49,914 (94.6%) |
| [lex](lex.md), [lexe](lexe.md), [lexo](lexo.md) | +0.22 | 470,203 / 470,845 (99.9%) | 28,104 / 30,150 (93.2%) |
| [morpho](morpho.md), [sp](sp.md) | +0.22 | 470,203 / 470,845 (99.9%) | 28,104 / 30,150 (93.2%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -0.22 | 27,892 / 29,927 (93.2%) | 470,415 / 471,068 (99.9%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:10+00:00Z |
| description | The consonantal representation of the lexeme of a word occurrence in BHSA transliteration |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
