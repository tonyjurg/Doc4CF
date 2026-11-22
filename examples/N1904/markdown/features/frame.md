# frame.tf

[← Corpus index](../index.md)

**Edge feature** · UTF\-8 · str

## Description

frame

## Generated description

frame is a directed edge feature in the Greek New Testament \(Nestle 1904\) Text\-Fabric corpus, linking word nodes to word nodes\. It records 25,491 source word nodes with 43,893 target word endpoints; each source has 1 to 18 links \(median 2\)\. Edge values are strings, with frequent values A0 and A1\. The relation semantics are undocumented, so it may encode a syntactic frame relation\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| word | 25,491 (18.5%) |

## Observed edge connections

| Source node type | Target node type | Edges |
| --- | --- | ---: |
| word | word | 43,893 |

### Targets per connected source node

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | ---: | ---: | ---: | ---: |
| word | 25,491 | 1 | 2 | 18 |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"A0"` | 25,654 | 58.4% |
| `"A1"` | 15,570 | 35.5% |
| `"A2"` | 2,577 | 5.9% |
| `"AA2"` | 92 | 0.2% |

<details>
<summary>Source metadata</summary>

| Field | Value |
| --- | --- |
| edgeValues |  |
| author | Evangelists and apostles |
| converterSourceLocation | https://github\.com/saulocantanhede/tfgreek2/tree/main/programs |
| converterVersion | 1\.0\.0 \(July 9, 2024\) |
| converters | Saulo de Oliveira Cantanhêde, Tony Jurg, Dirk Roorda |
| dataSource | MACULA Greek Linguistic Datasets, available at https://github\.com/Clear\-Bible/macula\-greek/tree/main/Nestle1904/lowfat |
| dataSourceFormat | XML lowfat tree data |
| dataSourceLocation | https://github\.com/saulocantanhede/tfgreek2/tree/main/xml/2022\-11\-01/gnt |
| description | frame |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:20Z |

</details>
