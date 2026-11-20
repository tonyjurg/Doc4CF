# mood.tf

[← Corpus index](../index.md)

verbal mood

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The mood feature records verbal mood as a string-valued node annotation in the Greek New Testament (Nestle 1904). Six values are observed: indicative (31,234), participle (13,306), infinitive (4,570), imperative (3,754), subjunctive (3,712), and optative (138). Populated nodes include 28,357 word nodes, 27,355 phrase nodes, and 1,002 subphrase nodes; missing assignments indicate no recorded value, not a negative class.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 27,355 (39.6%) |
| [subphrase](../../structure.html#type-subphrase) | 1,002 (0.9%) |
| [word](../../structure.html#type-word) | 28,357 (20.6%) |

## Frequent values

6 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "indicative" | 31,234 | 55.1% |
| "participle" | 13,306 | 23.5% |
| "infinitive" | 4,570 | 8.1% |
| "imperative" | 3,754 | 6.6% |
| "subjunctive" | 3,712 | 6.5% |
| "optative" | 138 | 0.2% |

## Correlated features

- [tense](tense.md) phrase · φ +1.00

- [voice](voice.md) phrase · φ +1.00

- [framespec](framespec.md) word · φ +0.94

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | mood present when compared feature is present | mood present when compared feature is absent |
| --- | --- | --- | --- |
| [tense](tense.md), [voice](voice.md) | +1.00 | 27,355 / 27,355 (100.0%) | 0 / 41,652 (0.0%) |
| [framespec](framespec.md) | +0.92 | 24,783 / 24,783 (100.0%) | 2,572 / 44,224 (5.8%) |
| [person](person.md) | +0.76 | 18,807 / 18,807 (100.0%) | 8,548 / 50,200 (17.0%) |
| [typems](typems.md) | -0.78 | 0 / 33,293 (0.0%) | 27,355 / 35,714 (76.6%) |
| [rule](rule.md) | -0.57 | 0 / 22,930 (0.0%) | 27,355 / 46,077 (59.4%) |

### subphrase nodes

| Compared feature(s) | φ | mood present when compared feature is present | mood present when compared feature is absent |
| --- | --- | --- | --- |
| [tense](tense.md), [voice](voice.md) | +1.00 | 1,002 / 1,002 (100.0%) | 0 / 115,176 (0.0%) |
| [framespec](framespec.md) | +0.84 | 710 / 710 (100.0%) | 292 / 115,468 (0.3%) |
| [person](person.md) | +0.78 | 612 / 612 (100.0%) | 390 / 115,566 (0.3%) |

### word nodes

| Compared feature(s) | φ | mood present when compared feature is present | mood present when compared feature is absent |
| --- | --- | --- | --- |
| [tense](tense.md), [voice](voice.md) | +1.00 | 28,357 / 28,357 (100.0%) | 0 / 109,422 (0.0%) |
| [framespec](framespec.md) | +0.94 | 25,493 / 25,493 (100.0%) | 2,864 / 112,286 (2.6%) |
| [person](person.md) | +0.80 | 19,419 / 19,419 (100.0%) | 8,938 / 118,360 (7.6%) |
| [case](case.md) | -0.35 | 6,653 / 79,518 (8.4%) | 21,704 / 58,261 (37.3%) |
| [typems](typems.md) | -0.35 | 0 / 44,458 (0.0%) | 28,357 / 93,321 (30.4%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/mood.md) Source: `docs/features/mood.md`; configured at `configuration.docs.featureBase` |

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
| description | verbal mood |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:14Z |
