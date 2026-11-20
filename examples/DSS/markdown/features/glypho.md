# glypho.tf

[← Corpus index](../index.md)

representation (original source) of a word or sign

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 408,125 (81.5%) |
| [sign](../../structure.html#type-sign) | 1,430,241 (100.0%) |

## Frequent values

28,756 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "w" | 188,859 | 10.3% |
| "y" | 125,341 | 6.8% |
| "h" | 114,845 | 6.2% |
| "l" | 105,689 | 5.7% |
| "" | 92,870 | 5.1% |
| "a" | 90,887 | 4.9% |
| "b" | 82,605 | 4.5% |
| "r" | 64,997 | 3.5% |
| "m" | 63,340 | 3.4% |
| "t" | 59,212 | 3.2% |
| "C" | 56,518 | 3.1% |
| "--" | 53,864 | 2.9% |

## Correlated features

- [glyph](glyph.md) word · φ +1.00

- [glyphe](glyphe.md) word · φ +1.00

- [glex](glex.md) word · φ +0.98

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | glypho present when compared feature is present | glypho present when compared feature is absent |
| --- | --- | --- | --- |
| [glyph](glyph.md), [glyphe](glyphe.md) | +1.00 | 408,125 / 408,125 (100.0%) | 0 / 92,870 (0.0%) |
| [glex](glex.md), [glexe](glexe.md), [glexo](glexo.md) | +0.98 | 405,715 / 405,736 (100.0%) | 2,410 / 95,259 (2.5%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.98 | 405,813 / 406,914 (99.7%) | 2,312 / 94,081 (2.5%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -0.53 | 0 / 29,927 (0.0%) | 408,125 / 471,068 (86.6%) |
| [after](after.md) | -0.25 | 296,974 / 389,180 (76.3%) | 111,151 / 111,815 (99.4%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [text-source-full rendering format](../../text.html#format-411816244e4a) | `{glypho}{punco}{after}` Uses: [glypho](glypho.md), [punco](punco.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:04Z |
| description | representation (original source) of a word or sign |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
