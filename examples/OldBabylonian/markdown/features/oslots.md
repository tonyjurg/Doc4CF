# oslots.tf

[← Corpus index](../index.md)

Maps each non-slot node to the slot nodes that make up its textual span. This core edge feature links structural units to the slots they cover and supports retrieving a node's text and relating it to the corpus's smallest units. Its edges express slot membership; they do not by themselves identify semantic, syntactic, or parent-child relationships between non-slot units.

Edge · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

oslots is an edge feature in the AbB Old Babylonian Cuneiform Text-Fabric corpus. The inventory identifies it as the edge-slot relation connecting non-slot nodes to the sign slot type, with otype recording the slot type. Its measured sources are cluster (23,449), document (1,285), face (2,834), line (27,375), and word (76,505); its sole attested target is sign, with 853,696 targets. The entry reports no distinct values and no frequent values, and is flagged for review. Because the inventory supplies no description, examples, or value semantics, the precise meaning of the edge values remains tentative and unspecified.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [document](../../structure.html#type-document) | 1,285 (100.0%) |
| [face](../../structure.html#type-face) | 2,834 (100.0%) |
| [line](../../structure.html#type-line) | 27,375 (100.0%) |
| [word](../../structure.html#type-word) | 76,505 (100.0%) |
| [cluster](../../structure.html#type-cluster) | 23,449 (100.0%) |

## Points to

| Node type | Incoming edges |
| --- | --- |
| [sign](../../structure.html#type-sign) | 853,696 |

## Observed edge connections

Counts show recorded edges for each source and target node-type pair.

| Source node type | Target node type | Edges |
| --- | --- | --- |
| [cluster](../../structure.html#type-cluster) | [sign](../../structure.html#type-sign) | 41,789 |
| [document](../../structure.html#type-document) | [sign](../../structure.html#type-sign) | 203,219 |
| [face](../../structure.html#type-face) | [sign](../../structure.html#type-sign) | 203,219 |
| [line](../../structure.html#type-line) | [sign](../../structure.html#type-sign) | 203,219 |
| [word](../../structure.html#type-word) | [sign](../../structure.html#type-sign) | 202,250 |

## Targets per connected source node

Summary for source nodes with at least one recorded edge.

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | --- | --- | --- | --- |
| [cluster](../../structure.html#type-cluster) | 23,449 | 1 | 1 | 13 |
| [document](../../structure.html#type-document) | 1,285 | 1 | 136 | 1,113 |
| [face](../../structure.html#type-face) | 2,834 | 1 | 65 | 548 |
| [line](../../structure.html#type-line) | 27,375 | 1 | 7 | 26 |
| [word](../../structure.html#type-word) | 76,505 | 1 | 2 | 14 |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:10Z |
