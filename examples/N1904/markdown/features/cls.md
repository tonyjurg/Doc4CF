# cls.tf

[← Corpus index](../index.md)

this is XML attribute cls

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

cls is a node-level string feature capturing the XML attribute cls on clause (28,676), phrase (66,851), sentence (1,476), subphrase (113,564), wg (72,788), and word (137,779) nodes. Values include np (61,822), cl (60,304), noun (56,910), verb (56,714), det (39,572), conj (36,456), pron (32,354), pp (22,338), prep (21,828), adj (16,904), adv (12,308), ptcl (1,546). It feeds the clause label template {typ} {function} {rela} \\ {cls} {role} {junction}; scope overlaps sp, typ, typems without documented distinctions.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sentence](../../structure.html#type-sentence) | 1,476 (18.4%) |
| [clause](../../structure.html#type-clause) | 28,676 (67.5%) |
| [wg](../../structure.html#type-wg) | 72,788 (68.1%) |
| [phrase](../../structure.html#type-phrase) | 66,851 (96.9%) |
| [subphrase](../../structure.html#type-subphrase) | 113,564 (97.8%) |
| [word](../../structure.html#type-word) | 137,779 (100.0%) |

## Frequent values

18 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "np" | 61,822 | 14.7% |
| "cl" | 60,304 | 14.3% |
| "noun" | 56,910 | 13.5% |
| "verb" | 56,714 | 13.5% |
| "det" | 39,572 | 9.4% |
| "conj" | 36,456 | 8.7% |
| "pron" | 32,354 | 7.7% |
| "pp" | 22,338 | 5.3% |
| "prep" | 21,828 | 5.2% |
| "adj" | 16,904 | 4.0% |
| "adv" | 12,308 | 2.9% |
| "ptcl" | 1,546 | 0.4% |

## Correlated features

- [function](function.md) sentence · φ +0.69

- [crule](crule.md) sentence · φ +0.56

- [nodeid](nodeid.md) sentence · φ +0.56

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sentence nodes

| Compared feature(s) | φ | cls present when compared feature is present | cls present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.69 | 778 / 778 (100.0%) | 698 / 7,233 (9.7%) |
| [crule](crule.md), [nodeid](nodeid.md) | +0.56 | 691 / 838 (82.5%) | 785 / 7,173 (10.9%) |
| [cltype](cltype.md) | +0.26 | 124 / 125 (99.2%) | 1,352 / 7,886 (17.1%) |
| [typems](typems.md) | -0.81 | 0 / 5,946 (0.0%) | 1,476 / 2,065 (71.5%) |
| [rule](rule.md) | -0.56 | 785 / 7,173 (10.9%) | 691 / 838 (82.5%) |

### clause nodes

| Compared feature(s) | φ | cls present when compared feature is present | cls present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.69 | 21,403 / 21,568 (99.2%) | 7,273 / 20,938 (34.7%) |
| [junction](junction.md) | +0.35 | 15,406 / 17,741 (86.8%) | 13,270 / 24,765 (53.6%) |
| [crule](crule.md), [nodeid](nodeid.md) | +0.18 | 4,281 / 4,720 (90.7%) | 24,395 / 37,786 (64.6%) |
| [typems](typems.md) | -0.74 | 0 / 8,873 (0.0%) | 28,676 / 33,633 (85.3%) |
| [articular](articular.md) | -0.27 | 822 / 3,386 (24.3%) | 27,854 / 39,120 (71.2%) |

### wg nodes

| Compared feature(s) | φ | cls present when compared feature is present | cls present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.49 | 42,955 / 45,276 (94.9%) | 29,833 / 61,592 (48.4%) |
| [typ](typ.md) | +0.30 | 42,621 / 51,733 (82.4%) | 30,167 / 55,135 (54.7%) |
| [rule](rule.md) | +0.26 | 67,816 / 93,234 (72.7%) | 4,972 / 13,634 (36.5%) |
| [appositioncontainer](appositioncontainer.md) | -0.20 | 0 / 1,908 (0.0%) | 72,788 / 104,960 (69.3%) |
| [typems](typems.md) | -0.18 | 42,621 / 68,710 (62.0%) | 30,167 / 38,158 (79.1%) |

### phrase nodes

| Compared feature(s) | φ | cls present when compared feature is present | cls present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +0.25 | 46,077 / 46,077 (100.0%) | 20,774 / 22,930 (90.6%) |
| [domain](domain.md), [ln](ln.md) | +0.23 | 43,153 / 43,153 (100.0%) | 23,698 / 25,854 (91.7%) |
| [number](number.md) | +0.21 | 39,260 / 39,260 (100.0%) | 27,591 / 29,747 (92.8%) |
| [appositioncontainer](appositioncontainer.md) | -0.57 | 0 / 715 (0.0%) | 66,851 / 68,292 (97.9%) |
| [rule](rule.md) | -0.25 | 20,774 / 22,930 (90.6%) | 46,077 / 46,077 (100.0%) |

### subphrase nodes

| Compared feature(s) | φ | cls present when compared feature is present | cls present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md), [id](id.md), [lemma](lemma.md), [lemmatranslit](lemmatranslit.md), [morph](morph.md), [normalized](normalized.md), [ref](ref.md), [sp](sp.md), [strong](strong.md), [text](text.md), [trailer](trailer.md), [trans](trans.md), [translit](translit.md), [unaccent](unaccent.md), [unicode](unicode.md) | +0.29 | 91,702 / 91,702 (100.0%) | 21,862 / 24,476 (89.3%) |
| [domain](domain.md), [ln](ln.md) | +0.24 | 83,726 / 83,726 (100.0%) | 29,838 / 32,452 (91.9%) |
| [number](number.md) | +0.16 | 59,677 / 59,677 (100.0%) | 53,887 / 56,501 (95.4%) |
| [appositioncontainer](appositioncontainer.md) | -0.65 | 0 / 1,131 (0.0%) | 113,564 / 115,047 (98.7%) |
| [rule](rule.md) | -0.29 | 21,862 / 24,475 (89.3%) | 91,702 / 91,703 (100.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.clause.label` | {typ} {function} {rela} \\ {cls} {role} {junction} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/cls.md) Source: `docs/features/cls.md`; configured at `configuration.docs.featureBase` |

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
| description | this is XML attribute cls |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:11Z |
