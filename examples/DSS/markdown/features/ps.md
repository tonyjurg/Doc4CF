# ps.tf

[← Corpus index](../index.md)

person (morphology tag)

Node · UTF-8 · str

## Generated description

The node feature ps records person as a morphology tag on word nodes\. Values include 1 and unknown among other string\-coded options\. Source metadata attributes the data to Martin Abegg's personal communication\. Missing assignments mean no value is recorded, not a negative person class\. Unpopulated word nodes simply lack a value\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 49,100 (9.8%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "3" | 33,880 | 69.0% |
| "2" | 7,924 | 16.1% |
| "1" | 6,792 | 13.8% |
| "unknown" | 504 | 1.0% |

## Correlated features

- [vt](vt.md) word · φ +0.75

- [vs](vs.md) word · φ +0.75

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | ps present when compared feature is present | ps present when compared feature is absent |
| --- | --- | --- | --- |
| [vt](vt.md) | +0.75 | 44,252 / 66,317 (66.7%) | 4,848 / 434,678 (1.1%) |
| [vs](vs.md) | +0.75 | 44,253 / 66,332 (66.7%) | 4,847 / 434,663 (1.1%) |
| [gn](gn.md) | +0.41 | 49,092 / 194,777 (25.2%) | 8 / 306,218 (0.0%) |
| [cl](cl.md) | -0.36 | 4,843 / 312,839 (1.5%) | 44,257 / 188,156 (23.5%) |
| [st](st.md) | -0.17 | 7 / 107,481 (0.0%) | 49,093 / 393,514 (12.5%) |

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
| dateWritten | 2020-12-29T15:02:10Z |
| description | person (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | 1, 2, 3, unknown |
| writtenBy | Text-Fabric |
