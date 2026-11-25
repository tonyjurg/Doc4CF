# g_vbe_etcbc.tf

[← Corpus index](../index.md)

The consonantal representation of the verbal ending of a word in BHSA transliteration.

Node · UTF-8 · str

## Generated description

The node feature g\_vbe\_etcbc records the consonantal representation of a word's verbal ending in BHSA transliteration\. Values are assigned to word nodes; missing assignments indicate no recorded value rather than a negative class\. It belongs to the dss\-additions family, uses string values, and includes forms such as W and TH\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 3,309 (0.7%) |

## Frequent values

25 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "W" | 1,907 | 57.6% |
| "TH" | 350 | 10.6% |
| "TJ" | 318 | 9.6% |
| "H" | 265 | 8.0% |
| "J" | 128 | 3.9% |
| "T" | 100 | 3.0% |
| "NH" | 49 | 1.5% |
| "TMH" | 40 | 1.2% |
| "NW" | 35 | 1.1% |
| "WN" | 33 | 1.0% |
| "WTH" | 24 | 0.7% |
| "TM" | 17 | 0.5% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | g_vbe_etcbc present when compared feature is present | g_vbe_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [g_pfm_etcbc](g_pfm_etcbc.md) | +0.36 | 1,323 / 4,033 (32.8%) | 1,986 / 496,962 (0.4%) |
| [g_vbs_etcbc](g_vbs_etcbc.md) | +0.24 | 536 / 1,476 (36.3%) | 2,773 / 499,519 (0.6%) |
| [g_lex_etcbc](g_lex_etcbc.md) | +0.23 | 3,309 / 56,891 (5.8%) | 0 / 444,104 (0.0%) |
| [g_nme_etcbc](g_nme_etcbc.md) | -0.25 | 0 / 451,081 (0.0%) | 3,309 / 49,914 (6.6%) |
| [uvf_etcbc](uvf_etcbc.md) | -0.22 | 5 / 441,611 (0.0%) | 3,304 / 59,384 (5.6%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:10+00:00Z |
| description | The consonantal representation of the verbal ending of a word in BHSA transliteration. |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
