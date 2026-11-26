# mood.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

verbal mood

## Generated description

The mood feature encodes verbal mood on word, phrase, and subphrase nodes in the Greek New Testament \(Nestle 1904\)\. Populated nodes carry string values such as indicative and participle; missing assignments mean no value is recorded, not a negative class\. It belongs to the morphology family and is related to morph, though that link is inferred\.

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
| `"indicative"` | 31,234 | 55.1% |
| `"participle"` | 13,306 | 23.5% |
| `"infinitive"` | 4,570 | 8.1% |
| `"imperative"` | 3,754 | 6.6% |
| `"subjunctive"` | 3,712 | 6.5% |
| `"optative"` | 138 | 0.2% |

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
| description | verbal mood |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:14Z |

</details>
