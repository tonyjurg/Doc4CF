# repeat.tf

[← Corpus index](../index.md)

repeat of a numeral; the value n (unknown) is represented as -1

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The repeat feature records how many times a numeral sign is repeated in the AbB Old Babylonian Cuneiform Text-Fabric corpus. It is a node-level feature sourced from sign nodes, with 2,060 attested occurrences and 9 distinct values. Frequent values are 1 (877 occurrences), 2 (398), 5 (246), 3 (239), 4 (152), 6 (67), 8 (40), 7 (26), and 9 (15). The feature belongs to the Numeral Attributes family alongside fraction, which records fractional values such as 1/2, 1/3, 2/3, and 5/6 for numeral signs.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 2,060 (1.0%) |

## Frequent values

9 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 877 | 42.6% |
| 2 | 398 | 19.3% |
| 5 | 246 | 11.9% |
| 3 | 239 | 11.6% |
| 4 | 152 | 7.4% |
| 6 | 67 | 3.3% |
| 8 | 40 | 1.9% |
| 7 | 26 | 1.3% |
| 9 | 15 | 0.7% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | repeat present when compared feature is present | repeat present when compared feature is absent |
| --- | --- | --- | --- |
| [langalt](langalt.md) | +0.18 | 1,262 / 19,063 (6.6%) | 798 / 184,156 (0.4%) |
| [afteru](afteru.md) | +0.15 | 1,801 / 50,122 (3.6%) | 259 / 153,097 (0.2%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | repeat of a numeral; the value n (unknown) is represented as -1 |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:09Z |
