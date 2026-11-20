# chapter.tf

[← Corpus index](../index.md)

chapter number, from ref attribute in xml

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The chapter node feature stores the chapter number taken from the ref attribute in the XML source. Integer values appear on chapter, clause, group, phrase, sentence, subphrase, verse, wg, and word nodes, with source counts from 260 to 137,779 nodes; no values are recorded on book nodes. Twenty-eight distinct values occur, with 1 appearing on 42,442 nodes and 12 on 21,100 nodes. It supports biblical reference navigation alongside book and verse.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [chapter](../../structure.html#type-chapter) | 260 (100.0%) |
| [verse](../../structure.html#type-verse) | 7,944 (100.0%) |
| [sentence](../../structure.html#type-sentence) | 8,011 (100.0%) |
| [group](../../structure.html#type-group) | 8,945 (100.0%) |
| [clause](../../structure.html#type-clause) | 42,506 (100.0%) |
| [wg](../../structure.html#type-wg) | 106,868 (100.0%) |
| [phrase](../../structure.html#type-phrase) | 69,007 (100.0%) |
| [subphrase](../../structure.html#type-subphrase) | 116,178 (100.0%) |
| [word](../../structure.html#type-word) | 137,779 (100.0%) |

## Frequent values

28 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 42,442 | 8.5% |
| 2 | 35,630 | 7.2% |
| 4 | 31,176 | 6.3% |
| 3 | 31,095 | 6.3% |
| 5 | 28,180 | 5.7% |
| 6 | 24,499 | 4.9% |
| 9 | 23,000 | 4.6% |
| 7 | 22,640 | 4.6% |
| 11 | 22,533 | 4.5% |
| 12 | 22,364 | 4.5% |
| 8 | 21,510 | 4.3% |
| 10 | 21,100 | 4.2% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.verse.label` | {book} {chapter}:{verse} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/chapter.md) Source: `docs/features/chapter.md`; configured at `configuration.docs.featureBase` |

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
| description | chapter number, from ref attribute in xml |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | int |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:10Z |
