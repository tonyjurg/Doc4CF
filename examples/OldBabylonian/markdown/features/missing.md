# missing.tf

[← Corpus index](../index.md)

whether a sign is missing - between square brackets [ ]

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The feature missing is a node-level integer feature on signs in the AbB Old Babylonian Cuneiform Text-Fabric corpus. It records whether a sign is missing, represented in ATF by square brackets [ ]. The feature has one distinct value, 1, which occurs 14,391 times on sign nodes out of 203,219 total signs. It belongs to the sign_status_flags feature family, which also includes supplied, uncertain, damage, excised, det, langalt, question, collated, remarkable, flags, and operator features. No targets are defined for missing, and its source is limited to sign nodes.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 14,391 (7.1%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 14,391 | 100.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | missing present when compared feature is present | missing present when compared feature is absent |
| --- | --- | --- | --- |
| [atfpre](atfpre.md) | +0.44 | 8,662 / 21,769 (39.8%) | 5,729 / 181,450 (3.2%) |
| [atfpost](atfpost.md) | +0.40 | 8,092 / 21,969 (36.8%) | 6,299 / 181,250 (3.5%) |
| [uncertain](uncertain.md) | +0.27 | 1,176 / 1,194 (98.5%) | 13,215 / 202,025 (6.5%) |
| [reading](reading.md), [readingr](readingr.md), [readingu](readingu.md) | -0.19 | 12,768 / 199,359 (6.4%) | 1,623 / 3,860 (42.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | whether a sign is missing - between square brackets [ ] |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
