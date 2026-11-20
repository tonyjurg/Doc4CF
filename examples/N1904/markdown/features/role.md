# role.tf

[← Corpus index](../index.md)

role

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [group](../../structure.html#type-group) | 335 (3.7%) |
| [clause](../../structure.html#type-clause) | 12,795 (30.1%) |
| [wg](../../structure.html#type-wg) | 37,426 (35.0%) |
| [phrase](../../structure.html#type-phrase) | 69,007 (100.0%) |
| [subphrase](../../structure.html#type-subphrase) | 2,081 (1.8%) |
| [word](../../structure.html#type-word) | 46,792 (34.0%) |

## Frequent values

14 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "v" | 50,344 | 29.9% |
| "adv" | 43,154 | 25.6% |
| "o" | 26,988 | 16.0% |
| "s" | 22,336 | 13.3% |
| "p" | 7,348 | 4.4% |
| "io" | 5,316 | 3.2% |
| "vc" | 5,186 | 3.1% |
| "apposition" | 4,878 | 2.9% |
| "aux" | 2,112 | 1.3% |
| "o2" | 718 | 0.4% |
| "topic" | 46 | 0.0% |
| "ellipsis" | 4 | 0.0% |

## Correlated features

- [function](function.md) word · φ +0.99

- [rela](rela.md) subphrase · φ +0.68

- [mood](mood.md) word · φ +0.68

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### group nodes

| Compared feature(s) | φ | role present when compared feature is present | role present when compared feature is absent |
| --- | --- | --- | --- |
| [rule](rule.md) | +0.60 | 335 / 870 (38.5%) | 0 / 8,075 (0.0%) |
| [articular](articular.md) | +0.42 | 108 / 181 (59.7%) | 227 / 8,764 (2.6%) |

### clause nodes

| Compared feature(s) | φ | role present when compared feature is present | role present when compared feature is absent |
| --- | --- | --- | --- |
| [typems](typems.md) | +0.25 | 4,623 / 8,873 (52.1%) | 8,172 / 33,633 (24.3%) |
| [articular](articular.md) | +0.12 | 1,656 / 3,386 (48.9%) | 11,139 / 39,120 (28.5%) |
| [cls](cls.md) | -0.17 | 7,038 / 28,676 (24.5%) | 5,757 / 13,830 (41.6%) |
| [cltype](cltype.md) | -0.14 | 155 / 2,718 (5.7%) | 12,640 / 39,788 (31.8%) |

### wg nodes

| Compared feature(s) | φ | role present when compared feature is present | role present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.49 | 28,083 / 45,276 (62.0%) | 9,343 / 61,592 (15.2%) |
| [articular](articular.md) | +0.23 | 15,329 / 28,772 (53.3%) | 22,097 / 78,096 (28.3%) |
| [rule](rule.md) | +0.21 | 36,280 / 93,234 (38.9%) | 1,146 / 13,634 (8.4%) |
| [cltype](cltype.md) | -0.10 | 155 / 2,843 (5.5%) | 37,271 / 104,025 (35.8%) |

### subphrase nodes

| Compared feature(s) | φ | role present when compared feature is present | role present when compared feature is absent |
| --- | --- | --- | --- |
| [rela](rela.md) | +0.68 | 979 / 979 (100.0%) | 1,102 / 115,199 (1.0%) |
| [person](person.md) | +0.16 | 191 / 612 (31.2%) | 1,890 / 115,566 (1.6%) |
| [rule](rule.md) | +0.15 | 1,365 / 24,475 (5.6%) | 716 / 91,703 (0.8%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -0.15 | 715 / 91,702 (0.8%) | 1,366 / 24,476 (5.6%) |
| [domain](domain.md), [ln](ln.md) | -0.11 | 708 / 83,726 (0.8%) | 1,373 / 32,452 (4.2%) |

### word nodes

| Compared feature(s) | φ | role present when compared feature is present | role present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.99 | 46,077 / 46,077 (100.0%) | 715 / 91,702 (0.8%) |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.68 | 27,546 / 28,357 (97.1%) | 19,246 / 109,422 (17.6%) |
| [framespec](framespec.md) | +0.64 | 24,899 / 25,493 (97.7%) | 21,893 / 112,286 (19.5%) |
| [gender](gender.md) | -0.22 | 18,114 / 73,975 (24.5%) | 28,678 / 63,804 (44.9%) |
| [case](case.md) | -0.19 | 20,912 / 79,518 (26.3%) | 25,880 / 58,261 (44.4%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.clause.label` | {typ} {function} {rela} \\ {cls} {role} {junction} |
| `configuration.typeDisplay.group.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.phrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.sentence.label` | {typ} {function} {rela} \\ {role} {rule} |
| `configuration.typeDisplay.subphrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.wg.label` | {typems} {role} {rule} {junction} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/role.md) Source: `docs/features/role.md`; configured at `configuration.docs.featureBase` |

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
| description | role |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:16Z |
