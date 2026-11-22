# ref.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

biblical reference with word counting

## Generated description

The ref node feature stores a biblical reference with word counting, exemplified by values such as MAT 1:1\!1\. It is observed on phrase, subphrase, and word nodes; sources mark populated nodes only, and missing assignments mean no value is recorded, not a negative class\. The value may combine section identifiers book, chapter, verse with the generated word number num\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 46,077 (66.8%) |
| subphrase | 91,702 (78.9%) |
| word | 137,779 (100.0%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"MAT 1:1!1"` | 2 | 0.0% |
| `"MAT 1:1!2"` | 2 | 0.0% |
| `"MAT 1:1!3"` | 2 | 0.0% |
| `"MAT 1:1!4"` | 2 | 0.0% |
| `"MAT 1:1!5"` | 2 | 0.0% |
| `"MAT 1:1!6"` | 2 | 0.0% |
| `"MAT 1:1!7"` | 2 | 0.0% |
| `"MAT 1:1!8"` | 2 | 0.0% |
| `"MAT 1:2!1"` | 2 | 0.0% |
| `"MAT 1:2!2"` | 2 | 0.0% |
| `"MAT 1:2!3"` | 2 | 0.0% |
| `"MAT 1:2!4"` | 2 | 0.0% |

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
| description | biblical reference with word counting |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:15Z |

</details>
