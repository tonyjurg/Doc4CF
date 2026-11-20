# junction.tf

[← Corpus index](../index.md)

type of junction

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The junction feature is a node-level annotation recording the type of junction as either coordinate or subordinate. It is populated on clause (17,741 nodes), wg (17,921), subphrase (123), and phrase (57) nodes in the Greek New Testament (Nestle 1904) corpus. Frequent values are coordinate (18,734) and subordinate (17,108). Junction also appears in clause and wg node label templates.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [clause](../../structure.html#type-clause) | 17,741 (41.7%) |
| [wg](../../structure.html#type-wg) | 17,921 (16.8%) |
| [phrase](../../structure.html#type-phrase) | 57 (0.1%) |
| [subphrase](../../structure.html#type-subphrase) | 123 (0.1%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "coordinate" | 18,734 | 52.3% |
| "subordinate" | 17,108 | 47.7% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### clause nodes

| Compared feature(s) | φ | junction present when compared feature is present | junction present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.41 | 13,343 / 21,568 (61.9%) | 4,398 / 20,938 (21.0%) |
| [cls](cls.md) | +0.35 | 15,406 / 28,676 (53.7%) | 2,335 / 13,830 (16.9%) |
| [rule](rule.md) | +0.30 | 17,741 / 37,786 (47.0%) | 0 / 4,720 (0.0%) |
| [typems](typems.md) | -0.32 | 1,011 / 8,873 (11.4%) | 16,730 / 33,633 (49.7%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.30 | 0 / 4,720 (0.0%) | 17,741 / 37,786 (47.0%) |

### wg nodes

| Compared feature(s) | φ | junction present when compared feature is present | junction present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.29 | 13,400 / 45,276 (29.6%) | 4,521 / 61,592 (7.3%) |
| [cls](cls.md) | +0.17 | 15,406 / 72,788 (21.2%) | 2,515 / 34,080 (7.4%) |
| [rule](rule.md) | +0.17 | 17,921 / 93,234 (19.2%) | 0 / 13,634 (0.0%) |
| [typems](typems.md) | -0.55 | 1,076 / 68,710 (1.6%) | 16,845 / 38,158 (44.1%) |
| [typ](typ.md) | -0.43 | 0 / 51,733 (0.0%) | 17,921 / 55,135 (32.5%) |

### phrase nodes

| Compared feature(s) | φ | junction present when compared feature is present | junction present when compared feature is absent |
| --- | --- | --- | --- |
| [cls](cls.md) | -0.16 | 0 / 66,851 (0.0%) | 57 / 2,156 (2.6%) |

### subphrase nodes

| Compared feature(s) | φ | junction present when compared feature is present | junction present when compared feature is absent |
| --- | --- | --- | --- |
| [cls](cls.md) | -0.21 | 0 / 113,564 (0.0%) | 123 / 2,614 (4.7%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.clause.label` | {typ} {function} {rela} \\ {cls} {role} {junction} |
| `configuration.typeDisplay.wg.label` | {typems} {role} {rule} {junction} |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/junction.md) Source: `docs/features/junction.md`; configured at `configuration.docs.featureBase` |

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
| description | type of junction |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:13Z |
