# g_vbs_etcbc.tf

[← Corpus index](../index.md)

The consonantal representation of the root formation of a verb in BHSA transliteration.

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 1,476 (0.3%) |

## Frequent values

16 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "H" | 738 | 50.0% |
| "N" | 465 | 31.5% |
| "T" | 114 | 7.7% |
| "HT" | 85 | 5.8% |
| "W" | 19 | 1.3% |
| "CT" | 12 | 0.8% |
| "HCT" | 11 | 0.7% |
| ">" | 9 | 0.6% |
| "HW" | 9 | 0.6% |
| "C" | 6 | 0.4% |
| "Z" | 2 | 0.1% |
| "S" | 2 | 0.1% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | g_vbs_etcbc present when compared feature is present | g_vbs_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [g_vbe_etcbc](g_vbe_etcbc.md) | +0.24 | 536 / 3,309 (16.2%) | 940 / 497,686 (0.2%) |
| [g_lex_etcbc](g_lex_etcbc.md) | +0.15 | 1,476 / 56,891 (2.6%) | 0 / 444,104 (0.0%) |
| [g_cons](g_cons.md) | +0.15 | 1,476 / 56,931 (2.6%) | 0 / 444,064 (0.0%) |
| [uvf_etcbc](uvf_etcbc.md) | -0.15 | 1 / 441,611 (0.0%) | 1,475 / 59,384 (2.5%) |
| [g_nme_etcbc](g_nme_etcbc.md) | -0.14 | 197 / 451,081 (0.0%) | 1,279 / 49,914 (2.6%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:10+00:00Z |
| description | The consonantal representation of the root formation of a verb in BHSA transliteration. |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
