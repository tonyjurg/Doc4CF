# person.tf

[← Corpus index](../index.md)

grammatical person

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 18,807 (27.3%) |
| [subphrase](../../structure.html#type-subphrase) | 612 (0.5%) |
| [word](../../structure.html#type-word) | 19,419 (14.1%) |

## Frequent values

3 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "p3" | 25,494 | 65.6% |
| "p2" | 7,458 | 19.2% |
| "p1" | 5,886 | 15.2% |

## Correlated features

- [mood](mood.md) word · φ +0.80

- [tense](tense.md) word · φ +0.80

- [voice](voice.md) word · φ +0.80

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | person present when compared feature is present | person present when compared feature is absent |
| --- | --- | --- | --- |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.76 | 18,807 / 27,355 (68.8%) | 0 / 41,652 (0.0%) |
| [framespec](framespec.md) | +0.67 | 16,653 / 24,783 (67.2%) | 2,154 / 44,224 (4.9%) |
| [number](number.md) | +0.53 | 18,807 / 39,260 (47.9%) | 0 / 29,747 (0.0%) |
| [typems](typems.md) | -0.59 | 0 / 33,293 (0.0%) | 18,807 / 35,714 (52.7%) |
| [rule](rule.md) | -0.43 | 0 / 22,930 (0.0%) | 18,807 / 46,077 (40.8%) |

### subphrase nodes

| Compared feature(s) | φ | person present when compared feature is present | person present when compared feature is absent |
| --- | --- | --- | --- |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.78 | 612 / 1,002 (61.1%) | 0 / 115,176 (0.0%) |
| [subjrefspec](subjrefspec.md) | +0.57 | 336 / 567 (59.3%) | 276 / 115,611 (0.2%) |
| [framespec](framespec.md) | +0.50 | 334 / 710 (47.0%) | 278 / 115,468 (0.2%) |

### word nodes

| Compared feature(s) | φ | person present when compared feature is present | person present when compared feature is absent |
| --- | --- | --- | --- |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.80 | 19,419 / 28,357 (68.5%) | 0 / 109,422 (0.0%) |
| [framespec](framespec.md) | +0.72 | 16,987 / 25,493 (66.6%) | 2,432 / 112,286 (2.2%) |
| [role](role.md) | +0.55 | 18,998 / 46,792 (40.6%) | 421 / 90,987 (0.5%) |
| [case](case.md) | -0.47 | 0 / 79,518 (0.0%) | 19,419 / 58,261 (33.3%) |
| [gender](gender.md) | -0.44 | 0 / 73,975 (0.0%) | 19,419 / 63,804 (30.4%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/person.md) Source: `docs/features/person.md`; configured at `configuration.docs.featureBase` |

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
| description | grammatical person |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:15Z |
