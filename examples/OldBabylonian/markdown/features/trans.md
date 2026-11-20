# trans.tf

[← Corpus index](../index.md)

whether a line has a translation

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The feature `trans` is a node-level line-node feature in the AbB Old Babylonian Cuneiform Text-Fabric corpus. Its description states it indicates whether a line has a translation. It has one distinct value, `1`, observed on 134 line nodes, with no targets listed. It belongs to the Line Structure and Numbering family with `ln`, `lnno`, `lnc`, `col`, `primecol`, `primeln`, `remarks`, and `translation@en`. The corpus has 1,285 documents, 2,834 faces, and 27,375 lines, so translations appear on a small subset of lines. The meaning of `1` is implied but not explicitly defined in the supplied inventory.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [line](../../structure.html#type-line) | 134 (0.5%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 134 | 100.0% |

## Correlated features

- [translation@en](translation%40en.md) line · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### line nodes

| Compared feature(s) | φ | trans present when compared feature is present | trans present when compared feature is absent |
| --- | --- | --- | --- |
| [translation@en](translation%40en.md) | +1.00 | 134 / 134 (100.0%) | 0 / 27,241 (0.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.dataDisplay.textFormats.layout-orig-rich.style` | trans |
| `configuration.dataDisplay.textFormats.text-orig-plain.style` | trans |
| `configuration.dataDisplay.textFormats.text-orig-rich.style` | trans |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | whether a line has a translation |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:10Z |
