# normalized.tf

[← Corpus index](../index.md)

lemma normalized

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The normalized node feature carries a string value described in metadata as lemma normalized. It is populated on 137,779 word nodes, 46,077 phrase nodes, and 91,702 subphrase nodes; source counts record populated nodes only, not universal coverage. No value examples are attested. It belongs to the surface_text feature family alongside text, unicode, translit, and unaccent, but the inventory designates no primary surface-text convention.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 46,077 (66.8%) |
| [subphrase](../../structure.html#type-subphrase) | 91,702 (78.9%) |
| [word](../../structure.html#type-word) | 137,779 (100.0%) |

## Frequent values

18,480 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "καί" | 17,152 | 6.2% |
| "ὁ" | 5,538 | 2.0% |
| "δέ" | 5,528 | 2.0% |
| "ἐν" | 5,368 | 1.9% |
| "τοῦ" | 4,994 | 1.8% |
| "εἰς" | 3,510 | 1.3% |
| "τό" | 3,328 | 1.2% |
| "τόν" | 3,124 | 1.1% |
| "τήν" | 3,046 | 1.1% |
| "αὐτοῦ" | 2,822 | 1.0% |
| "τῆς" | 2,600 | 0.9% |
| "ὅτι" | 2,562 | 0.9% |

## Correlated features

- [after](after.md) phrase · φ +1.00

- [id](id.md) phrase · φ +1.00

- [lemma](lemma.md) phrase · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | normalized present when compared feature is present | normalized present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +1.00 | 46,077 / 46,077 (100.0%) | 0 / 22,930 (0.0%) |
| [domain](domain.md), [ln](ln.md) | +0.91 | 43,153 / 43,153 (100.0%) | 2,924 / 25,854 (11.3%) |
| [number](number.md) | +0.81 | 39,260 / 39,260 (100.0%) | 6,817 / 29,747 (22.9%) |
| [rule](rule.md) | -1.00 | 0 / 22,930 (0.0%) | 46,077 / 46,077 (100.0%) |
| [typ](typ.md) | -0.93 | 0 / 20,768 (0.0%) | 46,077 / 48,239 (95.5%) |

### subphrase nodes

| Compared feature(s) | φ | normalized present when compared feature is present | normalized present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +1.00 | 91,702 / 91,702 (100.0%) | 0 / 24,476 (0.0%) |
| [domain](domain.md), [ln](ln.md) | +0.83 | 83,726 / 83,726 (100.0%) | 7,976 / 32,452 (24.6%) |
| [number](number.md) | +0.53 | 59,677 / 59,677 (100.0%) | 32,025 / 56,501 (56.7%) |
| [rule](rule.md) | -1.00 | 0 / 24,475 (0.0%) | 91,702 / 91,703 (100.0%) |
| [typ](typ.md) | -0.93 | 0 / 21,853 (0.0%) | 91,702 / 94,325 (97.2%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/normalized.md) Source: `docs/features/normalized.md`; configured at `configuration.docs.featureBase` |

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
| description | lemma normalized |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:14Z |
