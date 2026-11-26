# typems.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

morphological type \(on word\), syntactical type \(on sentence, group, clause, phrase or wg\)

## Generated description

typems is a node\-level string feature assigning morphological type on word nodes and syntactical type on clause, group, phrase, sentence, subphrase, and wg nodes\. Values are populated on those seven node types; missing assignments record no value rather than a negative class\. Attested values such as common and modifier\-scope may indicate word class or syntactic scope categories\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| sentence | 5,946 (74.2%) |
| group | 8,945 (100.0%) |
| clause | 8,873 (20.9%) |
| wg | 68,710 (64.3%) |
| phrase | 33,293 (48.2%) |
| subphrase | 56,111 (48.3%) |
| word | 44,458 (32.3%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"modifier-scope"` | 59,290 | 26.2% |
| `"common"` | 47,288 | 20.9% |
| `"wrapper-clause-scope"` | 24,332 | 10.8% |
| `"personal"` | 23,042 | 10.2% |
| `"wrapper-scope"` | 22,528 | 10.0% |
| `"conjuncted-wg"` | 16,150 | 7.1% |
| `"group"` | 9,914 | 4.4% |
| `"proper"` | 9,278 | 4.1% |
| `"demonstrative"` | 3,444 | 1.5% |
| `"modifier-clause-scope"` | 3,424 | 1.5% |
| `"relative"` | 3,348 | 1.5% |
| `"apposition-group"` | 1,782 | 0.8% |

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
| description | morphological type \(on word\), syntactical type \(on sentence, group, clause, phrase or wg\) |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:18Z |

</details>
