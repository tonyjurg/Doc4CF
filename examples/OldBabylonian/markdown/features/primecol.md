# primecol.tf

[← Corpus index](../index.md)

whether a prime is present on a column number

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The primecol feature is a node-level attribute on line nodes indicating whether a prime is present on an ATF column number. It is sourced from line nodes and has one distinct value, with value 1 occurring four times according to the frequent-values table. The feature is associated with col, which records the ATF column number, but the inventory does not specify how primecol and col interact or whether primecol applies only when a column number exists. Because only value 1 is attested, it is unclear whether absence of a prime is encoded by a zero, by a missing value, or by feature absence on most line nodes.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [line](../../structure.html#type-line) | 4 (0.0%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 4 | 100.0% |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | whether a prime is present on a column number |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
