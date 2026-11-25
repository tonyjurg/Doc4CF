# gn3.tf

[← Corpus index](../index.md)

gender (for part 3) (morphology tag)

Node · UTF-8 · str

## Generated description

The node feature gn3 records gender \(part 3\) as a morphology tag on word nodes\. Its metadata lists string values, including c and f, sourced from Martin Abegg's data files by personal communication\. Missing assignments mean no gender value is recorded rather than a negative class\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 14 (0.0%) |

## Frequent values

3 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "c" | 5 | 35.7% |
| "m" | 5 | 35.7% |
| "f" | 4 | 28.6% |

## Correlated features

- [nu3](nu3.md) word · φ +1.00

- [ps3](ps3.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | gn3 present when compared feature is present | gn3 present when compared feature is absent |
| --- | --- | --- | --- |
| [nu3](nu3.md), [ps3](ps3.md) | +1.00 | 14 / 14 (100.0%) | 0 / 500,981 (0.0%) |
| [cl2](cl2.md) | +0.10 | 14 / 1,334 (1.0%) | 0 / 499,661 (0.0%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:06Z |
| description | gender (for part 3) (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | c, f, m |
| writtenBy | Text-Fabric |
