# otype.tf

[← Corpus index](../index.md)

Maps every Text-Fabric node to its node type. The type identifies what kind of structural unit the node represents, such as a slot or a larger unit defined by the corpus. This core node feature lets tools select nodes by type and interpret where other features apply. Type labels describe the corpus data model; their names alone do not establish the linguistic or semantic role of a unit.

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The otype feature is a node-level annotation in the AbB Old Babylonian Cuneiform Text-Fabric corpus that assigns every node to one of six corpus node types. Its attested values are document, face, line, word, cluster, and sign, with sign serving as the slot type. Observed source counts are 1,285 documents, 2,834 faces, 27,375 lines, 76,505 words, 23,449 clusters, and 203,219 signs. The feature belongs to the node_typing family and is tentatively related to the type feature through an inferred refinement link, though the precise distinction and namespace sharing between otype and type remain unspecified.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [document](../../structure.html#type-document) | 1,285 (100.0%) |
| [face](../../structure.html#type-face) | 2,834 (100.0%) |
| [line](../../structure.html#type-line) | 27,375 (100.0%) |
| [word](../../structure.html#type-word) | 76,505 (100.0%) |
| [cluster](../../structure.html#type-cluster) | 23,449 (100.0%) |
| [sign](../../structure.html#type-sign) | 203,219 (100.0%) |

## Frequent values

6 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "sign" | 203,219 | 60.7% |
| "word" | 76,505 | 22.9% |
| "line" | 27,375 | 8.2% |
| "cluster" | 23,449 | 7.0% |
| "face" | 2,834 | 0.8% |
| "document" | 1,285 | 0.4% |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
