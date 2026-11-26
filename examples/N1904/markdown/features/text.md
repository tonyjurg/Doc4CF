# text.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

the text of a word

## Generated description

The text feature stores the surface text of a word as a string on word, phrase, and subphrase nodes\. It supports the default text\-orig\-full display format \(\{before\}\{text\}\{after\}\)\. Values such as καὶ and ὁ are Greek word forms; missing assignments mean no value is recorded, not a negative class\.

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
| `"καὶ"` | 17,090 | 6.2% |
| `"ὁ"` | 5,538 | 2.0% |
| `"ἐν"` | 5,368 | 1.9% |
| `"δὲ"` | 5,240 | 1.9% |
| `"τοῦ"` | 4,994 | 1.8% |
| `"εἰς"` | 3,510 | 1.3% |
| `"τὸ"` | 3,316 | 1.2% |
| `"τὸν"` | 3,112 | 1.1% |
| `"τὴν"` | 3,036 | 1.1% |
| `"αὐτοῦ"` | 2,822 | 1.0% |
| `"τῆς"` | 2,600 | 0.9% |
| `"ὅτι"` | 2,562 | 0.9% |

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
| description | the text of a word |
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
