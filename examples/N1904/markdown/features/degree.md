# degree.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

grammatical degree

## Generated description

The degree feature stores grammatical degree on word, phrase, and subphrase nodes in the Greek New Testament \(Nestle 1904\) corpus\. Observed values include comparative and superlative\. Because sources counts populated nodes only, nodes without a value have no assignment rather than a negative class\. It belongs to the morphology family and may mark inflectional degree, but the inventory does not explicitly limit its part\-of\-speech scope\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 151 (0.2%) |
| subphrase | 362 (0.3%) |
| word | 513 (0.4%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"comparative"` | 626 | 61.0% |
| `"superlative"` | 400 | 39.0% |

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
| description | grammatical degree |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:11Z |

</details>
