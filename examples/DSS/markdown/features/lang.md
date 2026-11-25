# lang.tf

[← Corpus index](../index.md)

language of a word or sign, only if it is not Hebrew

Node · UTF-8 · str

## Generated description

The lang node feature annotates word and sign nodes with language only when it is not Hebrew\. Two values are attested: g \(Greek\) and a \(Aramaic\)\. Hebrew words and signs carry no lang value; absence means no value is recorded rather than a negative class\. Values are observed on word and sign nodes\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 49,411 (9.9%) |
| [sign](../../structure.html#type-sign) | 135,728 (9.5%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "a" | 185,116 | 100.0% |
| "g" | 23 | 0.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | lang present when compared feature is present | lang present when compared feature is absent |
| --- | --- | --- | --- |
| [uvf_etcbc](uvf_etcbc.md) | +0.12 | 49,411 / 441,611 (11.2%) | 0 / 59,384 (0.0%) |
| [g_nme_etcbc](g_nme_etcbc.md) | +0.11 | 49,411 / 451,081 (11.0%) | 0 / 49,914 (0.0%) |
| [gn_etcbc](gn_etcbc.md) | -0.25 | 3,305 / 219,259 (1.5%) | 46,106 / 281,736 (16.4%) |
| [biblical](biblical.md), [book](book.md), [chapter](chapter.md), [verse](verse.md) | -0.24 | 3,438 / 218,189 (1.6%) | 45,973 / 282,806 (16.3%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.word.features` | lang lex cl ps gn nu st vs vt md |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:06Z |
| description | language of a word or sign, only if it is not Hebrew |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | g=greek, a=aramaic |
| writtenBy | Text-Fabric |
