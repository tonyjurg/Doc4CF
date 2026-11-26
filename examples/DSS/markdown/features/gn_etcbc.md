# gn_etcbc.tf

[← Corpus index](../index.md)

Dead Sea Scrolls: additions based on BHSA and machine learning

Node · UTF-8 · str

## Generated description

gn\_etcbc is a node feature on word nodes; missing assignments indicate no value rather than a negative class\. It has five distinct values, including m and f\. Part of the DSS additions family based on BHSA and machine learning, it may encode grammatical gender, paralleling gn, but this interpretation is unproven\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 219,259 (43.8%) |

## Frequent values

5 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "NA" | 86,611 | 39.5% |
| "m" | 84,962 | 38.7% |
| "unknown" | 23,473 | 10.7% |
| "f" | 18,901 | 8.6% |
| "" | 5,312 | 2.4% |

## Correlated features

- [biblical](biblical.md) word · φ +0.83

- [book](book.md) word · φ +0.83

- [chapter](chapter.md) word · φ +0.83

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | gn_etcbc present when compared feature is present | gn_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [biblical](biblical.md), [book](book.md), [chapter](chapter.md), [verse](verse.md) | +0.83 | 197,922 / 218,189 (90.7%) | 21,337 / 282,806 (7.5%) |
| [glex](glex.md), [glexe](glexe.md), [glexo](glexo.md) | +0.43 | 219,074 / 405,736 (54.0%) | 185 / 95,259 (0.2%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.42 | 219,074 / 406,914 (53.8%) | 185 / 94,081 (0.2%) |
| [lang](lang.md) | -0.25 | 3,305 / 49,411 (6.7%) | 215,954 / 451,584 (47.8%) |
| [uvf_etcbc](uvf_etcbc.md) | -0.22 | 175,298 / 441,611 (39.7%) | 43,961 / 59,384 (74.0%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2020 |
| dateWritten | 2026-11-04T12:00:10+00:00Z |
| description | Dead Sea Scrolls: additions based on BHSA and machine learning |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martijn Naaijer's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
