# person.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

grammatical person

## Generated description

The person feature is a node feature assigning grammatical person to word, phrase, and subphrase nodes in the Greek New Testament \(Nestle 1904\)\. Observed values include p1 and p3\. Sources count populated nodes by type only; missing assignments mean no value is recorded, not a negative class\. The metadata describes the feature only as 'grammatical person,' so the meanings of p1 and p3 are not explicitly defined\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 18,807 (27.3%) |
| subphrase | 612 (0.5%) |
| word | 19,419 (14.1%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"p3"` | 25,494 | 65.6% |
| `"p2"` | 7,458 | 19.2% |
| `"p1"` | 5,886 | 15.2% |

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
| description | grammatical person |
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
