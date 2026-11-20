# ARK.tf

[← Corpus index](../index.md)

persistent identifier of type ARK from metadata field "UCLA Library ARK"

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The ARK feature is a node-level persistent identifier drawn from the metadata field “UCLA Library ARK”. It is attested on 853 document nodes, each carrying a distinct value such as 21198/zz0020h36c. The corpus contains 1,285 documents in total, so ARK coverage is partial rather than universal. No target relationships are defined for this feature. Because the inventory records only presence and frequency without explaining missing values, it is unclear whether the remaining 432 documents lack ARK identifiers entirely or whether the values were not parsed from the source metadata.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [document](../../structure.html#type-document) | 853 (66.4%) |

## Frequent values

853 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "21198/zz0020h36c" | 1 | 0.1% |
| "21198/zz0022c6r4" | 1 | 0.1% |
| "21198/zz0020xdxz" | 1 | 0.1% |
| "21198/zz0022bd5s" | 1 | 0.1% |
| "21198/zz00214r3g" | 1 | 0.1% |
| "21198/zz002109j4" | 1 | 0.1% |
| "21198/zz00217wk0" | 1 | 0.1% |
| "21198/zz0020vnzz" | 1 | 0.1% |
| "21198/zz0020vp20" | 1 | 0.1% |
| "21198/zz0020vp5j" | 1 | 0.1% |
| "21198/zz0020vpb4" | 1 | 0.1% |
| "21198/zz0021643p" | 1 | 0.1% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### document nodes

| Compared feature(s) | φ | ARK present when compared feature is present | ARK present when compared feature is absent |
| --- | --- | --- | --- |
| [docnumber](docnumber.md) | -0.19 | 770 / 1,202 (64.1%) | 83 / 83 (100.0%) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | persistent identifier of type ARK from metadata field "UCLA Library ARK" |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:07Z |
