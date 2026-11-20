# otype.tf

[← Corpus index](../index.md)

Maps every Text-Fabric node to its node type. The type identifies what kind of structural unit the node represents, such as a slot or a larger unit defined by the corpus. This core node feature lets tools select nodes by type and interpret where other features apply. Type labels describe the corpus data model; their names alone do not establish the linguistic or semantic role of a unit.

Node · UTF-8 · str

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

10 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "word" | 137,779 | 27.7% |
| "subphrase" | 116,178 | 23.4% |
| "wg" | 106,868 | 21.5% |
| "phrase" | 69,007 | 13.9% |
| "clause" | 42,506 | 8.5% |
| "group" | 8,945 | 1.8% |
| "sentence" | 8,011 | 1.6% |
| "verse" | 7,944 | 1.6% |
| "chapter" | 260 | 0.1% |
| "book" | 27 | 0.0% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/otype.md) Source: `docs/features/otype.md`; configured at `configuration.docs.featureBase` |

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
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:15Z |
