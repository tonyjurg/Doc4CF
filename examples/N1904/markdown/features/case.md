# case.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

grammatical case

## Generated description

The case feature encodes grammatical case on word, phrase, and subphrase nodes in the Greek New Testament \(Nestle 1904\)\. It is a node feature whose value set includes nominative and accusative; nodes without a recorded value have no assignment rather than a negative class\. The case–morph relationship is inferred from metadata and marked for review\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 20,453 (29.6%) |
| subphrase | 59,065 (50.8%) |
| word | 79,518 (57.7%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"nominative"` | 48,394 | 30.4% |
| `"accusative"` | 46,062 | 29.0% |
| `"genitive"` | 39,030 | 24.5% |
| `"dative"` | 24,252 | 15.2% |
| `"vocative"` | 1,298 | 0.8% |

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
| description | grammatical case |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:10Z |

</details>
