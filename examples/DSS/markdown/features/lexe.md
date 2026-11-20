# lexe.tf

[← Corpus index](../index.md)

representation (ETCBC transliteration) of a lexeme

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [lex](../../structure.html#type-lex) | 10,450 (100.0%) |
| [word](../../structure.html#type-word) | 470,845 (94.0%) |

## Frequent values

10,450 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| " # " | 54,190 | 11.3% |
| "W:" | 45,091 | 9.4% |
| "L:" | 21,550 | 4.5% |
| "B.:" | 19,711 | 4.1% |
| "HA" | 18,759 | 3.9% |
| " # # # " | 10,813 | 2.2% |
| "K.OL" | 7,411 | 1.5% |
| "MIn" | 7,201 | 1.5% |
| ">;T_1" | 7,192 | 1.5% |
| "LO>" | 5,078 | 1.1% |
| "<AL_2" | 4,879 | 1.0% |
| ">:ACER" | 4,873 | 1.0% |

## Correlated features

- [lex](lex.md) word · φ +1.00

- [lexo](lexo.md) word · φ +1.00

- [morpho](morpho.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | lexe present when compared feature is present | lexe present when compared feature is absent |
| --- | --- | --- | --- |
| [lex](lex.md), [lexo](lexo.md) | +1.00 | 470,845 / 470,845 (100.0%) | 0 / 30,150 (0.0%) |
| [morpho](morpho.md), [sp](sp.md) | +1.00 | 470,841 / 470,845 (100.0%) | 4 / 30,150 (0.0%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.53 | 406,913 / 406,914 (100.0%) | 63,932 / 94,081 (68.0%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -1.00 | 2 / 29,927 (0.0%) | 470,843 / 471,068 (100.0%) |
| [after](after.md) | -0.13 | 359,246 / 389,180 (92.3%) | 111,599 / 111,815 (99.8%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.lex.features` | lex lexe |
| [lex-default rendering format](../../text.html#format-289c8aabd18f) | `word#{lang:h}-{lex}-{lexe}-{lexo} ` Uses: `lang:h`, [lex](lex.md), [lexe](lexe.md), [lexo](lexo.md) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:07Z |
| description | representation (ETCBC transliteration) of a lexeme |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
