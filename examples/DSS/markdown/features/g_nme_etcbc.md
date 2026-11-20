# g_nme_etcbc.tf

[← Corpus index](../index.md)

The consonantal representation of the nominal ending of a word in BHSA transliteration.

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 451,081 (90.0%) |

## Frequent values

35 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "" | 421,851 | 93.5% |
| "/J" | 4,866 | 1.1% |
| "/JM" | 4,641 | 1.0% |
| "/T" | 3,510 | 0.8% |
| "/H" | 3,047 | 0.7% |
| "J" | 2,634 | 0.6% |
| "JM" | 2,138 | 0.5% |
| "/WT" | 1,801 | 0.4% |
| "H" | 1,704 | 0.4% |
| "T" | 1,606 | 0.4% |
| "WT" | 1,088 | 0.2% |
| "/M" | 836 | 0.2% |

## Correlated features

- [uvf_etcbc](uvf_etcbc.md) word · φ +0.90

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | g_nme_etcbc present when compared feature is present | g_nme_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [uvf_etcbc](uvf_etcbc.md) | +0.90 | 441,374 / 441,611 (99.9%) | 9,707 / 59,384 (16.3%) |
| [g_prs_etcbc](g_prs_etcbc.md) | +0.46 | 352,987 / 357,210 (98.8%) | 98,094 / 143,785 (68.2%) |
| [lex_etcbc](lex_etcbc.md) | +0.22 | 451,081 / 498,307 (90.5%) | 0 / 2,688 (0.0%) |
| [morph_etcbc](morph_etcbc.md) | -0.87 | 9,708 / 56,934 (17.1%) | 441,373 / 444,061 (99.4%) |
| [g_cons](g_cons.md) | -0.87 | 9,708 / 56,931 (17.1%) | 441,373 / 444,064 (99.4%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:08+00:00Z |
| description | The consonantal representation of the nominal ending of a word in BHSA transliteration. |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
