# subjrefspec.tf

[← Corpus index](../index.md)

this is XML attribute subjrefspec

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 16,008 (23.2%) |
| [subphrase](../../structure.html#type-subphrase) | 567 (0.5%) |
| [word](../../structure.html#type-word) | 16,575 (12.0%) |

## Frequent values

5,567 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "n46003022002" | 344 | 1.0% |
| "n66001009002" | 262 | 0.8% |
| "n45001001001" | 208 | 0.6% |
| "n47010001004" | 208 | 0.6% |
| "n41006030007" | 190 | 0.6% |
| "n50001001001" | 184 | 0.6% |
| "n40005001015" | 156 | 0.5% |
| "n49003001013" | 146 | 0.4% |
| "n51001002007" | 142 | 0.4% |
| "n48001001001" | 132 | 0.4% |
| "n42020034005" | 118 | 0.4% |
| "n47001001001" | 112 | 0.3% |

## Correlated features

- [mood](mood.md) subphrase · φ +0.75

- [tense](tense.md) subphrase · φ +0.75

- [voice](voice.md) subphrase · φ +0.75

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | subjrefspec present when compared feature is present | subjrefspec present when compared feature is absent |
| --- | --- | --- | --- |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.68 | 16,008 / 27,355 (58.5%) | 0 / 41,652 (0.0%) |
| [framespec](framespec.md) | +0.67 | 15,132 / 24,783 (61.1%) | 876 / 44,224 (2.0%) |
| [person](person.md) | +0.43 | 9,896 / 18,807 (52.6%) | 6,112 / 50,200 (12.2%) |
| [typems](typems.md) | -0.53 | 0 / 33,293 (0.0%) | 16,008 / 35,714 (44.8%) |
| [rule](rule.md) | -0.39 | 0 / 22,930 (0.0%) | 16,008 / 46,077 (34.7%) |

### subphrase nodes

| Compared feature(s) | φ | subjrefspec present when compared feature is present | subjrefspec present when compared feature is absent |
| --- | --- | --- | --- |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.75 | 567 / 1,002 (56.6%) | 0 / 115,176 (0.0%) |
| [framespec](framespec.md) | +0.75 | 477 / 710 (67.2%) | 90 / 115,468 (0.1%) |
| [person](person.md) | +0.57 | 336 / 612 (54.9%) | 231 / 115,566 (0.2%) |

### word nodes

| Compared feature(s) | φ | subjrefspec present when compared feature is present | subjrefspec present when compared feature is absent |
| --- | --- | --- | --- |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.73 | 16,575 / 28,357 (58.5%) | 0 / 109,422 (0.0%) |
| [framespec](framespec.md) | +0.72 | 15,609 / 25,493 (61.2%) | 966 / 112,286 (0.9%) |
| [person](person.md) | +0.51 | 10,232 / 19,419 (52.7%) | 6,343 / 118,360 (5.4%) |
| [typems](typems.md) | -0.26 | 0 / 44,458 (0.0%) | 16,575 / 93,321 (17.8%) |
| [case](case.md) | -0.22 | 4,754 / 79,518 (6.0%) | 11,821 / 58,261 (20.3%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/subjrefspec.md) Source: `docs/features/subjrefspec.md`; configured at `configuration.docs.featureBase` |

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
| description | this is XML attribute subjrefspec |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:17Z |
