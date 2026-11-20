# articular.tf

[← Corpus index](../index.md)

1 if the sentence, group, clause, phrase or wg has an article

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The node feature articular marks clause, group, phrase, sentence, subphrase, and wg nodes with value 1 when the unit contains a Greek article. It is populated on 57,544 nodes: clause 3,386; group 181; phrase 13,079; sentence 229; subphrase 11,897; wg 28,772. Missing assignments indicate no recorded value, not a negative article-absent class.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sentence](../../structure.html#type-sentence) | 229 (2.9%) |
| [group](../../structure.html#type-group) | 181 (2.0%) |
| [clause](../../structure.html#type-clause) | 3,386 (8.0%) |
| [wg](../../structure.html#type-wg) | 28,772 (26.9%) |
| [phrase](../../structure.html#type-phrase) | 13,079 (19.0%) |
| [subphrase](../../structure.html#type-subphrase) | 11,897 (10.2%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 57,544 | 100.0% |

## Correlated features

- [rule](rule.md) phrase · φ +0.69

- [typ](typ.md) phrase · φ +0.66

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### group nodes

| Compared feature(s) | φ | articular present when compared feature is present | articular present when compared feature is absent |
| --- | --- | --- | --- |
| [rule](rule.md) | +0.44 | 181 / 870 (20.8%) | 0 / 8,075 (0.0%) |
| [role](role.md) | +0.42 | 108 / 335 (32.2%) | 73 / 8,610 (0.8%) |

### clause nodes

| Compared feature(s) | φ | articular present when compared feature is present | articular present when compared feature is absent |
| --- | --- | --- | --- |
| [typems](typems.md) | +0.35 | 2,336 / 8,873 (26.3%) | 1,050 / 33,633 (3.1%) |
| [cltype](cltype.md) | +0.14 | 614 / 2,718 (22.6%) | 2,772 / 39,788 (7.0%) |
| [role](role.md) | +0.12 | 1,656 / 12,795 (12.9%) | 1,730 / 29,711 (5.8%) |
| [cls](cls.md) | -0.27 | 822 / 28,676 (2.9%) | 2,564 / 13,830 (18.5%) |
| [function](function.md) | -0.16 | 785 / 21,568 (3.6%) | 2,601 / 20,938 (12.4%) |

### wg nodes

| Compared feature(s) | φ | articular present when compared feature is present | articular present when compared feature is absent |
| --- | --- | --- | --- |
| [typ](typ.md) | +0.41 | 23,708 / 51,733 (45.8%) | 5,064 / 55,135 (9.2%) |
| [typems](typems.md) | +0.37 | 26,940 / 68,710 (39.2%) | 1,832 / 38,158 (4.8%) |
| [role](role.md) | +0.23 | 15,329 / 37,426 (41.0%) | 13,443 / 69,442 (19.4%) |
| [junction](junction.md) | -0.24 | 559 / 17,921 (3.1%) | 28,213 / 88,947 (31.7%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.14 | 0 / 5,558 (0.0%) | 28,772 / 101,310 (28.4%) |

### phrase nodes

| Compared feature(s) | φ | articular present when compared feature is present | articular present when compared feature is absent |
| --- | --- | --- | --- |
| [rule](rule.md) | +0.69 | 13,079 / 22,930 (57.0%) | 0 / 46,077 (0.0%) |
| [typ](typ.md) | +0.66 | 12,163 / 20,768 (58.6%) | 916 / 48,239 (1.9%) |
| [typems](typems.md) | +0.46 | 12,582 / 33,293 (37.8%) | 497 / 35,714 (1.4%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -0.69 | 0 / 46,077 (0.0%) | 13,079 / 22,930 (57.0%) |
| [domain](domain.md), [ln](ln.md) | -0.62 | 0 / 43,153 (0.0%) | 13,079 / 25,854 (50.6%) |

### subphrase nodes

| Compared feature(s) | φ | articular present when compared feature is present | articular present when compared feature is absent |
| --- | --- | --- | --- |
| [typ](typ.md) | +0.66 | 11,280 / 21,853 (51.6%) | 617 / 94,325 (0.7%) |
| [rule](rule.md) | +0.65 | 11,897 / 24,475 (48.6%) | 0 / 91,703 (0.0%) |
| [typems](typems.md) | +0.34 | 11,688 / 56,111 (20.8%) | 209 / 60,067 (0.3%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -0.65 | 0 / 91,702 (0.0%) | 11,897 / 24,476 (48.6%) |
| [domain](domain.md), [ln](ln.md) | -0.54 | 0 / 83,726 (0.0%) | 11,897 / 32,452 (36.7%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/articular.md) Source: `docs/features/articular.md`; configured at `configuration.docs.featureBase` |

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
| description | 1 if the sentence, group, clause, phrase or wg has an article |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | int |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:09Z |
