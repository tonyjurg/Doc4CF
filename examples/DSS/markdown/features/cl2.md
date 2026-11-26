# cl2.tf

[← Corpus index](../index.md)

class (for part 2) (morphology tag)

Node · UTF-8 · str

## Generated description

The node feature cl2 records a morphology class tag for part 2 on word nodes in the Dead Sea Scrolls corpus\. Missing assignments mean no value is recorded rather than a negative class\. Attested values include d and n among four distinct values\. The feature belongs to the morphology family and is sourced from Martin Abegg's data files\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 1,334 (0.3%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "d" | 697 | 52.2% |
| "n" | 353 | 26.5% |
| "h" | 246 | 18.4% |
| "unknown" | 38 | 2.8% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | cl2 present when compared feature is present | cl2 present when compared feature is absent |
| --- | --- | --- | --- |
| [gn3](gn3.md), [nu3](nu3.md), [ps3](ps3.md) | +0.10 | 14 / 14 (100.0%) | 1,320 / 500,981 (0.3%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:01:57Z |
| description | class (for part 2) (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | d, h, n, unknown |
| writtenBy | Text-Fabric |
