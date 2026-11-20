# oslots.tf

[← Corpus index](../index.md)

Maps each non-slot node to the slot nodes that make up its textual span. This core edge feature links structural units to the slots they cover and supports retrieving a node's text and relating it to the corpus's smallest units. Its edges express slot membership; they do not by themselves identify semantic, syntactic, or parent-child relationships between non-slot units.

Edge · UTF-8 · str

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

## Points to

| Node type | Incoming edges |
| --- | --- |
| [word](../../structure.html#type-word) | 2,021,118 |

## Observed edge connections

Counts show recorded edges for each source and target node-type pair.

| Source node type | Target node type | Edges |
| --- | --- | --- |
| [book](../../structure.html#type-book) | [word](../../structure.html#type-word) | 137,779 |
| [chapter](../../structure.html#type-chapter) | [word](../../structure.html#type-word) | 137,779 |
| [clause](../../structure.html#type-clause) | [word](../../structure.html#type-word) | 355,238 |
| [group](../../structure.html#type-group) | [word](../../structure.html#type-word) | 62,700 |
| [phrase](../../structure.html#type-phrase) | [word](../../structure.html#type-word) | 131,031 |
| [sentence](../../structure.html#type-sentence) | [word](../../structure.html#type-word) | 137,779 |
| [subphrase](../../structure.html#type-subphrase) | [word](../../structure.html#type-word) | 186,032 |
| [verse](../../structure.html#type-verse) | [word](../../structure.html#type-word) | 137,779 |
| [wg](../../structure.html#type-wg) | [word](../../structure.html#type-word) | 735,001 |

## Targets per connected source node

Summary for source nodes with at least one recorded edge.

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | --- | --- | --- | --- |
| [book](../../structure.html#type-book) | 27 | 219 | 1739 | 19,456 |
| [chapter](../../structure.html#type-chapter) | 260 | 185 | 493 | 1,239 |
| [clause](../../structure.html#type-clause) | 42,506 | 1 | 6 | 164 |
| [group](../../structure.html#type-group) | 8,945 | 2 | 5 | 87 |
| [phrase](../../structure.html#type-phrase) | 69,007 | 1 | 1 | 154 |
| [sentence](../../structure.html#type-sentence) | 8,011 | 1 | 14 | 165 |
| [subphrase](../../structure.html#type-subphrase) | 116,178 | 1 | 1 | 153 |
| [verse](../../structure.html#type-verse) | 7,944 | 2 | 17 | 58 |
| [wg](../../structure.html#type-wg) | 106,868 | 1 | 4 | 165 |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/oslots.md) Source: `docs/features/oslots.md`; configured at `configuration.docs.featureBase` |

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
| dateWritten | 2024-07-28T01:57:20Z |
