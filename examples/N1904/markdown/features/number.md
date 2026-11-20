# number.tf

[← Corpus index](../index.md)

grammatical number

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The node feature number records grammatical number (singular or plural) on word, phrase, and subphrase nodes in the Greek New Testament (Nestle 1904). Populated counts are word 98,937, phrase 39,260, and subphrase 59,677; frequent values are singular 139,692 and plural 58,182. Missing assignments indicate no value recorded, not a negative class. Its relation to morph is inferred, not explicitly defined.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 39,260 (56.9%) |
| [subphrase](../../structure.html#type-subphrase) | 59,677 (51.4%) |
| [word](../../structure.html#type-word) | 98,937 (71.8%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "singular" | 139,692 | 70.6% |
| "plural" | 58,182 | 29.4% |

## Correlated features

- [case](case.md) subphrase · φ +0.99

- [gender](gender.md) subphrase · φ +0.94

- [after](after.md) phrase · φ +0.81

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | number present when compared feature is present | number present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +0.81 | 39,260 / 46,077 (85.2%) | 0 / 22,930 (0.0%) |
| [domain](domain.md), [ln](ln.md) | +0.76 | 37,084 / 43,153 (85.9%) | 2,176 / 25,854 (8.4%) |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.57 | 25,127 / 27,355 (91.9%) | 14,133 / 41,652 (33.9%) |
| [rule](rule.md) | -0.81 | 0 / 22,930 (0.0%) | 39,260 / 46,077 (85.2%) |
| [typ](typ.md) | -0.75 | 0 / 20,768 (0.0%) | 39,260 / 48,239 (81.4%) |

### subphrase nodes

| Compared feature(s) | φ | number present when compared feature is present | number present when compared feature is absent |
| --- | --- | --- | --- |
| [case](case.md) | +0.99 | 59,065 / 59,065 (100.0%) | 612 / 57,113 (1.1%) |
| [gender](gender.md) | +0.94 | 56,317 / 56,317 (100.0%) | 3,360 / 59,861 (5.6%) |
| [domain](domain.md), [ln](ln.md) | +0.58 | 57,997 / 83,726 (69.3%) | 1,680 / 32,452 (5.2%) |
| [rule](rule.md) | -0.53 | 0 / 24,475 (0.0%) | 59,677 / 91,703 (65.1%) |
| [typ](typ.md) | -0.49 | 0 / 21,853 (0.0%) | 59,677 / 94,325 (63.3%) |

### word nodes

| Compared feature(s) | φ | number present when compared feature is present | number present when compared feature is absent |
| --- | --- | --- | --- |
| [case](case.md) | +0.73 | 79,518 / 79,518 (100.0%) | 19,419 / 58,261 (33.3%) |
| [gender](gender.md) | +0.67 | 73,975 / 73,975 (100.0%) | 24,962 / 63,804 (39.1%) |
| [typems](typems.md) | +0.43 | 44,430 / 44,458 (99.9%) | 54,507 / 93,321 (58.4%) |
| [discontinuous](discontinuous.md) | -0.25 | 1,164 / 6,034 (19.3%) | 97,773 / 131,745 (74.2%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/number.md) Source: `docs/features/number.md`; configured at `configuration.docs.featureBase` |

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
| description | grammatical number |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:15Z |
