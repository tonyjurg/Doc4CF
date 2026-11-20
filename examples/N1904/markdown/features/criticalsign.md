# criticalsign.tf

[← Corpus index](../index.md)

this is XML attribute criticalsign

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

criticalsign is a node feature carrying XML attribute criticalsign on phrase, subphrase, and word nodes in Greek New Testament (Nestle 1904). It records 7 distinct string values; populated counts are phrase 30, subphrase 33, word 63. Frequent values include em dash (50), parentheses ( and ) (22 each), double brackets [[ and ]] (14 each), and single brackets [ and ] (2 each). Overlap with after and punctuation is unverified; missing assignments mean no value is recorded.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 30 (0.0%) |
| [subphrase](../../structure.html#type-subphrase) | 33 (0.0%) |
| [word](../../structure.html#type-word) | 63 (0.0%) |

## Frequent values

7 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "—" | 50 | 39.7% |
| "(" | 22 | 17.5% |
| ")" | 22 | 17.5% |
| "[[" | 14 | 11.1% |
| "]]" | 14 | 11.1% |
| "[" | 2 | 1.6% |
| "]" | 2 | 1.6% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | criticalsign present when compared feature is present | criticalsign present when compared feature is absent |
| --- | --- | --- | --- |
| [before](before.md) | +0.36 | 8 / 16 (50.0%) | 22 / 68,991 (0.0%) |

### subphrase nodes

| Compared feature(s) | φ | criticalsign present when compared feature is present | criticalsign present when compared feature is absent |
| --- | --- | --- | --- |
| [before](before.md) | +0.45 | 11 / 18 (61.1%) | 22 / 116,160 (0.0%) |

### word nodes

| Compared feature(s) | φ | criticalsign present when compared feature is present | criticalsign present when compared feature is absent |
| --- | --- | --- | --- |
| [before](before.md) | +0.41 | 19 / 34 (55.9%) | 44 / 137,745 (0.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/criticalsign.md) Source: `docs/features/criticalsign.md`; configured at `configuration.docs.featureBase` |

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
| description | this is XML attribute criticalsign |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:11Z |
