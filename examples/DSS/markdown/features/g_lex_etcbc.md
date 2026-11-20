# g_lex_etcbc.tf

[← Corpus index](../index.md)

The consonantal representation of the realised lexeme of a word occurrence in BHSA transliteration

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 56,891 (11.4%) |

## Frequent values

3,372 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "W" | 6,739 | 11.8% |
| "L" | 3,302 | 5.8% |
| "B" | 2,883 | 5.1% |
| "H" | 2,835 | 5.0% |
| "KWL" | 1,097 | 1.9% |
| "M" | 954 | 1.7% |
| "LW>" | 847 | 1.5% |
| "<L" | 689 | 1.2% |
| ">T" | 670 | 1.2% |
| ">CR" | 638 | 1.1% |
| "K" | 580 | 1.0% |
| ">L" | 570 | 1.0% |

## Correlated features

- [g_cons](g_cons.md) word · φ +1.00

- [morph_etcbc](morph_etcbc.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | g_lex_etcbc present when compared feature is present | g_lex_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [g_cons](g_cons.md) | +1.00 | 56,891 / 56,931 (99.9%) | 0 / 444,064 (0.0%) |
| [morph_etcbc](morph_etcbc.md) | +1.00 | 56,891 / 56,934 (99.9%) | 0 / 444,061 (0.0%) |
| [g_pfm_etcbc](g_pfm_etcbc.md) | +0.25 | 4,033 / 4,033 (100.0%) | 52,858 / 496,962 (10.6%) |
| [uvf_etcbc](uvf_etcbc.md) | -0.97 | 238 / 441,611 (0.1%) | 56,653 / 59,384 (95.4%) |
| [g_nme_etcbc](g_nme_etcbc.md) | -0.87 | 9,708 / 451,081 (2.2%) | 47,183 / 49,914 (94.5%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:08+00:00Z |
| description | The consonantal representation of the realised lexeme of a word occurrence in BHSA transliteration |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
