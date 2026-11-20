# glyph.tf

[← Corpus index](../index.md)

representation (Unicode) of a word or sign

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 408,125 (81.5%) |
| [sign](../../structure.html#type-sign) | 1,430,241 (100.0%) |

## Frequent values

28,759 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "ו" | 188,859 | 10.3% |
| "י" | 125,341 | 6.8% |
| "ה" | 114,845 | 6.2% |
| "ל" | 105,689 | 5.7% |
| "" | 92,870 | 5.1% |
| "א" | 90,887 | 4.9% |
| "ב" | 82,605 | 4.5% |
| "ר" | 64,997 | 3.5% |
| "מ" | 63,340 | 3.4% |
| "ת" | 59,212 | 3.2% |
| "ש" | 56,354 | 3.1% |
| "ε" | 53,864 | 2.9% |

## Correlated features

- [glyphe](glyphe.md) word · φ +1.00

- [glypho](glypho.md) word · φ +1.00

- [glex](glex.md) word · φ +0.98

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | glyph present when compared feature is present | glyph present when compared feature is absent |
| --- | --- | --- | --- |
| [glyphe](glyphe.md), [glypho](glypho.md) | +1.00 | 408,125 / 408,125 (100.0%) | 0 / 92,870 (0.0%) |
| [glex](glex.md), [glexe](glexe.md), [glexo](glexo.md) | +0.98 | 405,715 / 405,736 (100.0%) | 2,410 / 95,259 (2.5%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.98 | 405,813 / 406,914 (99.7%) | 2,312 / 94,081 (2.5%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -0.53 | 0 / 29,927 (0.0%) | 408,125 / 471,068 (86.6%) |
| [after](after.md) | -0.25 | 296,974 / 389,180 (76.3%) | 111,151 / 111,815 (99.4%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [text-orig-full rendering format](../../text.html#format-15716cf41c30) | `{glyph}{punc}{after}` Uses: [glyph](glyph.md), [punc](punc.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:00Z |
| description | representation (Unicode) of a word or sign |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
