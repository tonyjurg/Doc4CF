# tense.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

verbal tense

## Generated description

The tense feature records verbal tense as a string annotation on populated word, phrase, and subphrase nodes in the Greek New Testament \(Nestle 1904\)\. Observed values include aorist and present\. Populated\-node counts cover these three node types; missing assignments mean no value is recorded, not a negative class\. Tense on phrase and subphrase nodes may indicate inherited annotation, but the inventory does not explain this\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 27,355 (39.6%) |
| subphrase | 1,002 (0.9%) |
| word | 28,357 (20.6%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"aorist"` | 23,606 | 41.6% |
| `"present"` | 23,158 | 40.8% |
| `"imperfect"` | 3,378 | 6.0% |
| `"future"` | 3,252 | 5.7% |
| `"perfect"` | 3,144 | 5.5% |
| `"pluperfect"` | 176 | 0.3% |

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
| description | verbal tense |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:17Z |

</details>
