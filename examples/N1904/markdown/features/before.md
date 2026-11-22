# before.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

this is XML attribute before

## Generated description

The node feature \`before\` stores the XML attribute \`before\` as a string on word, phrase, and subphrase nodes; \`sources\` records populated nodes only, so unlisted types have no value\. It feeds the default text format \`\{before\}\{text\}\{after\}\` and may mark punctuation or material preceding a word, exemplified by values such as \`—\` and \`\(\`, though its boundary with \`punctuation\` is unverified\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| phrase | 16 (0.0%) |
| subphrase | 18 (0.0%) |
| word | 34 (0.0%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"—"` | 32 | 47.1% |
| `"("` | 20 | 29.4% |
| `"[["` | 14 | 20.6% |
| `"["` | 2 | 2.9% |

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
| description | this is XML attribute before |
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
