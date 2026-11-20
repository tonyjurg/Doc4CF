# num.tf

[← Corpus index](../index.md)

generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse.

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

num is a node feature storing a generated integer absent from the XML. Book nodes are numbered Matthew=1 through Revelation=27; sentence nodes per chapter; word nodes per verse. Populated values also appear on clause, group, phrase, subphrase, and wg nodes, but not chapter or verse. Frequent values include 17 (200 nodes) and 27 (198 nodes).

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [book](../../structure.html#type-book) | 27 (100.0%) |
| [sentence](../../structure.html#type-sentence) | 8,011 (100.0%) |
| [group](../../structure.html#type-group) | 8,945 (100.0%) |
| [clause](../../structure.html#type-clause) | 42,506 (100.0%) |
| [wg](../../structure.html#type-wg) | 106,868 (100.0%) |
| [phrase](../../structure.html#type-phrase) | 69,007 (100.0%) |
| [subphrase](../../structure.html#type-subphrase) | 116,178 (100.0%) |
| [word](../../structure.html#type-word) | 137,779 (100.0%) |

## Frequent values

25,041 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 17 | 200 | 0.0% |
| 27 | 198 | 0.0% |
| 19 | 198 | 0.0% |
| 7 | 198 | 0.0% |
| 15 | 197 | 0.0% |
| 12 | 195 | 0.0% |
| 26 | 195 | 0.0% |
| 30 | 192 | 0.0% |
| 10 | 190 | 0.0% |
| 14 | 189 | 0.0% |
| 39 | 189 | 0.0% |
| 21 | 189 | 0.0% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/num.md) Source: `docs/features/num.md`; configured at `configuration.docs.featureBase` |

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
| description | generated number (not in xml): book: (Matthew=1, Mark=2, ..., Revelation=27); sentence: numbered per chapter; word: numbered per verse. |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | int |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:14Z |
