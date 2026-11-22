# morph.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

morphological code

## Generated description

The morph node feature assigns a string\-valued morphological code to word, phrase, and subphrase nodes\. Attested values include CONJ and V\-PAI\-3S\. The metadata labels it 'morphological code\.' Populated nodes are counted by type in sources; absent assignments mean no value is recorded rather than a negative class\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 46,077 (66.8%) |
| subphrase | 91,702 (78.9%) |
| word | 137,779 (100.0%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"CONJ"` | 32,632 | 11.8% |
| `"PREP"` | 21,136 | 7.7% |
| `"ADV"` | 7,616 | 2.8% |
| `"N-NSM"` | 6,950 | 2.5% |
| `"N-GSM"` | 5,870 | 2.1% |
| `"T-NSM"` | 5,810 | 2.1% |
| `"N-ASF"` | 5,740 | 2.1% |
| `"PRT-N"` | 5,402 | 2.0% |
| `"N-ASM"` | 4,912 | 1.8% |
| `"V-PAI-3S"` | 4,542 | 1.6% |
| `"N-GSF"` | 4,384 | 1.6% |
| `"T-GSM"` | 3,840 | 1.4% |

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
| description | morphological code |
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
