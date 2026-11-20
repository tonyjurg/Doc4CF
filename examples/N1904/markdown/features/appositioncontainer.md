# appositioncontainer.tf

[← Corpus index](../index.md)

1 if it is an apposition container

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The appositioncontainer node feature flags syntactic units that serve as apposition containers in the Greek New Testament (Nestle 1904). It carries the single observed integer value 1 on 3,816 populated nodes: 62 clauses, 715 phrases, 1,131 subphrases, and 1,908 word groups. Missing values indicate no recorded annotation, not a negative class.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [clause](../../structure.html#type-clause) | 62 (0.1%) |
| [wg](../../structure.html#type-wg) | 1,908 (1.8%) |
| [phrase](../../structure.html#type-phrase) | 715 (1.0%) |
| [subphrase](../../structure.html#type-subphrase) | 1,131 (1.0%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 3,816 | 100.0% |

## Correlated features

- [typ](typ.md) clause · φ +0.61

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### clause nodes

| Compared feature(s) | φ | appositioncontainer present when compared feature is present | appositioncontainer present when compared feature is absent |
| --- | --- | --- | --- |
| [typ](typ.md) | +0.61 | 62 / 167 (37.1%) | 0 / 42,339 (0.0%) |

### wg nodes

| Compared feature(s) | φ | appositioncontainer present when compared feature is present | appositioncontainer present when compared feature is absent |
| --- | --- | --- | --- |
| [typems](typems.md) | +0.10 | 1,908 / 68,710 (2.8%) | 0 / 38,158 (0.0%) |
| [cls](cls.md) | -0.20 | 0 / 72,788 (0.0%) | 1,908 / 34,080 (5.6%) |
| [typ](typ.md) | -0.12 | 62 / 51,733 (0.1%) | 1,846 / 55,135 (3.3%) |

### phrase nodes

| Compared feature(s) | φ | appositioncontainer present when compared feature is present | appositioncontainer present when compared feature is absent |
| --- | --- | --- | --- |
| [rule](rule.md) | +0.15 | 715 / 22,930 (3.1%) | 0 / 46,077 (0.0%) |
| [typems](typems.md) | +0.11 | 715 / 33,293 (2.1%) | 0 / 35,714 (0.0%) |
| [cls](cls.md) | -0.57 | 0 / 66,851 (0.0%) | 715 / 2,156 (33.2%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -0.15 | 0 / 46,077 (0.0%) | 715 / 22,930 (3.1%) |

### subphrase nodes

| Compared feature(s) | φ | appositioncontainer present when compared feature is present | appositioncontainer present when compared feature is absent |
| --- | --- | --- | --- |
| [rule](rule.md) | +0.19 | 1,131 / 24,475 (4.6%) | 0 / 91,703 (0.0%) |
| [typems](typems.md) | +0.10 | 1,131 / 56,111 (2.0%) | 0 / 60,067 (0.0%) |
| [cls](cls.md) | -0.65 | 0 / 113,564 (0.0%) | 1,131 / 2,614 (43.3%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | -0.19 | 0 / 91,702 (0.0%) | 1,131 / 24,476 (4.6%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/appositioncontainer.md) Source: `docs/features/appositioncontainer.md`; configured at `configuration.docs.featureBase` |

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
| description | 1 if it is an apposition container |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | int |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:09Z |
