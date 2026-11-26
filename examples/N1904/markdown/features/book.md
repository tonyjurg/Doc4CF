# book.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

book name \(full name\)

## Generated description

The book feature stores the full biblical book name as a string annotation on corpus nodes\. It is populated on all ten node types—book, chapter, verse, sentence, group, clause, wg, phrase, subphrase, and word—with sources recording populated nodes per type\. Values such as Luke and Matthew locate text within the Nestle 1904 Greek New Testament and feed the verse label template \{book\} \{chapter\}:\{verse\}\.

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
| `"Luke"` | 70,494 | 14.2% |
| `"Acts"` | 66,507 | 13.4% |
| `"Matthew"` | 65,999 | 13.3% |
| `"John"` | 55,439 | 11.1% |
| `"Mark"` | 40,545 | 8.1% |
| `"Revelation"` | 36,434 | 7.3% |
| `"Romans"` | 25,591 | 5.1% |
| `"I_Corinthians"` | 24,530 | 4.9% |
| `"Hebrews"` | 17,871 | 3.6% |
| `"II_Corinthians"` | 16,178 | 3.3% |
| `"Ephesians"` | 8,866 | 1.8% |
| `"Galatians"` | 7,944 | 1.6% |

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
| description | book name \(full name\) |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:09Z |

</details>
