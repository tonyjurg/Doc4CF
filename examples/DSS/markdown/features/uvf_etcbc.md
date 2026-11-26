# uvf_etcbc.tf

[← Corpus index](../index.md)

The consonantal representation of the univalent final consonant of a word in BHSA transliteration.

Node · UTF-8 · str

## Generated description

The node feature uvf\_etcbc records the consonantal representation of the univalent final consonant of a word in BHSA transliteration on word nodes\. Missing assignments mean no value is recorded rather than a negative class\. Concrete values include H and N\. The source is Automatic generated morphological parsing corrected by Thijs Amersfoort\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 441,611 (88.1%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "" | 440,941 | 99.8% |
| "H" | 498 | 0.1% |
| "N" | 95 | 0.0% |
| "J" | 77 | 0.0% |

## Correlated features

- [g_nme_etcbc](g_nme_etcbc.md) word · φ +0.90

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | uvf_etcbc present when compared feature is present | uvf_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [g_nme_etcbc](g_nme_etcbc.md) | +0.90 | 441,374 / 451,081 (97.8%) | 237 / 49,914 (0.5%) |
| [g_prs_etcbc](g_prs_etcbc.md) | +0.50 | 351,259 / 357,210 (98.3%) | 90,352 / 143,785 (62.8%) |
| [lex_etcbc](lex_etcbc.md) | +0.20 | 441,611 / 498,307 (88.6%) | 0 / 2,688 (0.0%) |
| [morph_etcbc](morph_etcbc.md) | -0.97 | 238 / 56,934 (0.4%) | 441,373 / 444,061 (99.4%) |
| [g_cons](g_cons.md) | -0.97 | 238 / 56,931 (0.4%) | 441,373 / 444,064 (99.4%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:13+00:00Z |
| description | The consonantal representation of the univalent final consonant of a word in BHSA transliteration. |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
