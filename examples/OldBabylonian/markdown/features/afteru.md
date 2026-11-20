# afteru.tf

[← Corpus index](../index.md)

what comes after a sign when represented as unicode (space)

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The afteru feature is a node-level attribute on sign nodes that records the Unicode text immediately following a sign in ATF transcription. It belongs to the sign_surroundings feature family alongside atfpre and atfpost, which capture cluster openings and closings. The corpus configures afteru for the text-orig-unicode original-text format ({symu}{afteru}). Observed values on 50,122 sign nodes include a space (50,099 occurrences), slash (15), period (5), plus (2), and colon (1), with five distinct values total. The precise distinction between afteru and the ASCII variants after and afterr remains unspecified, particularly whether the frequent space value marks inter-sign spacing or genuine trailing text.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 50,122 (24.7%) |

## Frequent values

5 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| " " | 50,099 | 100.0% |
| "/" | 15 | 0.0% |
| "." | 5 | 0.0% |
| "+" | 2 | 0.0% |
| ":" | 1 | 0.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | afteru present when compared feature is present | afteru present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md) | +0.26 | 50,122 / 169,025 (29.7%) | 0 / 34,194 (0.0%) |
| [afterr](afterr.md) | +0.23 | 50,122 / 175,844 (28.5%) | 0 / 27,375 (0.0%) |
| [langalt](langalt.md) | +0.15 | 8,511 / 19,063 (44.6%) | 41,611 / 184,156 (22.6%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [text-orig-unicode rendering format](../../text.html#format-329463eae36f) | `{symu}{afteru}` Uses: [symu](symu.md), [afteru](afteru.md) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | what comes after a sign when represented as unicode (space) |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:07Z |
