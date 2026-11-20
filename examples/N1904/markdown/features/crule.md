# crule.tf

[← Corpus index](../index.md)

clause rule (from xml attribute Rule)

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

crule is a string node feature sourced from the XML attribute Rule and described as 'clause rule.' It has values on 4,720 clause, 838 sentence, and 5,558 wg nodes; observed values are ClCl (8,616) and ClCl2 (2,500). Unpopulated nodes have no recorded value. The feature also appears beyond clause nodes, and the meaning of ClCl versus ClCl2 is undocumented.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sentence](../../structure.html#type-sentence) | 838 (10.5%) |
| [clause](../../structure.html#type-clause) | 4,720 (11.1%) |
| [wg](../../structure.html#type-wg) | 5,558 (5.2%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "ClCl" | 8,616 | 77.5% |
| "ClCl2" | 2,500 | 22.5% |

## Correlated features

- [nodeid](nodeid.md) sentence · φ +1.00

- [cls](cls.md) sentence · φ +0.56

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sentence nodes

| Compared feature(s) | φ | crule present when compared feature is present | crule present when compared feature is absent |
| --- | --- | --- | --- |
| [nodeid](nodeid.md) | +1.00 | 838 / 838 (100.0%) | 0 / 7,173 (0.0%) |
| [cls](cls.md) | +0.56 | 691 / 1,476 (46.8%) | 147 / 6,535 (2.2%) |
| [rule](rule.md) | -1.00 | 0 / 7,173 (0.0%) | 838 / 838 (100.0%) |
| [typems](typems.md) | -0.58 | 0 / 5,946 (0.0%) | 838 / 2,065 (40.6%) |

### clause nodes

| Compared feature(s) | φ | crule present when compared feature is present | crule present when compared feature is absent |
| --- | --- | --- | --- |
| [nodeid](nodeid.md) | +1.00 | 4,720 / 4,720 (100.0%) | 0 / 37,786 (0.0%) |
| [cls](cls.md) | +0.18 | 4,281 / 28,676 (14.9%) | 439 / 13,830 (3.2%) |
| [rule](rule.md) | -1.00 | 0 / 37,786 (0.0%) | 4,720 / 4,720 (100.0%) |
| [function](function.md) | -0.36 | 0 / 21,568 (0.0%) | 4,720 / 20,938 (22.5%) |

### wg nodes

| Compared feature(s) | φ | crule present when compared feature is present | crule present when compared feature is absent |
| --- | --- | --- | --- |
| [nodeid](nodeid.md) | +1.00 | 5,558 / 5,558 (100.0%) | 0 / 101,310 (0.0%) |
| [cls](cls.md) | +0.11 | 4,972 / 72,788 (6.8%) | 586 / 34,080 (1.7%) |
| [rule](rule.md) | -0.61 | 0 / 93,234 (0.0%) | 5,558 / 13,634 (40.8%) |
| [typems](typems.md) | -0.31 | 1 / 68,710 (0.0%) | 5,557 / 38,158 (14.6%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/crule.md) Source: `docs/features/crule.md`; configured at `configuration.docs.featureBase` |

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
| description | clause rule (from xml attribute Rule) |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:11Z |
