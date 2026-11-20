# before.tf

[← Corpus index](../index.md)

this is XML attribute before

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The node feature `before` records the XML attribute `before` as a string on phrase (16 nodes), subphrase (18 nodes), and word (34 nodes). It is part of the default text-orig-full display template `{before}{text}{after}` and likely holds punctuation or editorial material preceding the surface text. Observed values are `—` (32), `(` (20), `[[` (14), and `[` (2); populated-node counts are not negative-class assignments.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [phrase](../../structure.html#type-phrase) | 16 (0.0%) |
| [subphrase](../../structure.html#type-subphrase) | 18 (0.0%) |
| [word](../../structure.html#type-word) | 34 (0.0%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "—" | 32 | 47.1% |
| "(" | 20 | 29.4% |
| "[[" | 14 | 20.6% |
| "[" | 2 | 2.9% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### phrase nodes

| Compared feature(s) | φ | before present when compared feature is present | before present when compared feature is absent |
| --- | --- | --- | --- |
| [criticalsign](criticalsign.md) | +0.36 | 8 / 30 (26.7%) | 8 / 68,977 (0.0%) |

### subphrase nodes

| Compared feature(s) | φ | before present when compared feature is present | before present when compared feature is absent |
| --- | --- | --- | --- |
| [criticalsign](criticalsign.md) | +0.45 | 11 / 33 (33.3%) | 7 / 116,145 (0.0%) |

### word nodes

| Compared feature(s) | φ | before present when compared feature is present | before present when compared feature is absent |
| --- | --- | --- | --- |
| [criticalsign](criticalsign.md) | +0.41 | 19 / 63 (30.2%) | 15 / 137,716 (0.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [text-orig-full rendering format](../../text.html#format-15716cf41c30) | `{before}{text}{after}` Uses: [before](before.md), [text](text.md), [after](after.md) |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/before.md) Source: `docs/features/before.md`; configured at `configuration.docs.featureBase` |

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
| description | this is XML attribute before |
| editors | Eberhart Nestle (1904) |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:09Z |
