# typ.tf

[← Corpus index](../index.md)

syntactical type (on sentence, group, clause or phrase)

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [group](../../structure.html#type-group) | 8,945 (100.0%) |
| [clause](../../structure.html#type-clause) | 167 (0.4%) |
| [wg](../../structure.html#type-wg) | 51,733 (48.4%) |
| [phrase](../../structure.html#type-phrase) | 20,768 (30.1%) |
| [subphrase](../../structure.html#type-subphrase) | 21,853 (18.8%) |

## Frequent values

8 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "NP" | 61,822 | 59.8% |
| "PP" | 22,338 | 21.6% |
| "conjuncted" | 16,150 | 15.6% |
| "apposition" | 1,740 | 1.7% |
| "VP" | 414 | 0.4% |
| "AdjP" | 336 | 0.3% |
| "Voct" | 334 | 0.3% |
| "AdvP" | 332 | 0.3% |

## Correlated features

- [rule](rule.md) subphrase · φ +0.93

- [typems](typems.md) wg · φ +0.72

- [articular](articular.md) phrase · φ +0.66

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### clause nodes

| Compared feature(s) | φ | typ present when compared feature is present | typ present when compared feature is absent |
| --- | --- | --- | --- |
| [appositioncontainer](appositioncontainer.md) | +0.61 | 62 / 62 (100.0%) | 105 / 42,444 (0.2%) |
| [typems](typems.md) | +0.10 | 147 / 8,873 (1.7%) | 20 / 33,633 (0.1%) |

### wg nodes

| Compared feature(s) | φ | typ present when compared feature is present | typ present when compared feature is absent |
| --- | --- | --- | --- |
| [typems](typems.md) | +0.72 | 51,698 / 68,710 (75.2%) | 35 / 38,158 (0.1%) |
| [articular](articular.md) | +0.41 | 23,708 / 28,772 (82.4%) | 28,025 / 78,096 (35.9%) |
| [cls](cls.md) | +0.30 | 42,621 / 72,788 (58.6%) | 9,112 / 34,080 (26.7%) |
| [junction](junction.md) | -0.43 | 0 / 17,921 (0.0%) | 51,733 / 88,947 (58.2%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.23 | 0 / 5,558 (0.0%) | 51,733 / 101,310 (51.1%) |

### phrase nodes

| Compared feature(s) | φ | typ present when compared feature is present | typ present when compared feature is absent |
| --- | --- | --- | --- |
| [rule](rule.md) | +0.93 | 20,768 / 22,930 (90.6%) | 0 / 46,077 (0.0%) |
| [typems](typems.md) | +0.68 | 20,768 / 33,293 (62.4%) | 0 / 35,714 (0.0%) |
| [articular](articular.md) | +0.66 | 12,163 / 13,079 (93.0%) | 8,605 / 55,928 (15.4%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -0.93 | 0 / 46,077 (0.0%) | 20,768 / 22,930 (90.6%) |
| [domain](domain.md), [ln](ln.md) | -0.85 | 0 / 43,153 (0.0%) | 20,768 / 25,854 (80.3%) |

### subphrase nodes

| Compared feature(s) | φ | typ present when compared feature is present | typ present when compared feature is absent |
| --- | --- | --- | --- |
| [rule](rule.md) | +0.93 | 21,853 / 24,475 (89.3%) | 0 / 91,703 (0.0%) |
| [articular](articular.md) | +0.66 | 11,280 / 11,897 (94.8%) | 10,573 / 104,281 (10.1%) |
| [typems](typems.md) | +0.50 | 21,838 / 56,111 (38.9%) | 15 / 60,067 (0.0%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -0.93 | 0 / 91,702 (0.0%) | 21,853 / 24,476 (89.3%) |
| [domain](domain.md), [ln](ln.md) | -0.77 | 0 / 83,726 (0.0%) | 21,853 / 32,452 (67.3%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.clause.label` | {typ} {function} {rela} \\ {cls} {role} {junction} |
| `configuration.typeDisplay.group.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.phrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.sentence.label` | {typ} {function} {rela} \\ {role} {rule} |
| `configuration.typeDisplay.subphrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/typ.md) Source: `docs/features/typ.md`; configured at `configuration.docs.featureBase` |

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
| description | syntactical type (on sentence, group, clause or phrase) |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:18Z |
