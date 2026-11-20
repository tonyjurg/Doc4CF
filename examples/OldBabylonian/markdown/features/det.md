# det.tf

[← Corpus index](../index.md)

whether a sign is a determinative gloss - between braces { }

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The `det` feature is a node-level integer feature on signs in the AbB Old Babylonian Cuneiform corpus. Its authoritative source description states that it marks whether a sign is a determinative gloss, rendered in ATF between braces `{ }`. The feature records one distinct value, `1`, on 6,796 sign nodes, and has no edge targets. It belongs to the sign_status_flags family, which groups sign-condition features including missing, supplied, uncertain, damage, excised, langalt, question, collated, remarkable, flags, operator, operatorr, and operatoru. The corpus contains 203,219 signs, so determinatives occur on a minority of nodes. The precise semantics of value `1` and whether unmarked signs are negative or unannotated are not specified.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 6,796 (3.3%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 6,796 | 100.0% |

## Correlated features

- [atfpre](atfpre.md) sign · φ +0.54

- [atfpost](atfpost.md) sign · φ +0.53

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | det present when compared feature is present | det present when compared feature is absent |
| --- | --- | --- | --- |
| [atfpre](atfpre.md) | +0.54 | 6,794 / 21,769 (31.2%) | 2 / 181,450 (0.0%) |
| [atfpost](atfpost.md) | +0.53 | 6,794 / 21,969 (30.9%) | 2 / 181,250 (0.0%) |
| [after](after.md) | -0.38 | 523 / 169,025 (0.3%) | 6,273 / 34,194 (18.3%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | whether a sign is a determinative gloss - between braces { } |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
