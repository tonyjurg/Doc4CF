# discontinuous.tf

[← Corpus index](../index.md)

1 if the word is out of sequence in the xml

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

discontinuous is a node-level integer flag indicating that a node is out of sequence in the source XML. It is populated on 645 phrase, 5,389 subphrase, and 6,034 word nodes (12,068 total), all with value 1. Unpopulated nodes have no recorded value, not a negative class. The description says “word,” yet phrase and subphrase nodes are also annotated.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 645 (0.9%) |
| [subphrase](../../structure.html#type-subphrase) | 5,389 (4.6%) |
| [word](../../structure.html#type-word) | 6,034 (4.4%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 12,068 | 100.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### subphrase nodes

| Compared feature(s) | φ | discontinuous present when compared feature is present | discontinuous present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +0.11 | 5,389 / 91,702 (5.9%) | 0 / 24,476 (0.0%) |
| [number](number.md) | -0.17 | 661 / 59,677 (1.1%) | 4,728 / 56,501 (8.4%) |
| [typems](typems.md) | -0.17 | 516 / 56,111 (0.9%) | 4,873 / 60,067 (8.1%) |

### word nodes

| Compared feature(s) | φ | discontinuous present when compared feature is present | discontinuous present when compared feature is absent |
| --- | --- | --- | --- |
| [number](number.md) | -0.25 | 1,164 / 98,937 (1.2%) | 4,870 / 38,842 (12.5%) |
| [case](case.md) | -0.19 | 865 / 79,518 (1.1%) | 5,169 / 58,261 (8.9%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/discontinuous.md) Source: `docs/features/discontinuous.md`; configured at `configuration.docs.featureBase` |

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
| description | 1 if the word is out of sequence in the xml |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | int |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:11Z |
