# sim.tf

[← Corpus index](../index.md)

similarity between lines, as a percentage of the common material wrt the combined material

Edge · UTF-8 · int

## Generated description

The sim feature records directed similarity edges from line nodes to line nodes in the Dead Sea Scrolls corpus\. Edge values are integer percentages measuring shared material against combined material, with frequent values including 60 and 100\. Edge direction runs from source line to target line\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [line](../../structure.html#type-line) | 10,733 (20.3%) |

## Points to

| Node type | Incoming edges |
| --- | --- |
| [line](../../structure.html#type-line) | 51,862 |

## Observed edge connections

Counts show recorded edges for each source and target node-type pair.

| Source node type | Target node type | Edges |
| --- | --- | --- |
| [line](../../structure.html#type-line) | [line](../../structure.html#type-line) | 51,862 |

## Targets per connected source node

Summary for source nodes with at least one recorded edge.

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | --- | --- | --- | --- |
| [line](../../structure.html#type-line) | 10,733 | 1 | 2 | 312 |

## Frequent values

38 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 60 | 24,546 | 47.3% |
| 67 | 11,761 | 22.7% |
| 75 | 3,781 | 7.3% |
| 100 | 3,646 | 7.0% |
| 62 | 1,248 | 2.4% |
| 71 | 988 | 1.9% |
| 80 | 857 | 1.7% |
| 64 | 667 | 1.3% |
| 69 | 505 | 1.0% |
| 73 | 379 | 0.7% |
| 83 | 304 | 0.6% |
| 65 | 290 | 0.6% |

### Source metadata

| Field | Value |
| --- | --- |
| edgeValues |  |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Dirk Roorda |
| createdDate | 2022-10-09 |
| description | similarity between lines, as a percentage of the common material wrt the combined material |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| sourceCreatedBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| sourceCreatedDate | 2015 |
| sourceDescription | Dead Sea Scrolls: biblical and non-biblical scrolls |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2022-10-09T10:08:27Z |
