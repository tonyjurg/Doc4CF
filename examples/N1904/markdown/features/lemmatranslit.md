# lemmatranslit.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

transliteration of the word lemma

## Generated description

The lemmatranslit node feature stores a string transliteration of a word lemma\. Values are populated on phrase, subphrase, and word nodes; absent entries mean no value is recorded, not a negative class\. Example transliterations are o and kai\. The feature is used in the lex\-translit\-plain text format alongside trailer\.

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
| `"o"` | 39,600 | 14.4% |
| `"kai"` | 17,956 | 6.5% |
| `"autos"` | 11,122 | 4.0% |
| `"su"` | 5,784 | 2.1% |
| `"de"` | 5,584 | 2.0% |
| `"en"` | 5,486 | 2.0% |
| `"ego"` | 5,134 | 1.9% |
| `"eimi"` | 4,914 | 1.8% |
| `"lego"` | 4,510 | 1.6% |
| `"eis"` | 4,204 | 1.5% |
| `"os"` | 3,818 | 1.4% |
| `"ou"` | 3,292 | 1.2% |

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
| description | transliteration of the word lemma |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:13Z |

</details>
