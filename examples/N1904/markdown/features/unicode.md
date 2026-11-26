# unicode.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

word in unicode characters plus material after it

## Generated description

The unicode node feature stores word surface text in Unicode characters plus material after the word\. Populated values appear on phrase, subphrase, and word nodes; sources counts only nodes with recorded values, so absences are not negative assignments\. Frequent values include καὶ and ὁ\. It may represent the primary Greek surface form, but the inventory does not designate unicode as the exclusive text convention among overlapping word\-text features\.

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
| `"καὶ"` | 17,082 | 6.2% |
| `"ὁ"` | 5,536 | 2.0% |
| `"ἐν"` | 5,366 | 1.9% |
| `"δὲ"` | 5,238 | 1.9% |
| `"τοῦ"` | 4,994 | 1.8% |
| `"εἰς"` | 3,510 | 1.3% |
| `"τὸ"` | 3,314 | 1.2% |
| `"τὸν"` | 3,112 | 1.1% |
| `"τὴν"` | 3,036 | 1.1% |
| `"τῆς"` | 2,600 | 0.9% |
| `"ὅτι"` | 2,562 | 0.9% |
| `"τῷ"` | 2,442 | 0.9% |

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
| description | word in unicode characters plus material after it |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:19Z |

</details>
