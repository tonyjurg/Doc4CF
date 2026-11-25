# gn2.tf

[← Corpus index](../index.md)

gender (for part 2) (morphology tag)

Node · UTF-8 · str

## Generated description

gn2 is a node feature on word nodes that records gender for part 2 as a morphology tag\. It uses four string values, including m and f, drawn from Martin Abegg's data files via personal communication\. The feature belongs to the morphology tagging family and may encode grammatical gender distinctions, though the semantics of some values are undocumented\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 44,408 (8.9%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "m" | 32,063 | 72.2% |
| "c" | 8,233 | 18.5% |
| "f" | 4,090 | 9.2% |
| "unknown" | 22 | 0.0% |

## Correlated features

- [ps2](ps2.md) word · φ +1.00

- [nu2](nu2.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | gn2 present when compared feature is present | gn2 present when compared feature is absent |
| --- | --- | --- | --- |
| [ps2](ps2.md) | +1.00 | 44,408 / 44,409 (100.0%) | 0 / 456,586 (0.0%) |
| [nu2](nu2.md) | +1.00 | 44,406 / 44,406 (100.0%) | 2 / 456,589 (0.0%) |
| [st](st.md) | +0.28 | 25,785 / 107,481 (24.0%) | 18,623 / 393,514 (4.7%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:06Z |
| description | gender (for part 2) (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | c, f, m, unknown |
| writtenBy | Text-Fabric |
