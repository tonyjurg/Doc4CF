# function.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

this is XML attribute function

## Generated description

The node feature function stores the XML attribute function as a string on clause, phrase, sentence, wg, and word nodes\. It appears in node labels for clause, group, phrase, sentence, and subphrase alongside typ and rela\. Common values such as Pred and Cmpl suggest syntactic function, but the source description only calls it an XML attribute, so the precise semantic scope is not explicitly defined\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| sentence | 778 (9.7%) |
| clause | 21,568 (50.7%) |
| wg | 45,276 (42.4%) |
| phrase | 69,007 (100.0%) |
| word | 46,077 (33.4%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"Pred"` | 49,714 | 27.2% |
| `"Cmpl"` | 26,024 | 14.2% |
| `"Subj"` | 20,396 | 11.2% |
| `"Objc"` | 18,674 | 10.2% |
| `"PreC"` | 12,344 | 6.8% |
| `"Adv"` | 11,192 | 6.1% |
| `"Pred-Obj"` | 5,452 | 3.0% |
| `"Pred-Cmpl"` | 3,818 | 2.1% |
| `"Cmpl-Pred"` | 2,370 | 1.3% |
| `"Obj-Pred"` | 2,154 | 1.2% |
| `"Cmpl-Pred-Obj"` | 1,368 | 0.7% |
| `"Subj-Pred"` | 1,278 | 0.7% |

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
| description | this is XML attribute function |
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
