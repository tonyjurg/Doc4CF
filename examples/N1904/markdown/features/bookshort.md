# bookshort.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

book name \(abbreviated\) from ref attribute in xml

## Generated description

bookshort assigns an abbreviated book name \(string\) taken from the ref attribute in the source XML\. Values are populated on book, clause, group, phrase, sentence, subphrase, wg, and word nodes; examples include MAT and LUK\. Populated\-node counts do not indicate negative assignments, and the inventory does not state whether non\-book nodes inherit the value or carry it independently\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| book | 27 (100.0%) |
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
| `"LUK"` | 69,321 | 14.2% |
| `"ACT"` | 65,477 | 13.4% |
| `"MAT"` | 64,903 | 13.3% |
| `"JHN"` | 54,539 | 11.1% |
| `"MRK"` | 39,855 | 8.1% |
| `"REV"` | 36,007 | 7.4% |
| `"ROM"` | 25,143 | 5.1% |
| `"1CO"` | 24,077 | 4.9% |
| `"HEB"` | 17,555 | 3.6% |
| `"2CO"` | 15,909 | 3.3% |
| `"EPH"` | 8,705 | 1.8% |
| `"GAL"` | 7,789 | 1.6% |

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
| description | book name \(abbreviated\) from ref attribute in xml |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:10Z |

</details>
