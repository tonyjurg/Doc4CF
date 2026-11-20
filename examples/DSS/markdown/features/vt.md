# vt.tf

[← Corpus index](../index.md)

verbal tense/aspect (morphology tag)

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 66,317 (13.2%) |

## Frequent values

9 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "perf" | 19,210 | 29.0% |
| "impf" | 18,719 | 28.2% |
| "ptca" | 9,210 | 13.9% |
| "infc" | 7,141 | 10.8% |
| "wayy" | 5,871 | 8.9% |
| "impv" | 3,648 | 5.5% |
| "ptcp" | 1,440 | 2.2% |
| "infa" | 639 | 1.0% |
| "unknown" | 439 | 0.7% |

## Correlated features

- [vs](vs.md) word · φ +1.00

- [ps](ps.md) word · φ +0.75

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | vt present when compared feature is present | vt present when compared feature is absent |
| --- | --- | --- | --- |
| [vs](vs.md) | +1.00 | 66,317 / 66,332 (100.0%) | 0 / 434,663 (0.0%) |
| [ps](ps.md) | +0.75 | 44,252 / 49,100 (90.1%) | 22,065 / 451,895 (4.9%) |
| [gn](gn.md) | +0.40 | 58,526 / 194,777 (30.0%) | 7,791 / 306,218 (2.5%) |
| [cl](cl.md) | -0.50 | 0 / 312,839 (0.0%) | 66,317 / 188,156 (35.2%) |
| [st](st.md) | -0.13 | 5,418 / 107,481 (5.0%) | 60,899 / 393,514 (15.5%) |

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
| dateWritten | 2020-12-29T15:02:16Z |
| description | verbal tense/aspect (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | impf, impv, infa, infc, perf, ptca, ptcp, unknown, wayy |
| writtenBy | Text-Fabric |
