# punctuation.tf

[← Corpus index](../index.md)

punctuation found after a word

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 8,412 (12.2%) |
| [subphrase](../../structure.html#type-subphrase) | 10,097 (8.7%) |
| [word](../../structure.html#type-word) | 18,509 (13.4%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "," | 18,924 | 51.1% |
| "." | 11,434 | 30.9% |
| "·" | 4,718 | 12.7% |
| ";" | 1,942 | 5.2% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | punctuation present when compared feature is present | punctuation present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +0.26 | 8,412 / 46,077 (18.3%) | 0 / 22,930 (0.0%) |
| [domain](domain.md), [ln](ln.md) | +0.25 | 8,036 / 43,153 (18.6%) | 376 / 25,854 (1.5%) |
| [number](number.md) | +0.24 | 7,494 / 39,260 (19.1%) | 918 / 29,747 (3.1%) |
| [rule](rule.md) | -0.26 | 0 / 22,930 (0.0%) | 8,412 / 46,077 (18.3%) |
| [typ](typ.md) | -0.24 | 0 / 20,768 (0.0%) | 8,412 / 48,239 (17.4%) |

### subphrase nodes

| Compared feature(s) | φ | punctuation present when compared feature is present | punctuation present when compared feature is absent |
| --- | --- | --- | --- |
| [number](number.md) | +0.28 | 9,776 / 59,677 (16.4%) | 321 / 56,501 (0.6%) |
| [case](case.md) | +0.28 | 9,707 / 59,065 (16.4%) | 390 / 57,113 (0.7%) |
| [gender](gender.md) | +0.24 | 8,785 / 56,317 (15.6%) | 1,312 / 59,861 (2.2%) |
| [rule](rule.md) | -0.16 | 0 / 24,475 (0.0%) | 10,097 / 91,703 (11.0%) |
| [typ](typ.md) | -0.15 | 0 / 21,853 (0.0%) | 10,097 / 94,325 (10.7%) |

### word nodes

| Compared feature(s) | φ | punctuation present when compared feature is present | punctuation present when compared feature is absent |
| --- | --- | --- | --- |
| [typems](typems.md) | +0.20 | 10,428 / 44,458 (23.5%) | 8,081 / 93,321 (8.7%) |
| [number](number.md) | +0.19 | 17,270 / 98,937 (17.5%) | 1,239 / 38,842 (3.2%) |
| [role](role.md) | +0.12 | 8,879 / 46,792 (19.0%) | 9,630 / 90,987 (10.6%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/punctuation.md) Source: `docs/features/punctuation.md`; configured at `configuration.docs.featureBase` |

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
| description | punctuation found after a word |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:15Z |
