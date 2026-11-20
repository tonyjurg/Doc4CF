# uncertain.tf

[← Corpus index](../index.md)

whether a sign is uncertain - between brackets ( )

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The uncertain feature is a node-level integer property on sign nodes in the AbB Old Babylonian Cuneiform corpus. Its source description states that it marks whether a sign is uncertain, corresponding to ATF content enclosed in round parentheses ( ). The inventory records exactly one distinct value, 1, attested on 1,194 sign nodes; the corpus contains 203,219 signs in total. The feature belongs to the sign-status condition family alongside missing, supplied, and question. The inventory does not specify whether unmarked signs implicitly have value 0, whether the feature is sparse, or what semantic weight value 1 carries beyond simple presence.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 1,194 (0.6%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 1,194 | 100.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | uncertain present when compared feature is present | uncertain present when compared feature is absent |
| --- | --- | --- | --- |
| [missing](missing.md) | +0.27 | 1,176 / 14,391 (8.2%) | 18 / 188,828 (0.0%) |
| [atfpre](atfpre.md) | +0.22 | 1,185 / 21,769 (5.4%) | 9 / 181,450 (0.0%) |
| [atfpost](atfpost.md) | +0.22 | 1,184 / 21,969 (5.4%) | 10 / 181,250 (0.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | whether a sign is uncertain - between brackets ( ) |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:10Z |
