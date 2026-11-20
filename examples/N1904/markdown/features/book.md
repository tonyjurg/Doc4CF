# book.tf

[← Corpus index](../index.md)

book name (full name)

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The book feature stores the full New Testament book name (string) on all ten node types, with 27 distinct values. Populated counts span 27 book nodes to 137,779 word nodes; frequent values are Luke (70,494), Acts (66,507), and Matthew (65,999). Absent assignments mean no recorded value, not a negative class.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [book](../../structure.html#type-book) | 27 (100.0%) |
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

27 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "Luke" | 70,494 | 14.2% |
| "Acts" | 66,507 | 13.4% |
| "Matthew" | 65,999 | 13.3% |
| "John" | 55,439 | 11.1% |
| "Mark" | 40,545 | 8.1% |
| "Revelation" | 36,434 | 7.3% |
| "Romans" | 25,591 | 5.1% |
| "I_Corinthians" | 24,530 | 4.9% |
| "Hebrews" | 17,871 | 3.6% |
| "II_Corinthians" | 16,178 | 3.3% |
| "Ephesians" | 8,866 | 1.8% |
| "Galatians" | 7,944 | 1.6% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.verse.label` | {book} {chapter}:{verse} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/book.md) Source: `docs/features/book.md`; configured at `configuration.docs.featureBase` |

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
| description | book name (full name) |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:09Z |
