# num.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · int

## Description

generated number \(not in xml\): book: \(Matthew=1, Mark=2, \.\.\., Revelation=27\); sentence: numbered per chapter; word: numbered per verse\.

## Generated description

The num feature is a node\-level generated integer absent from the source XML\. It numbers books 1 \(Matthew\) through 27 \(Revelation\), sentences within chapters, and words within verses\. Values are populated on book, sentence, word, clause, group, phrase, subphrase, and wg nodes; missing assignments mean no recorded value, not a negative class\.

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
| `17` | 200 | 0.0% |
| `27` | 198 | 0.0% |
| `19` | 198 | 0.0% |
| `7` | 198 | 0.0% |
| `15` | 197 | 0.0% |
| `12` | 195 | 0.0% |
| `26` | 195 | 0.0% |
| `30` | 192 | 0.0% |
| `10` | 190 | 0.0% |
| `14` | 189 | 0.0% |
| `39` | 189 | 0.0% |
| `21` | 189 | 0.0% |

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
| description | generated number \(not in xml\): book: \(Matthew=1, Mark=2, \.\.\., Revelation=27\); sentence: numbered per chapter; word: numbered per verse\. |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | int |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:14Z |

</details>
