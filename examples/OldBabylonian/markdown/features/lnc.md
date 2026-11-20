# lnc.tf

[← Corpus index](../index.md)

ATF line identification of a comment line ($)

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The lnc feature is a node-level attribute on line nodes in the AbB Old Babylonian Cuneiform Text-Fabric corpus. It records ATF line identification specifically for comment lines marked with the dollar sign ($). The feature has one distinct value, the dollar sign ($), observed on 969 line nodes. It belongs to the Line Structure and Numbering feature family, which also includes ln, lnno, col, primecol, primeln, remarks, trans, and translation@en. The inventory does not specify how lnc relates to ln or lnno, nor does it list explicit targets for the feature.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [line](../../structure.html#type-line) | 969 (3.5%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "$" | 969 | 100.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### line nodes

| Compared feature(s) | φ | lnc present when compared feature is present | lnc present when compared feature is absent |
| --- | --- | --- | --- |
| [ln](ln.md) | -1.00 | 0 / 26,406 (0.0%) | 969 / 969 (100.0%) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | ATF line identification of a comment line ($) |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
