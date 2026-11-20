# langalt.tf

[← Corpus index](../index.md)

1 if a sign is in the alternate language (i.e. Sumerian) - between underscores _ _

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The `langalt` feature is a node-level boolean marker on sign nodes in the AbB Old Babylonian Cuneiform corpus. It indicates that a sign is written in the alternate language, identified in the corpus context as Sumerian, and is delimited in ATF transcription by underscores (`_ _`). The feature has exactly one distinct value, 1, observed on 19,063 sign nodes. It belongs to the sign_status_flags feature family, which also includes missing, supplied, uncertain, damage, excised, det, question, collated, remarkable, flags, operator, operatorr, and operatoru. While document language is predominantly Akkadian with a minority of Sumerian, the precise criteria for assigning langalt at the sign level versus the document-level lang feature are not specified.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 19,063 (9.4%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 19,063 | 100.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | langalt present when compared feature is present | langalt present when compared feature is absent |
| --- | --- | --- | --- |
| [atfpost](atfpost.md) | +0.38 | 9,032 / 21,969 (41.1%) | 10,031 / 181,250 (5.5%) |
| [atfpre](atfpre.md) | +0.34 | 8,254 / 21,769 (37.9%) | 10,809 / 181,450 (6.0%) |
| [repeat](repeat.md) | +0.18 | 1,262 / 2,060 (61.3%) | 17,801 / 201,159 (8.8%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | 1 if a sign is in the alternate language (i.e. Sumerian) - between underscores _ _ |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
