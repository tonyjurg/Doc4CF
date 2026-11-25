# rule.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

syntactical rule

## Generated description

The rule feature assigns a string\-valued syntactical rule to individual nodes\. Populated values occur on clause, group, phrase, sentence, subphrase, and wg nodes; book, chapter, verse, and word nodes have no recorded values\. It contributes to node labels together with typems, role, and junction \(wg\) or typ, function, rela, typems, and role \(other types\)\. Attested values include DetNP and PrepNp\. Missing assignments mean no value is recorded, not a negative class\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| sentence | 7,173 (89.5%) |
| group | 870 (9.7%) |
| clause | 37,786 (88.9%) |
| wg | 93,234 (87.2%) |
| phrase | 22,930 (33.2%) |
| subphrase | 24,475 (21.1%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"DetNP"` | 31,392 | 16.8% |
| `"PrepNp"` | 22,088 | 11.8% |
| `"NPofNP"` | 13,638 | 7.3% |
| `"Conj-CL"` | 11,152 | 6.0% |
| `"CLaCL"` | 7,658 | 4.1% |
| `"sub-CL"` | 6,058 | 3.2% |
| `"V2CL"` | 5,686 | 3.0% |
| `"V-O"` | 5,450 | 2.9% |
| `"DetCL"` | 4,022 | 2.2% |
| `"Np-Appos"` | 3,816 | 2.0% |
| `"V-ADV"` | 3,374 | 1.8% |
| `"ClCl"` | 3,158 | 1.7% |

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
| description | syntactical rule |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:16Z |

</details>
