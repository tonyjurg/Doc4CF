# question.tf

[← Corpus index](../index.md)

whether a sign has the question flag (?)

Node · UTF-8 · int

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The question feature indicates whether a sign carries the ATF question flag (?). It is a node-level integer feature sourced from sign nodes, exhibiting one distinct value (1) on 560 signs. It belongs to the sign_status_flags family together with missing, supplied, uncertain, damage, excised, det, langalt, collated, remarkable, flags, operator, operatorr, and operatoru. The separate flags feature records sequences of ATF flags after a sign and may include ? among values such as #, !, *, #?, and ?#. The inventory does not specify whether question and flags encode the same marker independently or whether question=1 simply marks presence.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [sign](../../structure.html#type-sign) | 560 (0.3%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 560 | 100.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### sign nodes

| Compared feature(s) | φ | question present when compared feature is present | question present when compared feature is absent |
| --- | --- | --- | --- |
| [flags](flags.md) | +0.23 | 560 / 10,498 (5.3%) | 0 / 192,721 (0.0%) |
| [grapheme](grapheme.md), [graphemer](graphemer.md), [graphemeu](graphemeu.md) | +0.18 | 246 / 3,011 (8.2%) | 314 / 200,208 (0.2%) |
| [reading](reading.md), [readingr](readingr.md), [readingu](readingu.md) | -0.16 | 315 / 199,359 (0.2%) | 245 / 3,860 (6.3%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.sign.features` | collated remarkable question damage det uncertain missing excised supplied langalt comment remarks repeat fraction operator grapheme |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | whether a sign has the question flag (?) |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | int |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
