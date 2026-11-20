# frame.tf

[← Corpus index](../index.md)

frame

Edge · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

frame is a directed, valued edge feature in the Greek New Testament (Nestle 1904) corpus linking word nodes to word nodes. It records 43,893 edges from 25,491 source words; each source has 1–18 outgoing links (median 2). Targets count edge endpoints, not unique nodes. Four string values occur: A0 (25,654), A1 (15,570), A2 (2,577), and AA2 (92). The inventory labels it "frame" but does not define its semantic relation.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 25,491 (18.5%) |

## Points to

| Node type | Incoming edges |
| --- | --- |
| [word](../../structure.html#type-word) | 43,893 |

## Observed edge connections

Counts show recorded edges for each source and target node-type pair.

| Source node type | Target node type | Edges |
| --- | --- | --- |
| [word](../../structure.html#type-word) | [word](../../structure.html#type-word) | 43,893 |

## Targets per connected source node

Summary for source nodes with at least one recorded edge.

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | --- | --- | --- | --- |
| [word](../../structure.html#type-word) | 25,491 | 1 | 2 | 18 |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "A0" | 25,654 | 58.4% |
| "A1" | 15,570 | 35.5% |
| "A2" | 2,577 | 5.9% |
| "AA2" | 92 | 0.2% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/frame.md) Source: `docs/features/frame.md`; configured at `configuration.docs.featureBase` |

### Source metadata

| Field | Value |
| --- | --- |
| edgeValues |  |
| author | Evangelists and apostles |
| converterSourceLocation | https://github.com/saulocantanhede/tfgreek2/tree/main/programs |
| converterVersion | 1.0.0 (July 9, 2024) |
| converters | Saulo de Oliveira Cantanhêde, Tony Jurg, Dirk Roorda |
| dataSource | MACULA Greek Linguistic Datasets, available at https://github.com/Clear-Bible/macula-greek/tree/main/Nestle1904/lowfat |
| dataSourceFormat | XML lowfat tree data |
| dataSourceLocation | https://github.com/saulocantanhede/tfgreek2/tree/main/xml/2022-11-01/gnt |
| description | frame |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:20Z |
