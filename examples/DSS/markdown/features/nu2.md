# nu2.tf

[← Corpus index](../index.md)

number (for part 2) (morphology tag)

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 44,406 (8.9%) |

## Frequent values

3 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "s" | 32,611 | 73.4% |
| "p" | 11,783 | 26.5% |
| "unknown" | 12 | 0.0% |

## Correlated features

- [gn2](gn2.md) word · φ +1.00

- [ps2](ps2.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | nu2 present when compared feature is present | nu2 present when compared feature is absent |
| --- | --- | --- | --- |
| [gn2](gn2.md) | +1.00 | 44,406 / 44,408 (100.0%) | 0 / 456,587 (0.0%) |
| [ps2](ps2.md) | +1.00 | 44,406 / 44,409 (100.0%) | 0 / 456,586 (0.0%) |
| [st](st.md) | +0.28 | 25,784 / 107,481 (24.0%) | 18,622 / 393,514 (4.7%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:09Z |
| description | number (for part 2) (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | p, s, unknown |
| writtenBy | Text-Fabric |
