# gender.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

grammatical gender

## Generated description

The gender feature records grammatical gender as a string annotation on populated word, phrase, and subphrase nodes in the Greek New Testament \(Nestle 1904\) Text\-Fabric corpus\. Observed values include masculine and feminine\. Missing assignments indicate no recorded value rather than a negative class\. It belongs to the verified morphology feature family and is related to morph, though that relationship is inferred\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 17,658 (25.6%) |
| subphrase | 56,317 (48.5%) |
| word | 73,975 (53.7%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"masculine"` | 82,972 | 56.1% |
| `"feminine"` | 37,472 | 25.3% |
| `"neuter"` | 27,506 | 18.6% |

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
| description | grammatical gender |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:12Z |

</details>
