# afterr.tf

[← Corpus index](../index.md)

what comes after a sign or word (- or space); between adjacent signs a ␣ is inserted

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The node feature `afterr` records what comes after a sign or word in ATF transcription. It is defined on both sign and word nodes, with 175,844 sign targets and 50,099 word targets. Its seven distinct values include `-` (118,903 occurrences), space (100,198 occurrences), `⁼` (6,819 occurrences), `/` (15), `.` (5), `+` (2), and `:` (1). Between adjacent signs, a space is inserted. `afterr` participates in the `text-orig-plain` format (`{sym}{afterr}`) and the `text-orig-rich` format (`{symr}{afterr}`). It is a variant of `after` and `afteru`, though the precise scope separating these variants is not fully specified in the inventory.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 50,099 (65.5%) |
| [sign](../../structure.html#type-sign) | 175,844 (86.5%) |

## Frequent values

7 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "-" | 118,903 | 52.6% |
| " " | 100,198 | 44.3% |
| "⁼" | 6,819 | 3.0% |
| "/" | 15 | 0.0% |
| "." | 5 | 0.0% |
| "+" | 2 | 0.0% |
| ":" | 1 | 0.0% |

## Correlated features

- [after](after.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | afterr present when compared feature is present | afterr present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md) | +1.00 | 50,099 / 50,099 (100.0%) | 0 / 26,406 (0.0%) |

### sign nodes

| Compared feature(s) | φ | afterr present when compared feature is present | afterr present when compared feature is absent |
| --- | --- | --- | --- |
| [after](after.md) | +0.88 | 169,025 / 169,025 (100.0%) | 6,819 / 34,194 (19.9%) |
| [afteru](afteru.md) | +0.23 | 50,122 / 50,122 (100.0%) | 125,722 / 153,097 (82.1%) |
| [reading](reading.md), [readingr](readingr.md), [readingu](readingu.md) | +0.18 | 174,174 / 199,359 (87.4%) | 1,670 / 3,860 (43.3%) |
| [comment](comment.md) | -0.18 | 2 / 971 (0.2%) | 175,842 / 202,248 (86.9%) |
| [atfpost](atfpost.md) | -0.11 | 16,650 / 21,969 (75.8%) | 159,194 / 181,250 (87.8%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [text-orig-plain rendering format](../../text.html#format-c2974482636a) | `{sym}{afterr}` Uses: [sym](sym.md), [afterr](afterr.md) |
| [text-orig-rich rendering format](../../text.html#format-f2ec8daf7edb) | `{symr}{afterr}` Uses: [symr](symr.md), [afterr](afterr.md) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | what comes after a sign or word (- or space); between adjacent signs a ␣ is inserted |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:07Z |
