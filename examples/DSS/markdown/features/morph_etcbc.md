# morph_etcbc.tf

[← Corpus index](../index.md)

The complete morphological parsing of a word in the BHSA convention.

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 56,934 (11.4%) |

## Frequent values

11,462 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "W" | 6,455 | 11.3% |
| "H" | 2,782 | 4.9% |
| "L" | 2,573 | 4.5% |
| "B" | 2,132 | 3.7% |
| "M(N" | 911 | 1.6% |
| "L&W>" | 844 | 1.5% |
| "<L" | 656 | 1.2% |
| ">CR" | 623 | 1.1% |
| ">T" | 591 | 1.0% |
| "JHWH/" | 531 | 0.9% |
| "K&WL/:c" | 508 | 0.9% |
| "K&WL/" | 488 | 0.9% |

## Correlated features

- [g_cons](g_cons.md) word · φ +1.00

- [g_lex_etcbc](g_lex_etcbc.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | morph_etcbc present when compared feature is present | morph_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [g_cons](g_cons.md) | +1.00 | 56,931 / 56,931 (100.0%) | 3 / 444,064 (0.0%) |
| [g_lex_etcbc](g_lex_etcbc.md) | +1.00 | 56,891 / 56,891 (100.0%) | 43 / 444,104 (0.0%) |
| [g_pfm_etcbc](g_pfm_etcbc.md) | +0.25 | 4,033 / 4,033 (100.0%) | 52,901 / 496,962 (10.6%) |
| [uvf_etcbc](uvf_etcbc.md) | -0.97 | 238 / 441,611 (0.1%) | 56,696 / 59,384 (95.5%) |
| [g_nme_etcbc](g_nme_etcbc.md) | -0.87 | 9,708 / 451,081 (2.2%) | 47,226 / 49,914 (94.6%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:11+00:00Z |
| description | The complete morphological parsing of a word in the BHSA convention. |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
