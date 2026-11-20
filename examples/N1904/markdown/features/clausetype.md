# clausetype.tf

[← Corpus index](../index.md)

clause type

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The node feature clausetype stores a string-valued clause type on clause, sentence, and wg nodes. Populated counts are 5,237 clause nodes, 59 sentence nodes, and 5,296 wg nodes; missing nodes have no recorded value, not a negative class. The only observed value is nominalized (10,592 occurrences). Its relation to the overlapping feature cltype is undocumented.\n

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sentence](../../structure.html#type-sentence) | 59 (0.7%) |
| [clause](../../structure.html#type-clause) | 5,237 (12.3%) |
| [wg](../../structure.html#type-wg) | 5,296 (5.0%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "nominalized" | 10,592 | 100.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sentence nodes

| Compared feature(s) | φ | clausetype present when compared feature is present | clausetype present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.12 | 31 / 778 (4.0%) | 28 / 7,233 (0.4%) |
| [typems](typems.md) | -0.14 | 2 / 5,946 (0.0%) | 57 / 2,065 (2.8%) |

### clause nodes

| Compared feature(s) | φ | clausetype present when compared feature is present | clausetype present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.18 | 3,890 / 21,568 (18.0%) | 1,347 / 20,938 (6.4%) |
| [cls](cls.md) | +0.17 | 4,660 / 28,676 (16.3%) | 577 / 13,830 (4.2%) |
| [rule](rule.md) | +0.13 | 5,237 / 37,786 (13.9%) | 0 / 4,720 (0.0%) |
| [typems](typems.md) | -0.16 | 170 / 8,873 (1.9%) | 5,067 / 33,633 (15.1%) |
| [crule](crule.md), [nodeid](nodeid.md) | -0.13 | 0 / 4,720 (0.0%) | 5,237 / 37,786 (13.9%) |

### wg nodes

| Compared feature(s) | φ | clausetype present when compared feature is present | clausetype present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.15 | 3,921 / 45,276 (8.7%) | 1,375 / 61,592 (2.2%) |
| [junction](junction.md) | +0.10 | 1,778 / 17,921 (9.9%) | 3,518 / 88,947 (4.0%) |
| [cls](cls.md) | +0.10 | 4,694 / 72,788 (6.4%) | 602 / 34,080 (1.8%) |
| [typems](typems.md) | -0.29 | 172 / 68,710 (0.3%) | 5,124 / 38,158 (13.4%) |
| [typ](typ.md) | -0.22 | 0 / 51,733 (0.0%) | 5,296 / 55,135 (9.6%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/clausetype.md) Source: `docs/features/clausetype.md`; configured at `configuration.docs.featureBase` |

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
| description | clause type |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:11Z |
