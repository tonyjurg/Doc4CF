# framespec.tf

[← Corpus index](../index.md)

this is XML attribute framespec

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

framespec is a node feature recording the XML attribute framespec as a string. Values are populated on phrase (24,783), subphrase (710), and word (25,493) nodes; it is absent from other observed node types. The 20,299 distinct values include identifiers such as A0:n00000000000 (1,792 occurrences) and A1:n00000000000 (338). It may encode frame or slot specifications from the XML lowfat source, but the inventory does not define its syntax or semantics.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 24,783 (35.9%) |
| [subphrase](../../structure.html#type-subphrase) | 710 (0.6%) |
| [word](../../structure.html#type-word) | 25,493 (18.5%) |

## Frequent values

20,299 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "A0:n00000000000" | 1,792 | 3.5% |
| "A1:n00000000000" | 338 | 0.7% |
| "A0:n47010001004" | 94 | 0.2% |
| "A0:n46003022002" | 92 | 0.2% |
| "A0:n41006030007" | 68 | 0.1% |
| "A0:n66001009002" | 68 | 0.1% |
| "A0:n40005001015" | 62 | 0.1% |
| "A0:n45001001001" | 58 | 0.1% |
| "A0:n50001001001" | 54 | 0.1% |
| "A0:n42020034005" | 50 | 0.1% |
| "A0:n47005004007" | 50 | 0.1% |
| "A0:n47001001001" | 48 | 0.1% |

## Correlated features

- [mood](mood.md) word · φ +0.94

- [tense](tense.md) word · φ +0.94

- [voice](voice.md) word · φ +0.94

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | framespec present when compared feature is present | framespec present when compared feature is absent |
| --- | --- | --- | --- |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.92 | 24,783 / 27,355 (90.6%) | 0 / 41,652 (0.0%) |
| [person](person.md) | +0.67 | 16,653 / 18,807 (88.5%) | 8,130 / 50,200 (16.2%) |
| [subjrefspec](subjrefspec.md) | +0.67 | 15,132 / 16,008 (94.5%) | 9,651 / 52,999 (18.2%) |
| [typems](typems.md) | -0.72 | 0 / 33,293 (0.0%) | 24,783 / 35,714 (69.4%) |
| [rule](rule.md) | -0.53 | 0 / 22,930 (0.0%) | 24,783 / 46,077 (53.8%) |

### subphrase nodes

| Compared feature(s) | φ | framespec present when compared feature is present | framespec present when compared feature is absent |
| --- | --- | --- | --- |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.84 | 710 / 1,002 (70.9%) | 0 / 115,176 (0.0%) |
| [subjrefspec](subjrefspec.md) | +0.75 | 477 / 567 (84.1%) | 233 / 115,611 (0.2%) |
| [person](person.md) | +0.50 | 334 / 612 (54.6%) | 376 / 115,566 (0.3%) |

### word nodes

| Compared feature(s) | φ | framespec present when compared feature is present | framespec present when compared feature is absent |
| --- | --- | --- | --- |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.94 | 25,493 / 28,357 (89.9%) | 0 / 109,422 (0.0%) |
| [subjrefspec](subjrefspec.md) | +0.72 | 15,609 / 16,575 (94.2%) | 9,884 / 121,204 (8.2%) |
| [person](person.md) | +0.72 | 16,987 / 19,419 (87.5%) | 8,506 / 118,360 (7.2%) |
| [typems](typems.md) | -0.33 | 0 / 44,458 (0.0%) | 25,493 / 93,321 (27.3%) |
| [case](case.md) | -0.32 | 6,385 / 79,518 (8.0%) | 19,108 / 58,261 (32.8%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/framespec.md) Source: `docs/features/framespec.md`; configured at `configuration.docs.featureBase` |

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
| description | this is XML attribute framespec |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:12Z |
