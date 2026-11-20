# typems.tf

[← Corpus index](../index.md)

morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg)

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sentence](../../structure.html#type-sentence) | 5,946 (74.2%) |
| [group](../../structure.html#type-group) | 8,945 (100.0%) |
| [clause](../../structure.html#type-clause) | 8,873 (20.9%) |
| [wg](../../structure.html#type-wg) | 68,710 (64.3%) |
| [phrase](../../structure.html#type-phrase) | 33,293 (48.2%) |
| [subphrase](../../structure.html#type-subphrase) | 56,111 (48.3%) |
| [word](../../structure.html#type-word) | 44,458 (32.3%) |

## Frequent values

16 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "modifier-scope" | 59,290 | 26.2% |
| "common" | 47,288 | 20.9% |
| "wrapper-clause-scope" | 24,332 | 10.8% |
| "personal" | 23,042 | 10.2% |
| "wrapper-scope" | 22,528 | 10.0% |
| "conjuncted-wg" | 16,150 | 7.1% |
| "group" | 9,914 | 4.4% |
| "proper" | 9,278 | 4.1% |
| "demonstrative" | 3,444 | 1.5% |
| "modifier-clause-scope" | 3,424 | 1.5% |
| "relative" | 3,348 | 1.5% |
| "apposition-group" | 1,782 | 0.8% |

## Correlated features

- [typ](typ.md) wg · φ +0.72

- [rule](rule.md) phrase · φ +0.66

- [case](case.md) word · φ +0.59

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sentence nodes

| Compared feature(s) | φ | typems present when compared feature is present | typems present when compared feature is absent |
| --- | --- | --- | --- |
| [rule](rule.md) | +0.58 | 5,946 / 7,173 (82.9%) | 0 / 838 (0.0%) |
| [cls](cls.md) | -0.81 | 0 / 1,476 (0.0%) | 5,946 / 6,535 (91.0%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.58 | 0 / 838 (0.0%) | 5,946 / 7,173 (82.9%) |

### clause nodes

| Compared feature(s) | φ | typems present when compared feature is present | typems present when compared feature is absent |
| --- | --- | --- | --- |
| [articular](articular.md) | +0.35 | 2,336 / 3,386 (69.0%) | 6,537 / 39,120 (16.7%) |
| [role](role.md) | +0.25 | 4,623 / 12,795 (36.1%) | 4,250 / 29,711 (14.3%) |
| [rule](rule.md) | +0.18 | 8,872 / 37,786 (23.5%) | 1 / 4,720 (0.0%) |
| [cls](cls.md) | -0.74 | 0 / 28,676 (0.0%) | 8,873 / 13,830 (64.2%) |
| [function](function.md) | -0.52 | 0 / 21,568 (0.0%) | 8,873 / 20,938 (42.4%) |

### wg nodes

| Compared feature(s) | φ | typems present when compared feature is present | typems present when compared feature is absent |
| --- | --- | --- | --- |
| [typ](typ.md) | +0.72 | 51,698 / 51,733 (99.9%) | 17,012 / 55,135 (30.9%) |
| [articular](articular.md) | +0.37 | 26,940 / 28,772 (93.6%) | 41,770 / 78,096 (53.5%) |
| [role](role.md) | +0.16 | 27,953 / 37,426 (74.7%) | 40,757 / 69,442 (58.7%) |
| [junction](junction.md) | -0.55 | 1,076 / 17,921 (6.0%) | 67,634 / 88,947 (76.0%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.31 | 1 / 5,558 (0.0%) | 68,709 / 101,310 (67.8%) |

### phrase nodes

| Compared feature(s) | φ | typems present when compared feature is present | typems present when compared feature is absent |
| --- | --- | --- | --- |
| [typ](typ.md) | +0.68 | 20,768 / 20,768 (100.0%) | 12,525 / 48,239 (26.0%) |
| [rule](rule.md) | +0.66 | 21,726 / 22,930 (94.7%) | 11,567 / 46,077 (25.1%) |
| [articular](articular.md) | +0.46 | 12,582 / 13,079 (96.2%) | 20,711 / 55,928 (37.0%) |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | -0.78 | 0 / 27,355 (0.0%) | 33,293 / 41,652 (79.9%) |
| [framespec](framespec.md) | -0.72 | 0 / 24,783 (0.0%) | 33,293 / 44,224 (75.3%) |

### subphrase nodes

| Compared feature(s) | φ | typems present when compared feature is present | typems present when compared feature is absent |
| --- | --- | --- | --- |
| [typ](typ.md) | +0.50 | 21,838 / 21,853 (99.9%) | 34,273 / 94,325 (36.3%) |
| [rule](rule.md) | +0.48 | 23,220 / 24,475 (94.9%) | 32,891 / 91,703 (35.9%) |
| [articular](articular.md) | +0.34 | 11,688 / 11,897 (98.2%) | 44,423 / 104,281 (42.6%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -0.48 | 32,891 / 91,702 (35.9%) | 23,220 / 24,476 (94.9%) |
| [domain](domain.md), [ln](ln.md) | -0.34 | 31,649 / 83,726 (37.8%) | 24,462 / 32,452 (75.4%) |

### word nodes

| Compared feature(s) | φ | typems present when compared feature is present | typems present when compared feature is absent |
| --- | --- | --- | --- |
| [case](case.md) | +0.59 | 44,430 / 79,518 (55.9%) | 28 / 58,261 (0.0%) |
| [gender](gender.md) | +0.47 | 38,887 / 73,975 (52.6%) | 5,571 / 63,804 (8.7%) |
| [referent](referent.md) | +0.45 | 13,593 / 14,471 (93.9%) | 30,865 / 123,308 (25.0%) |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | -0.35 | 0 / 28,357 (0.0%) | 44,458 / 109,422 (40.6%) |
| [framespec](framespec.md) | -0.33 | 0 / 25,493 (0.0%) | 44,458 / 112,286 (39.6%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.group.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.phrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.subphrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.wg.label` | {typems} {role} {rule} {junction} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/typems.md) Source: `docs/features/typems.md`; configured at `configuration.docs.featureBase` |

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
| description | morphological type (on word), syntactical type (on sentence, group, clause, phrase or wg) |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:18Z |
