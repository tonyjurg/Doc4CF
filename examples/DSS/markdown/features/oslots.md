# oslots.tf

[← Corpus index](../index.md)

Maps each non-slot node to the slot nodes that make up its textual span. This core edge feature links structural units to the slots they cover and supports retrieving a node's text and relating it to the corpus's smallest units. Its edges express slot membership; they do not by themselves identify semantic, syntactic, or parent-child relationships between non-slot units.

Edge · UTF-8 · str

## Generated description

The oslots edge feature maps non\-slot nodes to the sign slots they cover, so following an oslots edge returns a node's constituent slots and supports locating its text span\. Source\-node counts differ from edge counts\. These links show slot membership only, not parenthood, semantics, or order\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [scroll](../../structure.html#type-scroll) | 1,001 (100.0%) |
| [lex](../../structure.html#type-lex) | 10,450 (100.0%) |
| [fragment](../../structure.html#type-fragment) | 11,182 (100.0%) |
| [line](../../structure.html#type-line) | 52,895 (100.0%) |
| [clause](../../structure.html#type-clause) | 125 (100.0%) |
| [cluster](../../structure.html#type-cluster) | 101,099 (100.0%) |
| [phrase](../../structure.html#type-phrase) | 315 (100.0%) |
| [word](../../structure.html#type-word) | 500,995 (100.0%) |

## Points to

| Node type | Incoming edges |
| --- | --- |
| [sign](../../structure.html#type-sign) | 7,728,622 |

## Observed edge connections

Counts show recorded edges for each source and target node-type pair.

| Source node type | Target node type | Edges |
| --- | --- | --- |
| [clause](../../structure.html#type-clause) | [sign](../../structure.html#type-sign) | 1,606 |
| [cluster](../../structure.html#type-cluster) | [sign](../../structure.html#type-sign) | 675,198 |
| [fragment](../../structure.html#type-fragment) | [sign](../../structure.html#type-sign) | 1,430,241 |
| [lex](../../structure.html#type-lex) | [sign](../../structure.html#type-sign) | 1,349,509 |
| [line](../../structure.html#type-line) | [sign](../../structure.html#type-sign) | 1,430,241 |
| [phrase](../../structure.html#type-phrase) | [sign](../../structure.html#type-sign) | 1,606 |
| [scroll](../../structure.html#type-scroll) | [sign](../../structure.html#type-sign) | 1,430,241 |
| [word](../../structure.html#type-word) | [sign](../../structure.html#type-sign) | 1,409,980 |

## Targets per connected source node

Summary for source nodes with at least one recorded edge.

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | --- | --- | --- | --- |
| [cluster](../../structure.html#type-cluster) | 101,099 | 1 | 2 | 660 |
| [fragment](../../structure.html#type-fragment) | 11,182 | 3 | 27 | 4,503 |
| [lex](../../structure.html#type-lex) | 10,450 | 1 | 11 | 108,439 |
| [line](../../structure.html#type-line) | 52,895 | 1 | 20 | 686 |
| [scroll](../../structure.html#type-scroll) | 1,001 | 6 | 351 | 78,106 |
| [word](../../structure.html#type-word) | 500,995 | 1 | 2 | 77 |
| [clause](../../structure.html#type-clause) | 125 | 3 | 11 | 52 |
| [phrase](../../structure.html#type-phrase) | 315 | 1 | 4 | 35 |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:17Z |
| description | Dead Sea Scrolls: biblical and non-biblical scrolls |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
