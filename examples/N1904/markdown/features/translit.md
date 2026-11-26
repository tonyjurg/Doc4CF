# translit.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

transliteration of the word surface text

## Generated description

The translit node feature records the transliteration of the word surface text\. Populated values appear on word, phrase, and subphrase nodes; missing assignments mean no value is recorded, not a negative class\. Frequent values include kai and en\. The feature supplies the translit placeholder in the text\-translit\-plain format alongside trailer, and may overlap in scope with text\.

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
| `"kai"` | 17,152 | 6.2% |
| `"en"` | 6,304 | 2.3% |
| `"o"` | 6,298 | 2.3% |
| `"to"` | 5,770 | 2.1% |
| `"de"` | 5,538 | 2.0% |
| `"ton"` | 5,526 | 2.0% |
| `"tou"` | 4,994 | 1.8% |
| `"eis"` | 3,702 | 1.3% |
| `"ten"` | 3,046 | 1.1% |
| `"auton"` | 3,028 | 1.1% |
| `"autou"` | 2,822 | 1.0% |
| `"e"` | 2,736 | 1.0% |

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
| description | transliteration of the word surface text |
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
