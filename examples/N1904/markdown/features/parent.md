# parent.tf

[← Corpus index](../index.md)

**Edge feature** · UTF\-8 · str

## Description

parent relationship between words

## Generated description

The parent edge feature records directed links from source nodes to target nodes across multiple node types\. Each clause, group, phrase, sentence, and wg source has exactly one outgoing edge, while each word source has exactly two\. Observed endpoints span clause, group, phrase, sentence, subphrase, wg, book, and word nodes, with word\-to\-wg links being the most numerous endpoint pair\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| sentence | 8,011 (100.0%) |
| group | 8,945 (100.0%) |
| clause | 42,506 (100.0%) |
| wg | 106,867 (100.0%) |
| phrase | 69,007 (100.0%) |
| word | 137,779 (100.0%) |

## Observed edge connections

| Source node type | Target node type | Edges |
| --- | --- | ---: |
| clause | clause | 26,004 |
| clause | group | 6,054 |
| clause | phrase | 1,107 |
| clause | sentence | 8,156 |
| clause | subphrase | 1,185 |
| group | clause | 4,237 |
| group | group | 60 |
| group | phrase | 1,946 |
| group | sentence | 602 |
| group | subphrase | 2,100 |
| phrase | clause | 65,096 |
| phrase | sentence | 3,911 |
| sentence | book | 8,011 |
| wg | book | 8,011 |
| wg | wg | 98,856 |
| word | clause | 51,312 |
| word | group | 9,949 |
| word | phrase | 31,863 |
| word | sentence | 8,228 |
| word | subphrase | 36,427 |
| word | wg | 137,779 |

### Targets per connected source node

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | ---: | ---: | ---: | ---: |
| word | 137,779 | 2 | 2 | 2 |
| clause | 42,506 | 1 | 1 | 1 |
| group | 8,945 | 1 | 1 | 1 |
| phrase | 69,007 | 1 | 1 | 1 |
| sentence | 8,011 | 1 | 1 | 1 |
| wg | 106,867 | 1 | 1 | 1 |

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
| description | parent relationship between words |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:21Z |

</details>
