# damage.tf

[← Corpus index](../index.md)

whether a sign is damaged

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

In the AbB Old Babylonian Cuneiform Text-Fabric corpus, the node feature damage records whether a sign is damaged. It is attached to sign nodes and exhibits one distinct value, 1, on 9,974 of the corpus's 203,219 signs. The feature is part of the sign_status_flags family, which also includes missing, supplied, uncertain, excised, det, langalt, question, collated, remarkable, flags, and operator. The inventory does not explain how undamaged or unassessed signs are represented, nor does it define the meaning of the single observed value beyond the feature label.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 9,974 (4.9%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 9,974 | 100.0% |

## Correlated features

- [flags](flags.md) sign · φ +0.97

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | damage present when compared feature is present | damage present when compared feature is absent |
| --- | --- | --- | --- |
| [flags](flags.md) | +0.97 | 9,974 / 10,498 (95.0%) | 0 / 192,721 (0.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | whether a sign is damaged |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
