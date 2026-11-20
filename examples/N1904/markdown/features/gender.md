# gender.tf

[← Corpus index](../index.md)

grammatical gender

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

gender encodes grammatical gender on phrase, subphrase, and word nodes in the Greek New Testament (Nestle 1904). Observed values are masculine (82,972 nodes), feminine (37,472), and neuter (27,506). Populated counts are phrase 17,658, subphrase 56,317, and word 73,975; unlisted nodes have no recorded value, not a negative assignment. It belongs to the morphology feature family and is related to morph.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 17,658 (25.6%) |
| [subphrase](../../structure.html#type-subphrase) | 56,317 (48.5%) |
| [word](../../structure.html#type-word) | 73,975 (53.7%) |

## Frequent values

3 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "masculine" | 82,972 | 56.1% |
| "feminine" | 37,472 | 25.3% |
| "neuter" | 27,506 | 18.6% |

## Correlated features

- [case](case.md) subphrase · φ +0.95

- [number](number.md) subphrase · φ +0.94

- [domain](domain.md) subphrase · φ +0.56

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | gender present when compared feature is present | gender present when compared feature is absent |
| --- | --- | --- | --- |
| [case](case.md) | +0.90 | 17,658 / 20,453 (86.3%) | 0 / 48,554 (0.0%) |
| [number](number.md) | +0.51 | 17,658 / 39,260 (45.0%) | 0 / 29,747 (0.0%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +0.41 | 17,658 / 46,077 (38.3%) | 0 / 22,930 (0.0%) |
| [rule](rule.md) | -0.41 | 0 / 22,930 (0.0%) | 17,658 / 46,077 (38.3%) |
| [typ](typ.md) | -0.38 | 0 / 20,768 (0.0%) | 17,658 / 48,239 (36.6%) |

### subphrase nodes

| Compared feature(s) | φ | gender present when compared feature is present | gender present when compared feature is absent |
| --- | --- | --- | --- |
| [case](case.md) | +0.95 | 56,317 / 59,065 (95.3%) | 0 / 57,113 (0.0%) |
| [number](number.md) | +0.94 | 56,317 / 59,677 (94.4%) | 0 / 56,501 (0.0%) |
| [domain](domain.md), [ln](ln.md) | +0.56 | 55,102 / 83,726 (65.8%) | 1,215 / 32,452 (3.7%) |
| [rule](rule.md) | -0.50 | 0 / 24,475 (0.0%) | 56,317 / 91,703 (61.4%) |
| [typ](typ.md) | -0.47 | 0 / 21,853 (0.0%) | 56,317 / 94,325 (59.7%) |

### word nodes

| Compared feature(s) | φ | gender present when compared feature is present | gender present when compared feature is absent |
| --- | --- | --- | --- |
| [case](case.md) | +0.92 | 73,975 / 79,518 (93.0%) | 0 / 58,261 (0.0%) |
| [number](number.md) | +0.67 | 73,975 / 98,937 (74.8%) | 0 / 38,842 (0.0%) |
| [typems](typems.md) | +0.47 | 38,887 / 44,458 (87.5%) | 35,088 / 93,321 (37.6%) |
| [person](person.md) | -0.44 | 0 / 19,419 (0.0%) | 73,975 / 118,360 (62.5%) |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | -0.31 | 6,653 / 28,357 (23.5%) | 67,322 / 109,422 (61.5%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/gender.md) Source: `docs/features/gender.md`; configured at `configuration.docs.featureBase` |

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
| description | grammatical gender |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:12Z |
