# referent.tf

[← Corpus index](../index.md)

number of referent

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 7,827 (11.3%) |
| [subphrase](../../structure.html#type-subphrase) | 6,644 (5.7%) |
| [word](../../structure.html#type-word) | 14,471 (10.5%) |

## Frequent values

6,099 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "n40005001015" | 224 | 0.8% |
| "n43014023002" | 158 | 0.5% |
| "n46003022002" | 154 | 0.5% |
| "n45001001001" | 152 | 0.5% |
| "n47008001004" | 146 | 0.5% |
| "n50001001001" | 116 | 0.4% |
| "n51001002007" | 114 | 0.4% |
| "n43013023006 n43013037003 n43014005003 n43014008003 n43014022003" | 108 | 0.4% |
| "n41003007003" | 96 | 0.3% |
| "n42020034005" | 94 | 0.3% |
| "n41006030007" | 88 | 0.3% |
| "n43017001003" | 88 | 0.3% |

## Correlated features

- [case](case.md) phrase · φ +0.53

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | referent present when compared feature is present | referent present when compared feature is absent |
| --- | --- | --- | --- |
| [case](case.md) | +0.53 | 7,643 / 20,453 (37.4%) | 184 / 48,554 (0.4%) |
| [typems](typems.md) | +0.32 | 7,223 / 33,293 (21.7%) | 604 / 35,714 (1.7%) |
| [gender](gender.md) | +0.30 | 4,891 / 17,658 (27.7%) | 2,936 / 51,349 (5.7%) |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | -0.29 | 0 / 27,355 (0.0%) | 7,827 / 41,652 (18.8%) |
| [framespec](framespec.md) | -0.27 | 0 / 24,783 (0.0%) | 7,827 / 44,224 (17.7%) |

### subphrase nodes

| Compared feature(s) | φ | referent present when compared feature is present | referent present when compared feature is absent |
| --- | --- | --- | --- |
| [case](case.md) | +0.24 | 6,641 / 59,065 (11.2%) | 3 / 57,113 (0.0%) |
| [number](number.md) | +0.24 | 6,641 / 59,677 (11.1%) | 3 / 56,501 (0.0%) |
| [typems](typems.md) | +0.23 | 6,370 / 56,111 (11.4%) | 274 / 60,067 (0.5%) |
| [rule](rule.md) | -0.13 | 0 / 24,475 (0.0%) | 6,644 / 91,703 (7.2%) |
| [typ](typ.md) | -0.12 | 0 / 21,853 (0.0%) | 6,644 / 94,325 (7.0%) |

### word nodes

| Compared feature(s) | φ | referent present when compared feature is present | referent present when compared feature is absent |
| --- | --- | --- | --- |
| [typems](typems.md) | +0.45 | 13,593 / 44,458 (30.6%) | 878 / 93,321 (0.9%) |
| [case](case.md) | +0.28 | 14,284 / 79,518 (18.0%) | 187 / 58,261 (0.3%) |
| [number](number.md) | +0.20 | 14,284 / 98,937 (14.4%) | 187 / 38,842 (0.5%) |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | -0.17 | 0 / 28,357 (0.0%) | 14,471 / 109,422 (13.2%) |
| [framespec](framespec.md) | -0.16 | 0 / 25,493 (0.0%) | 14,471 / 112,286 (12.9%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/referent.md) Source: `docs/features/referent.md`; configured at `configuration.docs.featureBase` |

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
| description | number of referent |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:16Z |
