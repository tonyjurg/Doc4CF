# after.tf

[← Corpus index](../index.md)

what comes after a sign or word (- or space)

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The node feature after records the trailing text that follows a sign or word in ATF transcription. It is attested on 169,025 sign nodes and 50,099 word nodes. Six distinct values occur: hyphen (-) 118,903 times, space ( ) 100,198 times, slash (/) 15 times, period (.) 5 times, plus (+) 2 times, and colon (:) 1 time. The related features afterr and afteru are described as parallel "what comes after" variants, but the inventory does not specify how after differs from afterr beyond the undocumented claim that afterr inserts a space between adjacent signs. This distinction is tentative.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 50,099 (65.5%) |
| [sign](../../structure.html#type-sign) | 169,025 (83.2%) |

## Frequent values

6 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "-" | 118,903 | 54.3% |
| " " | 100,198 | 45.7% |
| "/" | 15 | 0.0% |
| "." | 5 | 0.0% |
| "+" | 2 | 0.0% |
| ":" | 1 | 0.0% |

## Correlated features

- [afterr](afterr.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | after present when compared feature is present | after present when compared feature is absent |
| --- | --- | --- | --- |
| [afterr](afterr.md) | +1.00 | 50,099 / 50,099 (100.0%) | 0 / 26,406 (0.0%) |

### sign nodes

| Compared feature(s) | φ | after present when compared feature is present | after present when compared feature is absent |
| --- | --- | --- | --- |
| [afterr](afterr.md) | +0.88 | 169,025 / 175,844 (96.1%) | 0 / 27,375 (0.0%) |
| [afteru](afteru.md) | +0.26 | 50,122 / 50,122 (100.0%) | 118,903 / 153,097 (77.7%) |
| [reading](reading.md), [readingr](readingr.md), [readingu](readingu.md) | +0.15 | 167,369 / 199,359 (84.0%) | 1,656 / 3,860 (42.9%) |
| [det](det.md) | -0.38 | 523 / 6,796 (7.7%) | 168,502 / 196,423 (85.8%) |
| [atfpost](atfpost.md) | -0.31 | 10,842 / 21,969 (49.4%) | 158,183 / 181,250 (87.3%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [text-orig-full rendering format](../../text.html#format-15716cf41c30) | `{atfpre}{atf}{atfpost}{after}` Uses: [atfpre](atfpre.md), [atf](atf.md), [atfpost](atfpost.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | what comes after a sign or word (- or space) |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:07Z |
