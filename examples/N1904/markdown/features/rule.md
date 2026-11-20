# rule.tf

[← Corpus index](../index.md)

syntactical rule

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sentence](../../structure.html#type-sentence) | 7,173 (89.5%) |
| [group](../../structure.html#type-group) | 870 (9.7%) |
| [clause](../../structure.html#type-clause) | 37,786 (88.9%) |
| [wg](../../structure.html#type-wg) | 93,234 (87.2%) |
| [phrase](../../structure.html#type-phrase) | 22,930 (33.2%) |
| [subphrase](../../structure.html#type-subphrase) | 24,475 (21.1%) |

## Frequent values

817 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "DetNP" | 31,392 | 16.8% |
| "PrepNp" | 22,088 | 11.8% |
| "NPofNP" | 13,638 | 7.3% |
| "Conj-CL" | 11,152 | 6.0% |
| "CLaCL" | 7,658 | 4.1% |
| "sub-CL" | 6,058 | 3.2% |
| "V2CL" | 5,686 | 3.0% |
| "V-O" | 5,450 | 2.9% |
| "DetCL" | 4,022 | 2.2% |
| "Np-Appos" | 3,816 | 2.0% |
| "V-ADV" | 3,374 | 1.8% |
| "ClCl" | 3,158 | 1.7% |

## Correlated features

- [typ](typ.md) subphrase · φ +0.93

- [articular](articular.md) phrase · φ +0.69

- [typems](typems.md) phrase · φ +0.66

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sentence nodes

| Compared feature(s) | φ | rule present when compared feature is present | rule present when compared feature is absent |
| --- | --- | --- | --- |
| [typems](typems.md) | +0.58 | 5,946 / 5,946 (100.0%) | 1,227 / 2,065 (59.4%) |
| [function](function.md) | +0.11 | 778 / 778 (100.0%) | 6,395 / 7,233 (88.4%) |
| [crule](crule.md), [nodeid](nodeid.md) | -1.00 | 0 / 838 (0.0%) | 7,173 / 7,173 (100.0%) |
| [cls](cls.md) | -0.56 | 785 / 1,476 (53.2%) | 6,388 / 6,535 (97.8%) |

### group nodes

| Compared feature(s) | φ | rule present when compared feature is present | rule present when compared feature is absent |
| --- | --- | --- | --- |
| [role](role.md) | +0.60 | 335 / 335 (100.0%) | 535 / 8,610 (6.2%) |
| [articular](articular.md) | +0.44 | 181 / 181 (100.0%) | 689 / 8,764 (7.9%) |

### clause nodes

| Compared feature(s) | φ | rule present when compared feature is present | rule present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.36 | 21,568 / 21,568 (100.0%) | 16,218 / 20,938 (77.5%) |
| [junction](junction.md) | +0.30 | 17,741 / 17,741 (100.0%) | 20,045 / 24,765 (80.9%) |
| [typems](typems.md) | +0.18 | 8,872 / 8,873 (100.0%) | 28,914 / 33,633 (86.0%) |
| [crule](crule.md), [nodeid](nodeid.md) | -1.00 | 0 / 4,720 (0.0%) | 37,786 / 37,786 (100.0%) |
| [cls](cls.md) | -0.18 | 24,395 / 28,676 (85.1%) | 13,391 / 13,830 (96.8%) |

### wg nodes

| Compared feature(s) | φ | rule present when compared feature is present | rule present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.33 | 45,276 / 45,276 (100.0%) | 47,958 / 61,592 (77.9%) |
| [cls](cls.md) | +0.26 | 67,816 / 72,788 (93.2%) | 25,418 / 34,080 (74.6%) |
| [articular](articular.md) | +0.23 | 28,772 / 28,772 (100.0%) | 64,462 / 78,096 (82.5%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.61 | 0 / 5,558 (0.0%) | 93,234 / 101,310 (92.0%) |

### phrase nodes

| Compared feature(s) | φ | rule present when compared feature is present | rule present when compared feature is absent |
| --- | --- | --- | --- |
| [typ](typ.md) | +0.93 | 20,768 / 20,768 (100.0%) | 2,162 / 48,239 (4.5%) |
| [articular](articular.md) | +0.69 | 13,079 / 13,079 (100.0%) | 9,851 / 55,928 (17.6%) |
| [typems](typems.md) | +0.66 | 21,726 / 33,293 (65.3%) | 1,204 / 35,714 (3.4%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -1.00 | 0 / 46,077 (0.0%) | 22,930 / 22,930 (100.0%) |
| [domain](domain.md), [ln](ln.md) | -0.91 | 0 / 43,153 (0.0%) | 22,930 / 25,854 (88.7%) |

### subphrase nodes

| Compared feature(s) | φ | rule present when compared feature is present | rule present when compared feature is absent |
| --- | --- | --- | --- |
| [typ](typ.md) | +0.93 | 21,853 / 21,853 (100.0%) | 2,622 / 94,325 (2.8%) |
| [articular](articular.md) | +0.65 | 11,897 / 11,897 (100.0%) | 12,578 / 104,281 (12.1%) |
| [typems](typems.md) | +0.48 | 23,220 / 56,111 (41.4%) | 1,255 / 60,067 (2.1%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -1.00 | 0 / 91,702 (0.0%) | 24,475 / 24,476 (100.0%) |
| [domain](domain.md), [ln](ln.md) | -0.83 | 0 / 83,726 (0.0%) | 24,475 / 32,452 (75.4%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.group.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.phrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.sentence.label` | {typ} {function} {rela} \\ {role} {rule} |
| `configuration.typeDisplay.subphrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.wg.label` | {typems} {role} {rule} {junction} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/rule.md) Source: `docs/features/rule.md`; configured at `configuration.docs.featureBase` |

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
| description | syntactical rule |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:16Z |
