# ln.tf

[← Corpus index](../index.md)

ln

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The node feature ln records string annotations on phrase, subphrase, and word nodes in the Greek New Testament (Nestle 1904). Sources show 43,153 phrase, 83,726 subphrase, and 126,879 word nodes with values; other nodes of these types have no recorded value. Of 7,815 distinct values, frequent strings include “92.24” (39,476) and “92.11” (9,436). Metadata describes the feature only as “ln,” leaving its semantic interpretation undocumented.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 43,153 (62.5%) |
| [subphrase](../../structure.html#type-subphrase) | 83,726 (72.1%) |
| [word](../../structure.html#type-word) | 126,879 (92.1%) |

## Frequent values

7,815 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "92.24" | 39,476 | 15.6% |
| "92.11" | 9,436 | 3.7% |
| "89.92" | 5,806 | 2.3% |
| "89.87" | 5,512 | 2.2% |
| "33.69" | 4,672 | 1.8% |
| "69.3" | 3,472 | 1.4% |
| "92.1" | 3,464 | 1.4% |
| "92.7" | 2,988 | 1.2% |
| "12.1" | 2,494 | 1.0% |
| "92.29" | 2,180 | 0.9% |
| "59.23" | 2,178 | 0.9% |
| "92.27" | 2,034 | 0.8% |

## Correlated features

- [domain](domain.md) phrase · φ +1.00

- [after](after.md) phrase · φ +0.91

- [id](id.md) phrase · φ +0.91

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | ln present when compared feature is present | ln present when compared feature is absent |
| --- | --- | --- | --- |
| [domain](domain.md) | +1.00 | 43,153 / 43,153 (100.0%) | 0 / 25,854 (0.0%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +0.91 | 43,153 / 46,077 (93.7%) | 0 / 22,930 (0.0%) |
| [number](number.md) | +0.76 | 37,084 / 39,260 (94.5%) | 6,069 / 29,747 (20.4%) |
| [rule](rule.md) | -0.91 | 0 / 22,930 (0.0%) | 43,153 / 46,077 (93.7%) |
| [typ](typ.md) | -0.85 | 0 / 20,768 (0.0%) | 43,153 / 48,239 (89.5%) |

### subphrase nodes

| Compared feature(s) | φ | ln present when compared feature is present | ln present when compared feature is absent |
| --- | --- | --- | --- |
| [domain](domain.md) | +1.00 | 83,726 / 83,726 (100.0%) | 0 / 32,452 (0.0%) |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +0.83 | 83,726 / 91,702 (91.3%) | 0 / 24,476 (0.0%) |
| [number](number.md) | +0.58 | 57,997 / 59,677 (97.2%) | 25,729 / 56,501 (45.5%) |
| [rule](rule.md) | -0.83 | 0 / 24,475 (0.0%) | 83,726 / 91,703 (91.3%) |
| [typ](typ.md) | -0.77 | 0 / 21,853 (0.0%) | 83,726 / 94,325 (88.8%) |

### word nodes

| Compared feature(s) | φ | ln present when compared feature is present | ln present when compared feature is absent |
| --- | --- | --- | --- |
| [domain](domain.md) | +1.00 | 126,879 / 126,879 (100.0%) | 0 / 10,900 (0.0%) |
| [number](number.md) | +0.24 | 95,081 / 98,937 (96.1%) | 31,798 / 38,842 (81.9%) |
| [gender](gender.md) | +0.19 | 71,637 / 73,975 (96.8%) | 55,242 / 63,804 (86.6%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/ln.md) Source: `docs/features/ln.md`; configured at `configuration.docs.featureBase` |

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
| description | ln |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:13Z |
