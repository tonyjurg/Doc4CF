# punco.tf

[← Corpus index](../index.md)

trailing punctuation (original source) of a word

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 29,927 (6.0%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "." | 29,909 | 99.9% |
| "±" | 18 | 0.1% |

## Correlated features

- [punc](punc.md) word · φ +1.00

- [punce](punce.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | punco present when compared feature is present | punco present when compared feature is absent |
| --- | --- | --- | --- |
| [punc](punc.md), [punce](punce.md) | +1.00 | 29,927 / 29,927 (100.0%) | 0 / 471,068 (0.0%) |
| [after](after.md) | +0.13 | 29,717 / 389,180 (7.6%) | 210 / 111,815 (0.2%) |
| [lex](lex.md), [lexe](lexe.md), [lexo](lexo.md) | -1.00 | 2 / 470,845 (0.0%) | 29,925 / 30,150 (99.3%) |
| [morpho](morpho.md), [sp](sp.md) | -1.00 | 2 / 470,845 (0.0%) | 29,925 / 30,150 (99.3%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [lex-source-full rendering format](../../text.html#format-a48c95b2ff30) | `word#{lang:h}-{glexo}{punco}{after}` Uses: `lang:h`, [glexo](glexo.md), [punco](punco.md), [after](after.md) |
| [morph-source-full rendering format](../../text.html#format-70e7f3d1fdff) | `word#{morpho}{punco}{after}` Uses: [morpho](morpho.md), [punco](punco.md), [after](after.md) |
| [text-source-full rendering format](../../text.html#format-411816244e4a) | `{glypho}{punco}{after}` Uses: [glypho](glypho.md), [punco](punco.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:11Z |
| description | trailing punctuation (original source) of a word |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
