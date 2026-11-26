# articular.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · int

## Description

1 if the sentence, group, clause, phrase or wg has an article

## Generated description

The articular feature is a node\-level integer annotation marking whether a sentence, group, clause, phrase, subphrase, or wg node has an article\. Populated values are observed on clause, group, phrase, sentence, subphrase, and wg nodes; the single attested value is 1\. Missing assignments indicate no recorded article rather than a negative class\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| sentence | 229 (2.9%) |
| group | 181 (2.0%) |
| clause | 3,386 (8.0%) |
| wg | 28,772 (26.9%) |
| phrase | 13,079 (19.0%) |
| subphrase | 11,897 (10.2%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `1` | 57,544 | 100.0% |

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
| description | 1 if the sentence, group, clause, phrase or wg has an article |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | int |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:09Z |

</details>
