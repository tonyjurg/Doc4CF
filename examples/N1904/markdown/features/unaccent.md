# unaccent.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

word in unicode characters without accents and diacritical markers

## Generated description

The unaccent node feature assigns a Unicode string to word, phrase, and subphrase nodes, representing word surface text with accents and diacritical markers removed\. Populated node types are word, phrase, and subphrase; missing assignments mean no value is recorded\. Example values include και and ο\. The feature is used in the text\-unaccent\-plain display format together with trailer\.

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
| `"και"` | 17,152 | 6.2% |
| `"ο"` | 6,038 | 2.2% |
| `"δε"` | 5,528 | 2.0% |
| `"εν"` | 5,504 | 2.0% |
| `"του"` | 4,994 | 1.8% |
| `"εις"` | 3,702 | 1.3% |
| `"το"` | 3,328 | 1.2% |
| `"τον"` | 3,124 | 1.1% |
| `"την"` | 3,046 | 1.1% |
| `"αυτου"` | 2,822 | 1.0% |
| `"η"` | 2,736 | 1.0% |
| `"της"` | 2,600 | 0.9% |

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
| description | word in unicode characters without accents and diacritical markers |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:19Z |

</details>
