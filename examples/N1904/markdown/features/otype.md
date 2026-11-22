# otype.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

Maps every Text\-Fabric node to its node type\. The type identifies what kind of structural unit the node represents, such as a slot or a larger unit defined by the corpus\. This core node feature lets tools select nodes by type and interpret where other features apply\. Type labels describe the corpus data model; their names alone do not establish the linguistic or semantic role of a unit\.

## Generated description

The otype feature assigns every Text\-Fabric node a type label identifying the kind of structural unit it represents, such as word or book\. Other features use these labels to specify where they apply\. The corpus uses multiple node types; labels alone do not establish linguistic meaning, hierarchy, or population totals\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| book | 27 (100.0%) |
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
| `"word"` | 137,779 | 27.7% |
| `"subphrase"` | 116,178 | 23.4% |
| `"wg"` | 106,868 | 21.5% |
| `"phrase"` | 69,007 | 13.9% |
| `"clause"` | 42,506 | 8.5% |
| `"group"` | 8,945 | 1.8% |
| `"sentence"` | 8,011 | 1.6% |
| `"verse"` | 7,944 | 1.6% |
| `"chapter"` | 260 | 0.1% |
| `"book"` | 27 | 0.0% |

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
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:15Z |

</details>
