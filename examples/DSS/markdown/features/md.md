# md.tf

[← Corpus index](../index.md)

mood (morphology tag)

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 1,984 (0.4%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "juss" | 1,333 | 67.2% |
| "coho" | 546 | 27.5% |
| "cons" | 103 | 5.2% |
| "unknown" | 2 | 0.1% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | md present when compared feature is present | md present when compared feature is absent |
| --- | --- | --- | --- |
| [ps](ps.md) | +0.19 | 1,981 / 49,100 (4.0%) | 3 / 451,895 (0.0%) |
| [vt](vt.md) | +0.16 | 1,984 / 66,317 (3.0%) | 0 / 434,678 (0.0%) |
| [vs](vs.md) | +0.16 | 1,984 / 66,332 (3.0%) | 0 / 434,663 (0.0%) |

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
| dateWritten | 2020-12-29T15:02:08Z |
| description | mood (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | coho, cons, juss, unknown |
| writtenBy | Text-Fabric |
