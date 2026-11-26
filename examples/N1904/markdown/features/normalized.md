# normalized.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

lemma normalized

## Generated description

The normalized feature is a node\-level string feature for the Nestle 1904 Greek New Testament\. Its terse metadata describes values as 'lemma normalized'\. Values are populated on word, subphrase, and phrase nodes; nodes lacking an assignment have no recorded value rather than a negative class\. The exact normalization rule is not documented beyond the metadata, and coverage on phrase and subphrase nodes is unexplained\.

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
| `"καί"` | 17,152 | 6.2% |
| `"ὁ"` | 5,538 | 2.0% |
| `"δέ"` | 5,528 | 2.0% |
| `"ἐν"` | 5,368 | 1.9% |
| `"τοῦ"` | 4,994 | 1.8% |
| `"εἰς"` | 3,510 | 1.3% |
| `"τό"` | 3,328 | 1.2% |
| `"τόν"` | 3,124 | 1.1% |
| `"τήν"` | 3,046 | 1.1% |
| `"αὐτοῦ"` | 2,822 | 1.0% |
| `"τῆς"` | 2,600 | 0.9% |
| `"ὅτι"` | 2,562 | 0.9% |

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
| description | lemma normalized |
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
