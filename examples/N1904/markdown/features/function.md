# function.tf

[← Corpus index](../index.md)

this is XML attribute function

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The node feature function records an XML attribute value on clause, phrase, sentence, wg, and word nodes (21,568; 69,007; 778; 45,276; and 46,077 populated nodes respectively). Frequent values include Pred (49,714), Cmpl (26,024), Subj (20,396), and Objc (18,674), which may encode syntactic functions such as predicate, complement, subject, and object. Exact value semantics are not fully documented; unpopulated nodes have no recorded value, not a negative class.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sentence](../../structure.html#type-sentence) | 778 (9.7%) |
| [clause](../../structure.html#type-clause) | 21,568 (50.7%) |
| [wg](../../structure.html#type-wg) | 45,276 (42.4%) |
| [phrase](../../structure.html#type-phrase) | 69,007 (100.0%) |
| [word](../../structure.html#type-word) | 46,077 (33.4%) |

## Frequent values

429 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "Pred" | 49,714 | 27.2% |
| "Cmpl" | 26,024 | 14.2% |
| "Subj" | 20,396 | 11.2% |
| "Objc" | 18,674 | 10.2% |
| "PreC" | 12,344 | 6.8% |
| "Adv" | 11,192 | 6.1% |
| "Pred-Obj" | 5,452 | 3.0% |
| "Pred-Cmpl" | 3,818 | 2.1% |
| "Cmpl-Pred" | 2,370 | 1.3% |
| "Obj-Pred" | 2,154 | 1.2% |
| "Cmpl-Pred-Obj" | 1,368 | 0.7% |
| "Subj-Pred" | 1,278 | 0.7% |

## Correlated features

- [role](role.md) word · φ +0.99

- [cls](cls.md) sentence · φ +0.69

- [mood](mood.md) word · φ +0.68

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sentence nodes

| Compared feature(s) | φ | function present when compared feature is present | function present when compared feature is absent |
| --- | --- | --- | --- |
| [cls](cls.md) | +0.69 | 778 / 1,476 (52.7%) | 0 / 6,535 (0.0%) |
| [cltype](cltype.md) | +0.36 | 118 / 125 (94.4%) | 660 / 7,886 (8.4%) |
| [clausetype](clausetype.md) | +0.12 | 31 / 59 (52.5%) | 747 / 7,952 (9.4%) |
| [typems](typems.md) | -0.56 | 0 / 5,946 (0.0%) | 778 / 2,065 (37.7%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.11 | 0 / 838 (0.0%) | 778 / 7,173 (10.8%) |

### clause nodes

| Compared feature(s) | φ | function present when compared feature is present | function present when compared feature is absent |
| --- | --- | --- | --- |
| [cls](cls.md) | +0.69 | 21,403 / 28,676 (74.6%) | 165 / 13,830 (1.2%) |
| [junction](junction.md) | +0.41 | 13,343 / 17,741 (75.2%) | 8,225 / 24,765 (33.2%) |
| [rule](rule.md) | +0.36 | 21,568 / 37,786 (57.1%) | 0 / 4,720 (0.0%) |
| [typems](typems.md) | -0.52 | 0 / 8,873 (0.0%) | 21,568 / 33,633 (64.1%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.36 | 0 / 4,720 (0.0%) | 21,568 / 37,786 (57.1%) |

### wg nodes

| Compared feature(s) | φ | function present when compared feature is present | function present when compared feature is absent |
| --- | --- | --- | --- |
| [cls](cls.md) | +0.49 | 42,955 / 72,788 (59.0%) | 2,321 / 34,080 (6.8%) |
| [role](role.md) | +0.49 | 28,083 / 37,426 (75.0%) | 17,193 / 69,442 (24.8%) |
| [rule](rule.md) | +0.33 | 45,276 / 93,234 (48.6%) | 0 / 13,634 (0.0%) |
| [typems](typems.md) | -0.29 | 21,726 / 68,710 (31.6%) | 23,550 / 38,158 (61.7%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.20 | 0 / 5,558 (0.0%) | 45,276 / 101,310 (44.7%) |

### word nodes

| Compared feature(s) | φ | function present when compared feature is present | function present when compared feature is absent |
| --- | --- | --- | --- |
| [role](role.md) | +0.99 | 46,077 / 46,792 (98.5%) | 0 / 90,987 (0.0%) |
| [mood](mood.md), [tense](tense.md), [voice](voice.md) | +0.68 | 27,355 / 28,357 (96.5%) | 18,722 / 109,422 (17.1%) |
| [framespec](framespec.md) | +0.64 | 24,783 / 25,493 (97.2%) | 21,294 / 112,286 (19.0%) |
| [gender](gender.md) | -0.22 | 17,658 / 73,975 (23.9%) | 28,419 / 63,804 (44.5%) |
| [case](case.md) | -0.19 | 20,453 / 79,518 (25.7%) | 25,624 / 58,261 (44.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.clause.label` | {typ} {function} {rela} \\ {cls} {role} {junction} |
| `configuration.typeDisplay.group.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.phrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| `configuration.typeDisplay.sentence.label` | {typ} {function} {rela} \\ {role} {rule} |
| `configuration.typeDisplay.subphrase.label` | {typ} {function} {rela} \\ {typems} {role} {rule} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/function.md) Source: `docs/features/function.md`; configured at `configuration.docs.featureBase` |

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
| description | this is XML attribute function |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:12Z |
