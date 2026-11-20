# type.tf

[← Corpus index](../index.md)

name of a type of cluster or kind of sign

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The `type` feature names the type of a cluster or the kind of a sign in the AbB Old Babylonian Cuneiform corpus. It is a node-level feature with sources on 23,449 cluster nodes and 203,219 sign nodes and 14 distinct values. Frequent values include reading (188,292), unknown (8,761), langalt (7,600), missing (7,572), det (6,794), numeral (2,184), ellipsis (1,617), grapheme (1,272), uncertain (1,183), commentline (969), supplied (231), and complex (122). The feature is described as refining `otype`, but whether type values are shared across clusters and signs or namespaced by node type is not specified.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [cluster](../../structure.html#type-cluster) | 23,449 (100.0%) |
| [sign](../../structure.html#type-sign) | 203,219 (100.0%) |

## Frequent values

14 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "reading" | 188,292 | 83.1% |
| "unknown" | 8,761 | 3.9% |
| "langalt" | 7,600 | 3.4% |
| "missing" | 7,572 | 3.3% |
| "det" | 6,794 | 3.0% |
| "numeral" | 2,184 | 1.0% |
| "ellipsis" | 1,617 | 0.7% |
| "grapheme" | 1,272 | 0.6% |
| "uncertain" | 1,183 | 0.5% |
| "commentline" | 969 | 0.4% |
| "supplied" | 231 | 0.1% |
| "complex" | 122 | 0.1% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.cluster.label` | {type} |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | name of a type of cluster or kind of sign |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:10Z |
