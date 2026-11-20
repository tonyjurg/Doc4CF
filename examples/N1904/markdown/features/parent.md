# parent.tf

[← Corpus index](../index.md)

parent relationship between words

Edge · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sentence](../../structure.html#type-sentence) | 8,011 (100.0%) |
| [group](../../structure.html#type-group) | 8,945 (100.0%) |
| [clause](../../structure.html#type-clause) | 42,506 (100.0%) |
| [wg](../../structure.html#type-wg) | 106,867 (100.0%) |
| [phrase](../../structure.html#type-phrase) | 69,007 (100.0%) |
| [word](../../structure.html#type-word) | 137,779 (100.0%) |

## Points to

| Node type | Incoming edges |
| --- | --- |
| [book](../../structure.html#type-book) | 16,022 |
| [sentence](../../structure.html#type-sentence) | 20,897 |
| [group](../../structure.html#type-group) | 16,063 |
| [clause](../../structure.html#type-clause) | 146,649 |
| [wg](../../structure.html#type-wg) | 236,635 |
| [phrase](../../structure.html#type-phrase) | 34,916 |
| [subphrase](../../structure.html#type-subphrase) | 39,712 |

## Observed edge connections

Counts show recorded edges for each source and target node-type pair.

| Source node type | Target node type | Edges |
| --- | --- | --- |
| [clause](../../structure.html#type-clause) | [clause](../../structure.html#type-clause) | 26,004 |
| [clause](../../structure.html#type-clause) | [group](../../structure.html#type-group) | 6,054 |
| [clause](../../structure.html#type-clause) | [phrase](../../structure.html#type-phrase) | 1,107 |
| [clause](../../structure.html#type-clause) | [sentence](../../structure.html#type-sentence) | 8,156 |
| [clause](../../structure.html#type-clause) | [subphrase](../../structure.html#type-subphrase) | 1,185 |
| [group](../../structure.html#type-group) | [clause](../../structure.html#type-clause) | 4,237 |
| [group](../../structure.html#type-group) | [group](../../structure.html#type-group) | 60 |
| [group](../../structure.html#type-group) | [phrase](../../structure.html#type-phrase) | 1,946 |
| [group](../../structure.html#type-group) | [sentence](../../structure.html#type-sentence) | 602 |
| [group](../../structure.html#type-group) | [subphrase](../../structure.html#type-subphrase) | 2,100 |
| [phrase](../../structure.html#type-phrase) | [clause](../../structure.html#type-clause) | 65,096 |
| [phrase](../../structure.html#type-phrase) | [sentence](../../structure.html#type-sentence) | 3,911 |
| [sentence](../../structure.html#type-sentence) | [book](../../structure.html#type-book) | 8,011 |
| [wg](../../structure.html#type-wg) | [book](../../structure.html#type-book) | 8,011 |
| [wg](../../structure.html#type-wg) | [wg](../../structure.html#type-wg) | 98,856 |
| [word](../../structure.html#type-word) | [clause](../../structure.html#type-clause) | 51,312 |
| [word](../../structure.html#type-word) | [group](../../structure.html#type-group) | 9,949 |
| [word](../../structure.html#type-word) | [phrase](../../structure.html#type-phrase) | 31,863 |
| [word](../../structure.html#type-word) | [sentence](../../structure.html#type-sentence) | 8,228 |
| [word](../../structure.html#type-word) | [subphrase](../../structure.html#type-subphrase) | 36,427 |
| [word](../../structure.html#type-word) | [wg](../../structure.html#type-wg) | 137,779 |

## Targets per connected source node

Summary for source nodes with at least one recorded edge.

| Source node type | Source nodes | Minimum | Median | Maximum |
| --- | --- | --- | --- | --- |
| [word](../../structure.html#type-word) | 137,779 | 2 | 2 | 2 |
| [clause](../../structure.html#type-clause) | 42,506 | 1 | 1 | 1 |
| [group](../../structure.html#type-group) | 8,945 | 1 | 1 | 1 |
| [phrase](../../structure.html#type-phrase) | 69,007 | 1 | 1 | 1 |
| [sentence](../../structure.html#type-sentence) | 8,011 | 1 | 1 | 1 |
| [wg](../../structure.html#type-wg) | 106,867 | 1 | 1 | 1 |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/parent.md) Source: `docs/features/parent.md`; configured at `configuration.docs.featureBase` |

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
| description | parent relationship between words |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:21Z |
