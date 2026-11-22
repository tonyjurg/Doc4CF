# punctuation.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

punctuation found after a word

## Generated description

The node feature punctuation records punctuation found after a word on word, phrase, and subphrase nodes in the Greek New Testament \(Nestle 1904\)\. Populated nodes occur on all three types; missing assignments mean no value is recorded, not a negative class\. Observed values include "," and "\." among four distinct values\. Metadata describes it as punctuation after a word, but overlap with before, after, trailer, and criticalsign features is unverified\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 8,412 (12.2%) |
| subphrase | 10,097 (8.7%) |
| word | 18,509 (13.4%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `","` | 18,924 | 51.1% |
| `"."` | 11,434 | 30.9% |
| `"·"` | 4,718 | 12.7% |
| `";"` | 1,942 | 5.2% |

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
| description | punctuation found after a word |
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
