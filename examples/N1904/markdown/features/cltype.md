# cltype.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

clause type

## Generated description

cltype is a node feature recording clause type as a string\. Values are observed on clause, sentence, and wg nodes; nodes without assignments have no recorded value rather than a negative class\. Frequent values include VerbElided and Verbless\. The inventory notes cltype overlaps with clausetype, also described as clause type, but their relationship is unclear\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| sentence | 125 (1.6%) |
| clause | 2,718 (6.4%) |
| wg | 2,843 (2.7%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"VerbElided"` | 2,100 | 36.9% |
| `"Verbless"` | 1,922 | 33.8% |
| `"Minor"` | 1,664 | 29.3% |

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
| description | clause type |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:11Z |

</details>
