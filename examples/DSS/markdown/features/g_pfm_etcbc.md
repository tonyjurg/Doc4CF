# g_pfm_etcbc.tf

[← Corpus index](../index.md)

The consonantal representation of the preformative of a word in BHSA transliteration.

Node · UTF-8 · str

## Generated description

The node feature g\_pfm\_etcbc records the consonantal representation of a word's preformative in BHSA transliteration\. It is populated on word nodes, with missing assignments indicating no recorded value rather than a negative class\. Attested values include J and T among nine distinct strings\. The feature originates from automatic morphological parsing corrected by Thijs Amersfoort and is licensed CC\-BY\-NC\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 4,033 (0.8%) |

## Frequent values

9 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "J" | 2,220 | 55.0% |
| "T" | 846 | 21.0% |
| "M" | 435 | 10.8% |
| ">" | 391 | 9.7% |
| "H" | 70 | 1.7% |
| "N" | 68 | 1.7% |
| "TJ" | 1 | 0.0% |
| "X" | 1 | 0.0% |
| ">J" | 1 | 0.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | g_pfm_etcbc present when compared feature is present | g_pfm_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [g_vbe_etcbc](g_vbe_etcbc.md) | +0.36 | 1,323 / 3,309 (40.0%) | 2,710 / 497,686 (0.5%) |
| [g_lex_etcbc](g_lex_etcbc.md) | +0.25 | 4,033 / 56,891 (7.1%) | 0 / 444,104 (0.0%) |
| [g_cons](g_cons.md) | +0.25 | 4,033 / 56,931 (7.1%) | 0 / 444,064 (0.0%) |
| [g_nme_etcbc](g_nme_etcbc.md) | -0.25 | 213 / 451,081 (0.0%) | 3,820 / 49,914 (7.7%) |
| [uvf_etcbc](uvf_etcbc.md) | -0.24 | 84 / 441,611 (0.0%) | 3,949 / 59,384 (6.6%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:09+00:00Z |
| description | The consonantal representation of the preformative of a word in BHSA transliteration. |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
