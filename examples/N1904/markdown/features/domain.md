# domain.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

domain

## Generated description

The domain node feature assigns string values to phrase, subphrase, and word nodes in the Greek New Testament \(Nestle 1904\)\. Observed values such as 092004 and 089017 may denote textual or linguistic domains from the MACULA source data, but the metadata does not define their semantics\. Sources record populated nodes only; missing assignments mean no value is stored, not a negative class\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 43,153 (62.5%) |
| subphrase | 83,726 (72.1%) |
| word | 126,879 (92.1%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"092004"` | 52,258 | 20.6% |
| `"089017"` | 8,740 | 3.4% |
| `"093001"` | 7,342 | 2.9% |
| `"033006"` | 6,446 | 2.5% |
| `"012001"` | 6,000 | 2.4% |
| `"089015"` | 5,620 | 2.2% |
| `"092003"` | 4,888 | 1.9% |
| `"069002"` | 3,714 | 1.5% |
| `"092001"` | 3,690 | 1.5% |
| `"089023"` | 3,560 | 1.4% |
| `"013001"` | 3,422 | 1.3% |
| `"089007"` | 3,152 | 1.2% |

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
| description | domain |
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
