# discontinuous.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · int

## Description

1 if the word is out of sequence in the xml

## Generated description

The discontinuous node feature records an integer flag on phrase, subphrase, and word nodes in the Greek New Testament \(Nestle 1904\)\. A value of 1 marks a node as out of sequence in the XML source; populated nodes are counted by type, while unpopulated nodes have no recorded value rather than a negative class\. The phrase “word” in the description may refer generically to annotated units\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 645 (0.9%) |
| subphrase | 5,389 (4.6%) |
| word | 6,034 (4.4%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `1` | 12,068 | 100.0% |

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
| description | 1 if the word is out of sequence in the xml |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | int |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:11Z |

</details>
