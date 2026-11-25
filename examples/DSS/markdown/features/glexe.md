# glexe.tf

[← Corpus index](../index.md)

representation (ETCBC transliteration) of a lexeme leaving out non-letters

Node · UTF-8 · str

## Generated description

The glexe node feature stores an ETCBC transliteration of a lexeme with non\-letters omitted as a string\. Populated values occur on lex nodes and word nodes; absent assignments mean no value is recorded, not a negative class\. The feature appears in the lex\-trans\-full text format template together with lang, punce, and after, though runtime consumption is unverified\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [lex](../../structure.html#type-lex) | 10,444 (99.9%) |
| [word](../../structure.html#type-word) | 405,736 (81.0%) |

## Frequent values

8,264 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "W:" | 45,091 | 10.8% |
| "L:" | 21,550 | 5.2% |
| "B.:" | 19,711 | 4.7% |
| "HA" | 18,759 | 4.5% |
| ">;T" | 7,675 | 1.8% |
| "K.OL" | 7,411 | 1.8% |
| "MIn" | 7,201 | 1.7% |
| "<AL" | 5,432 | 1.3% |
| "LO>" | 5,078 | 1.2% |
| ">:ACER" | 4,873 | 1.2% |
| "JHWH" | 4,844 | 1.2% |
| "K.IJ" | 4,101 | 1.0% |

## Correlated features

- [glex](glex.md) word · φ +1.00

- [glexo](glexo.md) word · φ +1.00

- [lex_utf8_etcbc](lex_utf8_etcbc.md) word · φ +0.99

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | glexe present when compared feature is present | glexe present when compared feature is absent |
| --- | --- | --- | --- |
| [glex](glex.md), [glexo](glexo.md) | +1.00 | 405,736 / 405,736 (100.0%) | 0 / 95,259 (0.0%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.99 | 405,649 / 406,914 (99.7%) | 87 / 94,081 (0.1%) |
| [glyph](glyph.md), [glyphe](glyphe.md), [glypho](glypho.md) | +0.98 | 405,715 / 408,125 (99.4%) | 21 / 92,870 (0.0%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -0.52 | 1 / 29,927 (0.0%) | 405,735 / 471,068 (86.1%) |
| [after](after.md) | -0.25 | 294,604 / 389,180 (75.7%) | 111,132 / 111,815 (99.4%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [lex-trans-full rendering format](../../text.html#format-449a2f9052e2) | `word#{lang:h}-{glexe}{punce}{after}` Uses: `lang:h`, [glexe](glexe.md), [punce](punce.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:01:59Z |
| description | representation (ETCBC transliteration) of a lexeme leaving out non-letters |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
