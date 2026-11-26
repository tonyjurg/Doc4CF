# subjref.tf

[← Corpus index](../index.md)

**Edge feature** · UTF\-8 · str

## Description

number of subject referent

## Generated description

The subjref edge feature records links from word nodes to word nodes in the Greek New Testament \(Nestle 1904\)\. Its metadata gloss is “number of subject referent,” but the inventory does not define the linguistic relation or fully specify edge direction, so subject reference is a plausible but unverified interpretation\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| word | 16,575 (12.0%) |

## Observed edge connections

| Source node type | Target node type | Edges |
| --- | --- | ---: |
| word | word | 20,312 |

### Targets per connected source node

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | ---: | ---: | ---: | ---: |
| word | 16,575 | 1 | 1 | 18 |

<details>
<summary>Source metadata</summary>

| Field | Value |
| --- | --- |
| author | Evangelists and apostles |
| converterSourceLocation | https://github\.com/saulocantanhede/tfgreek2/tree/main/programs |
| converterVersion | 1\.0\.0 \(July 9, 2024\) |
| converters | Saulo de Oliveira Cantanhêde, Tony Jurg, Dirk Roorda |
| dataSource | MACULA Greek Linguistic Datasets, available at https://github\.com/Clear\-Bible/macula\-greek/tree/main/Nestle1904/lowfat |
| dataSourceFormat | XML lowfat tree data |
| dataSourceLocation | https://github\.com/saulocantanhede/tfgreek2/tree/main/xml/2022\-11\-01/gnt |
| description | number of subject referent |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:41Z |

</details>
