# cltype.tf

[← Corpus index](../index.md)

clause type

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

cltype is a node feature recording clause type. Values are populated on clause (2,718 nodes), sentence (125), and wg (2,843); unpopulated nodes have no recorded value rather than a negative class. Three distinct values occur: VerbElided (2,100), Verbless (1,922), and Minor (1,664). The feature's relation to clausetype, which shares the 'clause type' label but may use different values, remains unverified.\n

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sentence](../../structure.html#type-sentence) | 125 (1.6%) |
| [clause](../../structure.html#type-clause) | 2,718 (6.4%) |
| [wg](../../structure.html#type-wg) | 2,843 (2.7%) |

## Frequent values

3 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "VerbElided" | 2,100 | 36.9% |
| "Verbless" | 1,922 | 33.8% |
| "Minor" | 1,664 | 29.3% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sentence nodes

| Compared feature(s) | φ | cltype present when compared feature is present | cltype present when compared feature is absent |
| --- | --- | --- | --- |
| [function](function.md) | +0.36 | 118 / 778 (15.2%) | 7 / 7,233 (0.1%) |
| [cls](cls.md) | +0.26 | 124 / 1,476 (8.4%) | 1 / 6,535 (0.0%) |
| [typems](typems.md) | -0.21 | 0 / 5,946 (0.0%) | 125 / 2,065 (6.1%) |

### clause nodes

| Compared feature(s) | φ | cltype present when compared feature is present | cltype present when compared feature is absent |
| --- | --- | --- | --- |
| [articular](articular.md) | +0.14 | 614 / 3,386 (18.1%) | 2,104 / 39,120 (5.4%) |
| [role](role.md) | -0.14 | 155 / 12,795 (1.2%) | 2,563 / 29,711 (8.6%) |
| [typems](typems.md) | -0.13 | 0 / 8,873 (0.0%) | 2,718 / 33,633 (8.1%) |

### wg nodes

| Compared feature(s) | φ | cltype present when compared feature is present | cltype present when compared feature is absent |
| --- | --- | --- | --- |
| [junction](junction.md) | +0.13 | 1,309 / 17,921 (7.3%) | 1,534 / 88,947 (1.7%) |
| [typems](typems.md) | -0.22 | 0 / 68,710 (0.0%) | 2,843 / 38,158 (7.5%) |
| [typ](typ.md) | -0.16 | 0 / 51,733 (0.0%) | 2,843 / 55,135 (5.2%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/cltype.md) Source: `docs/features/cltype.md`; configured at `configuration.docs.featureBase` |

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
