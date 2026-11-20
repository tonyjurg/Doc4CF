# case.tf

[← Corpus index](../index.md)

grammatical case

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The case feature records grammatical case on word, phrase, and subphrase nodes in the Greek New Testament (Nestle 1904) Text-Fabric corpus. It is a string-valued node feature in the morphology family with five observed values: nominative (48,394), accusative (46,062), genitive (39,030), dative (24,252), and vocative (1,298). Populated counts are phrase 20,453, subphrase 59,065, and word 79,518; missing assignments mean no value is recorded, not a negative class.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 20,453 (29.6%) |
| [subphrase](../../structure.html#type-subphrase) | 59,065 (50.8%) |
| [word](../../structure.html#type-word) | 79,518 (57.7%) |

## Frequent values

5 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "nominative" | 48,394 | 30.4% |
| "accusative" | 46,062 | 29.0% |
| "genitive" | 39,030 | 24.5% |
| "dative" | 24,252 | 15.2% |
| "vocative" | 1,298 | 0.8% |

## Correlated features

- [number](number.md) subphrase · φ +0.99

- [gender](gender.md) subphrase · φ +0.95

- [typems](typems.md) word · φ +0.59

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | case present when compared feature is present | case present when compared feature is absent |
| --- | --- | --- | --- |
| [gender](gender.md) | +0.90 | 17,658 / 17,658 (100.0%) | 2,795 / 51,349 (5.4%) |
| [number](number.md) | +0.56 | 20,453 / 39,260 (52.1%) | 0 / 29,747 (0.0%) |
| [referent](referent.md) | +0.53 | 7,643 / 7,827 (97.6%) | 12,810 / 61,180 (20.9%) |
| [rule](rule.md) | -0.46 | 0 / 22,930 (0.0%) | 20,453 / 46,077 (44.4%) |
| [typ](typ.md) | -0.43 | 0 / 20,768 (0.0%) | 20,453 / 48,239 (42.4%) |

### subphrase nodes

| Compared feature(s) | φ | case present when compared feature is present | case present when compared feature is absent |
| --- | --- | --- | --- |
| [number](number.md) | +0.99 | 59,065 / 59,677 (99.0%) | 0 / 56,501 (0.0%) |
| [gender](gender.md) | +0.95 | 56,317 / 56,317 (100.0%) | 2,748 / 59,861 (4.6%) |
| [domain](domain.md), [ln](ln.md) | +0.57 | 57,546 / 83,726 (68.7%) | 1,519 / 32,452 (4.7%) |
| [rule](rule.md) | -0.53 | 0 / 24,475 (0.0%) | 59,065 / 91,703 (64.4%) |
| [typ](typ.md) | -0.49 | 0 / 21,853 (0.0%) | 59,065 / 94,325 (62.6%) |

### word nodes

| Compared feature(s) | φ | case present when compared feature is present | case present when compared feature is absent |
| --- | --- | --- | --- |
| [gender](gender.md) | +0.92 | 73,975 / 73,975 (100.0%) | 5,543 / 63,804 (8.7%) |
| [number](number.md) | +0.73 | 79,518 / 98,937 (80.4%) | 0 / 38,842 (0.0%) |
| [typems](typems.md) | +0.59 | 44,430 / 44,458 (99.9%) | 35,088 / 93,321 (37.6%) |
| [person](person.md) | -0.47 | 0 / 19,419 (0.0%) | 79,518 / 118,360 (67.2%) |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | -0.35 | 6,653 / 28,357 (23.5%) | 72,865 / 109,422 (66.6%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/case.md) Source: `docs/features/case.md`; configured at `configuration.docs.featureBase` |

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
| description | grammatical case |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:10Z |
