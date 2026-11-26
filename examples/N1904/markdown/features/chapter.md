# chapter.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · int

## Description

chapter number, from ref attribute in xml

## Generated description

The chapter feature records the chapter number from the XML ref attribute as an integer\. Values are observed on chapter, clause, group, phrase, sentence, subphrase, verse, wg, and word nodes, reflecting section membership across the corpus\. Example values include 1 and 2\. Missing assignments indicate no recorded value rather than a negative class\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| chapter | 260 (100.0%) |
| verse | 7,944 (100.0%) |
| sentence | 8,011 (100.0%) |
| group | 8,945 (100.0%) |
| clause | 42,506 (100.0%) |
| wg | 106,868 (100.0%) |
| phrase | 69,007 (100.0%) |
| subphrase | 116,178 (100.0%) |
| word | 137,779 (100.0%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `1` | 42,442 | 8.5% |
| `2` | 35,630 | 7.2% |
| `4` | 31,176 | 6.3% |
| `3` | 31,095 | 6.3% |
| `5` | 28,180 | 5.7% |
| `6` | 24,499 | 4.9% |
| `9` | 23,000 | 4.6% |
| `7` | 22,640 | 4.6% |
| `11` | 22,533 | 4.5% |
| `12` | 22,364 | 4.5% |
| `8` | 21,510 | 4.3% |
| `10` | 21,100 | 4.2% |

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
| description | chapter number, from ref attribute in xml |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | int |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:10Z |

</details>
