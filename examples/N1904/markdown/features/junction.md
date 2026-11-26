# junction.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

type of junction

## Generated description

The junction feature is a node feature recording the type of junction on clause, phrase, subphrase, and wg nodes, with observed values coordinate and subordinate\. It appears in clause and wg node label templates alongside role and typems\. Missing assignments mean no value is recorded rather than a negative class\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| clause | 17,741 (41.7%) |
| wg | 17,921 (16.8%) |
| phrase | 57 (0.1%) |
| subphrase | 123 (0.1%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"coordinate"` | 18,734 | 52.3% |
| `"subordinate"` | 17,108 | 47.7% |

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
| description | type of junction |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:13Z |

</details>
