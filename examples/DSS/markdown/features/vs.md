# vs.tf

[← Corpus index](../index.md)

verbal stem (morphology tag)

Node · UTF-8 · str

## Generated description

The vs feature is a node\-level morphological tag recording verbal stem on word nodes in the Dead Sea Scrolls corpus\. Values are populated on word nodes; unattested words have no recorded value rather than a negative stem assignment\. Attested stems include qal and hifil among 41 distinct values, with one value marking cases where the stem is not identified\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 66,332 (13.2%) |

## Frequent values

41 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "qal" | 38,989 | 58.8% |
| "hifil" | 8,350 | 12.6% |
| "piel" | 6,197 | 9.3% |
| "nifal" | 4,231 | 6.4% |
| "peal" | 4,040 | 6.1% |
| "hitpael" | 940 | 1.4% |
| "pael" | 542 | 0.8% |
| "aphel" | 472 | 0.7% |
| "pual" | 448 | 0.7% |
| "hofal" | 337 | 0.5% |
| "unknown" | 287 | 0.4% |
| "ithpeel" | 208 | 0.3% |

## Correlated features

- [vt](vt.md) word · φ +1.00

- [ps](ps.md) word · φ +0.75

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | vs present when compared feature is present | vs present when compared feature is absent |
| --- | --- | --- | --- |
| [vt](vt.md) | +1.00 | 66,317 / 66,317 (100.0%) | 15 / 434,678 (0.0%) |
| [ps](ps.md) | +0.75 | 44,253 / 49,100 (90.1%) | 22,079 / 451,895 (4.9%) |
| [gn](gn.md) | +0.40 | 58,527 / 194,777 (30.0%) | 7,805 / 306,218 (2.5%) |
| [cl](cl.md) | -0.50 | 0 / 312,839 (0.0%) | 66,332 / 188,156 (35.3%) |
| [st](st.md) | -0.13 | 5,418 / 107,481 (5.0%) | 60,914 / 393,514 (15.5%) |

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
| dateWritten | 2020-12-29T15:02:15Z |
| description | verbal stem (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | aphel, apoel, haphel, hifil, hishtafel, hishtaphel, hithaphel, hithpaal, hithpeel, hithpolel, hitopel, hitpael, hitpalpel, hitpoel, hofal, hophal, hotpaal, hpealal, ishtaphel, ithpaal, ithpeel, ithpoel, nifal, nitpael, pael, palel, passive, peal, peil, piel, pilpel, poal, poel, polal, polel, pual, pulal, qal, shaphel, tifil, unknown |
| writtenBy | Text-Fabric |
