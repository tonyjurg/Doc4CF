# rec.tf

[← Corpus index](../index.md)

reconstructed by a modern editor

Node · UTF-8 · int

## Generated description

The node feature rec records integer value 1 on sign nodes in the Dead Sea Scrolls corpus, annotated as 'reconstructed by a modern editor' in feature metadata\. Populated sign nodes carry this value; nodes without an assignment have no value recorded rather than a negative class\. The single value may indicate editorial reconstruction, but absence does not establish non\-reconstruction\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 661,789 (46.3%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 661,789 | 100.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | rec present when compared feature is present | rec present when compared feature is absent |
| --- | --- | --- | --- |
| [unc](unc.md) | -0.24 | 188 / 92,266 (0.2%) | 661,601 / 1,337,975 (49.4%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:11Z |
| description | reconstructed by a modern editor |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | int |
| values | 1 |
| writtenBy | Text-Fabric |
