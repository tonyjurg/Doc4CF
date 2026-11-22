# after.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

material after the end of the word

## Generated description

The node feature after stores string\-valued material after the end of the word\. It is populated on word, phrase, and subphrase nodes; absent assignments mean no value is recorded, not a negative class\. The feature feeds the text\-orig\-full format \{before\}\{text\}\{after\}\. Common values include ', ' and '\. ', so it may represent trailing spacing or punctuation, although its boundary with punctuation and trailer remains unverified\.

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
| `" "` | 238,522 | 86.6% |
| `", "` | 18,878 | 6.9% |
| `". "` | 11,408 | 4.1% |
| `"· "` | 4,710 | 1.7% |
| `"; "` | 1,938 | 0.7% |
| `",— "` | 36 | 0.0% |
| `"— "` | 14 | 0.0% |
| `"). "` | 12 | 0.0% |
| `".]] "` | 8 | 0.0% |
| `"·— "` | 8 | 0.0% |
| `",) "` | 6 | 0.0% |
| `"]]. "` | 4 | 0.0% |

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
| description | material after the end of the word |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:09Z |

</details>
