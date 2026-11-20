# lemma.tf

[← Corpus index](../index.md)

lexical lemma

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

lemma records lexical lemmas as strings for annotated nodes in the Greek New Testament (Nestle 1904). Populated counts are 137,779 word nodes, 91,702 subphrase nodes, and 46,077 phrase nodes; missing assignments are unrecorded, not negative. Among 5,396 distinct strings, frequent values include ὁ (39,566). The source description is minimal ("lexical lemma"), so finer semantic nuance is not attested.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 46,077 (66.8%) |
| [subphrase](../../structure.html#type-subphrase) | 91,702 (78.9%) |
| [word](../../structure.html#type-word) | 137,779 (100.0%) |

## Frequent values

5,396 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "ὁ" | 39,566 | 14.4% |
| "καί" | 17,956 | 6.5% |
| "αὐτός" | 11,122 | 4.0% |
| "σύ" | 5,784 | 2.1% |
| "δέ" | 5,574 | 2.0% |
| "ἐν" | 5,486 | 2.0% |
| "ἐγώ" | 5,134 | 1.9% |
| "εἰμί" | 4,914 | 1.8% |
| "λέγω" | 4,510 | 1.6% |
| "εἰς" | 3,532 | 1.3% |
| "οὐ" | 3,244 | 1.2% |
| "ὅς" | 2,814 | 1.0% |

## Correlated features

- [after](after.md) phrase · φ +1.00

- [id](id.md) phrase · φ +1.00

- [lemmatranslit](lemmatranslit.md) phrase · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | lemma present when compared feature is present | lemma present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md), [id](id.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +1.00 | 46,077 / 46,077 (100.0%) | 0 / 22,930 (0.0%) |
| [domain](domain.md), [ln](ln.md) | +0.91 | 43,153 / 43,153 (100.0%) | 2,924 / 25,854 (11.3%) |
| [number](number.md) | +0.81 | 39,260 / 39,260 (100.0%) | 6,817 / 29,747 (22.9%) |
| [rule](rule.md) | -1.00 | 0 / 22,930 (0.0%) | 46,077 / 46,077 (100.0%) |
| [typ](typ.md) | -0.93 | 0 / 20,768 (0.0%) | 46,077 / 48,239 (95.5%) |

### subphrase nodes

| Compared feature(s) | φ | lemma present when compared feature is present | lemma present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md), [id](id.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +1.00 | 91,702 / 91,702 (100.0%) | 0 / 24,476 (0.0%) |
| [domain](domain.md), [ln](ln.md) | +0.83 | 83,726 / 83,726 (100.0%) | 7,976 / 32,452 (24.6%) |
| [number](number.md) | +0.53 | 59,677 / 59,677 (100.0%) | 32,025 / 56,501 (56.7%) |
| [rule](rule.md) | -1.00 | 0 / 24,475 (0.0%) | 91,702 / 91,703 (100.0%) |
| [typ](typ.md) | -0.93 | 0 / 21,853 (0.0%) | 91,702 / 94,325 (97.2%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.word.features[0]` | lemma |
| [lex-orig-plain rendering format](../../text.html#format-89b995281e9d) | `{lemma}{trailer}` Uses: [lemma](lemma.md), [trailer](trailer.md) |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/lemma.md) Source: `docs/features/lemma.md`; configured at `configuration.docs.featureBase` |

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
| description | lexical lemma |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:13Z |
