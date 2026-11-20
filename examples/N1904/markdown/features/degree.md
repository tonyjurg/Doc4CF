# degree.tf

[← Corpus index](../index.md)

grammatical degree

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The degree feature records grammatical degree on word, phrase, and subphrase nodes in the Greek New Testament (Nestle 1904). It is populated on 513 word nodes, 151 phrase nodes, and 362 subphrase nodes. Missing assignments indicate no recorded value rather than a negative class. The two observed values are comparative (626 occurrences) and superlative (400 occurrences), suggesting it marks adjectival or adverbial comparison, though the inventory does not explicitly define the value semantics.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 151 (0.2%) |
| [subphrase](../../structure.html#type-subphrase) | 362 (0.3%) |
| [word](../../structure.html#type-word) | 513 (0.4%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "comparative" | 626 | 61.0% |
| "superlative" | 400 | 39.0% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/degree.md) Source: `docs/features/degree.md`; configured at `configuration.docs.featureBase` |

### Source metadata

| Field | Value |
| --- | --- |
| author | Evangelists and apostles |
| converterSourceLocation | https://github.com/saulocantanhede/tfgreek2/tree/main/programs |
| converterVersion | 1.0.0 (July 9, 2024) |
| converters | Saulo de Oliveira Cantanhêde, Tony Jurg, Dirk Roorda |
| dataSource | MACULA Greek Linguistic Datasets, available at https://github.com/Clear-Bible/macula-greek/tree/main/Nestle1904/lowfat |
| dataSourceFormat | XML lowfat tree data |
| dataSourceLocation | https://github.com/saulocantanhede/tfgreek2/tree/main/xml/2022-11-01/gnt |
| description | grammatical degree |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:11Z |
