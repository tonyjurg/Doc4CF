# st.tf

[← Corpus index](../index.md)

state (morphology tag)

Node · UTF-8 · str

## Generated description

The node feature st records a morphological state tag on word nodes in the Dead Sea Scrolls corpus\. Its values come from Martin Abegg's data files via personal communication\. Four string values occur, including a and c\. Missing assignments mean no state was recorded, not a negative class\. The tag may represent a morphological state category within the morphology feature family\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 107,481 (21.5%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "c" | 60,210 | 56.0% |
| "a" | 43,218 | 40.2% |
| "d" | 3,577 | 3.3% |
| "unknown" | 476 | 0.4% |

## Correlated features

- [nu](nu.md) word · φ +0.66

- [gn](gn.md) word · φ +0.66

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | st present when compared feature is present | st present when compared feature is absent |
| --- | --- | --- | --- |
| [nu](nu.md) | +0.66 | 107,479 / 194,670 (55.2%) | 2 / 306,325 (0.0%) |
| [gn](gn.md) | +0.66 | 107,478 / 194,777 (55.2%) | 3 / 306,218 (0.0%) |
| [cl](cl.md) | +0.29 | 95,711 / 312,839 (30.6%) | 11,770 / 188,156 (6.3%) |
| [ps](ps.md) | -0.17 | 7 / 49,100 (0.0%) | 107,474 / 451,895 (23.8%) |
| [biblical](biblical.md), [book](book.md), [chapter](chapter.md), [verse](verse.md) | -0.14 | 32,485 / 218,189 (14.9%) | 74,996 / 282,806 (26.5%) |

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
| dateWritten | 2020-12-29T15:02:13Z |
| description | state (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | a, c, d, unknown |
| writtenBy | Text-Fabric |
