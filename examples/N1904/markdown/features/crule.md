# crule.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

clause rule \(from xml attribute Rule\)

## Generated description

The crule node feature stores a clause rule taken from the XML attribute Rule\. Populated values appear on clause, sentence, and wg nodes; missing nodes have no recorded value rather than a negative assignment\. Two distinct string values, ClCl and ClCl2, occur, which may indicate a two\-way clause\-rule distinction, but their meanings are undefined in the metadata\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| sentence | 838 (10.5%) |
| clause | 4,720 (11.1%) |
| wg | 5,558 (5.2%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"ClCl"` | 8,616 | 77.5% |
| `"ClCl2"` | 2,500 | 22.5% |

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
| description | clause rule \(from xml attribute Rule\) |
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
