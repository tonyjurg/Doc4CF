# bookshort.tf

[← Corpus index](../index.md)

book name (abbreviated) from ref attribute in xml

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

bookshort is a node feature storing the abbreviated book name from the ref attribute in the Nestle 1904 XML source. It has 27 distinct values and appears on book, sentence, group, clause, phrase, subphrase, wg, and word nodes. Frequent values include LUK (69,321), ACT (65,477), MAT (64,903), and JHN (54,539). No values are recorded on chapter or verse nodes.

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

27 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "LUK" | 69,321 | 14.2% |
| "ACT" | 65,477 | 13.4% |
| "MAT" | 64,903 | 13.3% |
| "JHN" | 54,539 | 11.1% |
| "MRK" | 39,855 | 8.1% |
| "REV" | 36,007 | 7.4% |
| "ROM" | 25,143 | 5.1% |
| "1CO" | 24,077 | 4.9% |
| "HEB" | 17,555 | 3.6% |
| "2CO" | 15,909 | 3.3% |
| "EPH" | 8,705 | 1.8% |
| "GAL" | 7,789 | 1.6% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/bookshort.md) Source: `docs/features/bookshort.md`; configured at `configuration.docs.featureBase` |

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
| description | book name (abbreviated) from ref attribute in xml |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:10Z |
