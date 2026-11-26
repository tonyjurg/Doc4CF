# oslots.tf

[← Corpus index](../index.md)

**Edge feature** · UTF\-8 · str

## Description

Maps each non\-slot node to the slot nodes that make up its textual span\. This core edge feature links structural units to the slots they cover and supports retrieving a node's text and relating it to the corpus's smallest units\. Its edges express slot membership; they do not by themselves identify semantic, syntactic, or parent\-child relationships between non\-slot units\.

## Generated description

The oslots edge feature maps non\-slot nodes such as clause to the word slots they cover, supporting retrieval of a node's constituent slots and text span\. These links express slot membership only and do not by themselves establish parenthood, semantic relations, or ordering among non\-slot nodes\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| book | 27 (100.0%) |
| chapter | 260 (100.0%) |
| verse | 7,944 (100.0%) |
| sentence | 8,011 (100.0%) |
| group | 8,945 (100.0%) |
| clause | 42,506 (100.0%) |
| wg | 106,868 (100.0%) |
| phrase | 69,007 (100.0%) |
| subphrase | 116,178 (100.0%) |

## Observed edge connections

| Source node type | Target node type | Edges |
| --- | --- | ---: |
| book | word | 137,779 |
| chapter | word | 137,779 |
| clause | word | 355,238 |
| group | word | 62,700 |
| phrase | word | 131,031 |
| sentence | word | 137,779 |
| subphrase | word | 186,032 |
| verse | word | 137,779 |
| wg | word | 735,001 |

### Targets per connected source node

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | ---: | ---: | ---: | ---: |
| book | 27 | 219 | 1739 | 19,456 |
| chapter | 260 | 185 | 493 | 1,239 |
| clause | 42,506 | 1 | 6 | 164 |
| group | 8,945 | 2 | 5 | 87 |
| phrase | 69,007 | 1 | 1 | 154 |
| sentence | 8,011 | 1 | 14 | 165 |
| subphrase | 116,178 | 1 | 1 | 153 |
| verse | 7,944 | 2 | 17 | 58 |
| wg | 106,868 | 1 | 4 | 165 |

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
