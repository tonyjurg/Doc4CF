# rela.tf

[← Corpus index](../index.md)

this is XML attribute rela

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [wg](../../structure.html#type-wg) | 969 (0.9%) |
| [subphrase](../../structure.html#type-subphrase) | 979 (0.8%) |
| [word](../../structure.html#type-word) | 10 (0.0%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "Appo" | 1,958 | 100.0% |

## Correlated features

- [role](role.md) subphrase · φ +0.68

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### wg nodes

| Compared feature(s) | φ | rela present when compared feature is present | rela present when compared feature is absent |
| --- | --- | --- | --- |
| [role](role.md) | +0.13 | 969 / 37,426 (2.6%) | 0 / 69,442 (0.0%) |

### subphrase nodes

| Compared feature(s) | φ | rela present when compared feature is present | rela present when compared feature is absent |
| --- | --- | --- | --- |
| [role](role.md) | +0.68 | 979 / 2,081 (47.0%) | 0 / 114,097 (0.0%) |
| [rule](rule.md) | +0.18 | 969 / 24,475 (4.0%) | 10 / 91,703 (0.0%) |
| [typ](typ.md) | +0.14 | 785 / 21,853 (3.6%) | 194 / 94,325 (0.2%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -0.18 | 10 / 91,702 (0.0%) | 969 / 24,476 (4.0%) |
| [domain](domain.md), [ln](ln.md) | -0.15 | 10 / 83,726 (0.0%) | 969 / 32,452 (3.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.clause.label` | {typ} {function} {rela} \\ {cls} {role} {junction} |
| `configuration.typeDisplay.group.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.phrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.sentence.label` | {typ} {function} {rela} \\ {role} {rule} |
| `configuration.typeDisplay.subphrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/rela.md) Source: `docs/features/rela.md`; configured at `configuration.docs.featureBase` |

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
| description | this is XML attribute rela |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:16Z |
