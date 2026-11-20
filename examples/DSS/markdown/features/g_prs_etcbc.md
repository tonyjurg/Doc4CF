# g_prs_etcbc.tf

[← Corpus index](../index.md)

The consonantal representation of the pronominal suffix of a word in BHSA transliteration.

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 357,210 (71.3%) |

## Frequent values

75 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "NA" | 312,208 | 87.4% |
| "W" | 10,194 | 2.9% |
| "K" | 5,965 | 1.7% |
| "J" | 5,257 | 1.5% |
| "H" | 4,302 | 1.2% |
| "KH" | 3,755 | 1.1% |
| "M" | 3,518 | 1.0% |
| "HM" | 2,160 | 0.6% |
| "KM" | 2,051 | 0.6% |
| "NW" | 1,838 | 0.5% |
| "NJ" | 1,099 | 0.3% |
| "HW" | 1,010 | 0.3% |

## Correlated features

- [glyph](glyph.md) word · φ +0.75

- [glyphe](glyphe.md) word · φ +0.75

- [glypho](glypho.md) word · φ +0.75

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | g_prs_etcbc present when compared feature is present | g_prs_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [glyph](glyph.md), [glyphe](glyphe.md), [glypho](glypho.md) | +0.75 | 357,210 / 408,125 (87.5%) | 0 / 92,870 (0.0%) |
| [glex](glex.md), [glexe](glexe.md), [glexo](glexo.md) | +0.74 | 354,838 / 405,736 (87.5%) | 2,372 / 95,259 (2.5%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.73 | 355,014 / 406,914 (87.2%) | 2,196 / 94,081 (2.3%) |
| [morph_etcbc](morph_etcbc.md) | -0.48 | 6,093 / 56,934 (10.7%) | 351,117 / 444,061 (79.1%) |
| [g_cons](g_cons.md) | -0.48 | 6,093 / 56,931 (10.7%) | 351,117 / 444,064 (79.1%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:09+00:00Z |
| description | The consonantal representation of the pronominal suffix of a word in BHSA transliteration. |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
