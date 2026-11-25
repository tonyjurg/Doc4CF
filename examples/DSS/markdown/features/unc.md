# unc.tf

[← Corpus index](../index.md)

uncertain material in various degrees: higher degree is less certain

Node · UTF-8 · int

## Generated description

The node feature unc records degrees of uncertain material on sign nodes, with higher integer values indicating less certainty\. It uses values 1 through 4, where 4 marks the highest degree of uncertainty\. Populated assignments appear on sign nodes; missing assignments mean no value is recorded rather than a negative classification\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 92,266 (6.5%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 4 | 40,167 | 43.5% |
| 2 | 27,146 | 29.4% |
| 3 | 14,629 | 15.9% |
| 1 | 10,324 | 11.2% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | unc present when compared feature is present | unc present when compared feature is absent |
| --- | --- | --- | --- |
| [rec](rec.md) | -0.24 | 188 / 661,789 (0.0%) | 92,078 / 768,452 (12.0%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:15Z |
| description | uncertain material in various degrees: higher degree is less certain |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | int |
| values | 1 2 3 4 |
| writtenBy | Text-Fabric |
