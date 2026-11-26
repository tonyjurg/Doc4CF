# verse.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · int

## Description

verse number, from ref attribute in xml

## Reviewed description

The verse feature records the verse number within a chapter, derived from the XML ref attribute. On verse nodes it identifies the verse itself; on word nodes it indicates the containing verse. On other populated node types it records the verse where the item begins. A sentence can span several verses, so this annotation does not establish verse containment. Verse numbers can have gaps.

Editorial clarification: [pinned N1904 verse documentation](https://github.com/CenterBLC/N1904/blob/3f53a5a9075cbca5c3001a000a7b004cdee251b6/docs/features/verse.md).

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
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
| `12` | 16,897 | 3.4% |
| `10` | 16,869 | 3.4% |
| `1` | 16,591 | 3.3% |
| `4` | 16,406 | 3.3% |
| `9` | 16,403 | 3.3% |
| `3` | 16,392 | 3.3% |
| `2` | 16,220 | 3.3% |
| `5` | 16,214 | 3.3% |
| `8` | 16,154 | 3.2% |
| `11` | 16,134 | 3.2% |
| `13` | 16,114 | 3.2% |
| `7` | 16,053 | 3.2% |

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
| description | verse number, from ref attribute in xml |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | int |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:19Z |

</details>
