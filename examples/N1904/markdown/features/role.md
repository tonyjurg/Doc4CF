# role.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

role

## Generated description

The node feature role assigns a syntactic role string to clause, group, phrase, subphrase, wg, and word nodes in the Greek New Testament \(Nestle 1904\)\. Observed values include v and adv\. It appears in node labels for clauses, groups, phrases, sentences, subphrases, and word groups\. Missing assignments mean no value is recorded, not a negative class\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| group | 335 (3.7%) |
| clause | 12,795 (30.1%) |
| wg | 37,426 (35.0%) |
| phrase | 69,007 (100.0%) |
| subphrase | 2,081 (1.8%) |
| word | 46,792 (34.0%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"v"` | 50,344 | 29.9% |
| `"adv"` | 43,154 | 25.6% |
| `"o"` | 26,988 | 16.0% |
| `"s"` | 22,336 | 13.3% |
| `"p"` | 7,348 | 4.4% |
| `"io"` | 5,316 | 3.2% |
| `"vc"` | 5,186 | 3.1% |
| `"apposition"` | 4,878 | 2.9% |
| `"aux"` | 2,112 | 1.3% |
| `"o2"` | 718 | 0.4% |
| `"topic"` | 46 | 0.0% |
| `"ellipsis"` | 4 | 0.0% |

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
| description | role |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:16Z |

</details>
