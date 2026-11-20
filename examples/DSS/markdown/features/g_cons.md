# g_cons.tf

[← Corpus index](../index.md)

The consonantal representation of a word or sign in BHSA transliteration.

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 56,931 (11.4%) |

## Frequent values

8,971 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "W" | 6,738 | 11.8% |
| "L" | 2,836 | 5.0% |
| "H" | 2,836 | 5.0% |
| "B" | 2,611 | 4.6% |
| "KWL" | 1,038 | 1.8% |
| "M" | 912 | 1.6% |
| "LW>" | 857 | 1.5% |
| "<L" | 659 | 1.2% |
| ">CR" | 627 | 1.1% |
| ">T" | 616 | 1.1% |
| "K" | 561 | 1.0% |
| "JHWH" | 531 | 0.9% |

## Correlated features

- [morph_etcbc](morph_etcbc.md) word · φ +1.00

- [g_lex_etcbc](g_lex_etcbc.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | g_cons present when compared feature is present | g_cons present when compared feature is absent |
| --- | --- | --- | --- |
| [morph_etcbc](morph_etcbc.md) | +1.00 | 56,931 / 56,934 (100.0%) | 0 / 444,061 (0.0%) |
| [g_lex_etcbc](g_lex_etcbc.md) | +1.00 | 56,891 / 56,891 (100.0%) | 40 / 444,104 (0.0%) |
| [g_pfm_etcbc](g_pfm_etcbc.md) | +0.25 | 4,033 / 4,033 (100.0%) | 52,898 / 496,962 (10.6%) |
| [uvf_etcbc](uvf_etcbc.md) | -0.97 | 238 / 441,611 (0.1%) | 56,693 / 59,384 (95.5%) |
| [g_nme_etcbc](g_nme_etcbc.md) | -0.87 | 9,708 / 451,081 (2.2%) | 47,223 / 49,914 (94.6%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:08+00:00Z |
| description | The consonantal representation of a word or sign in BHSA transliteration. |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
