# glexo.tf

[← Corpus index](../index.md)

representation (original source) of a lexeme leaving out non-letters

Node · UTF-8 · str

## Generated description

glexo is a node feature in the Dead Sea Scrolls corpus \(acronym dss\) storing the original\-source representation of a lexeme with non\-letters removed\. Values are populated on lex and word nodes, including forms such as 'w◊' and 'yhwh'; missing assignments indicate no recorded value, not a negative class\. It is used in the lex\-source\-full text format with punco\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [lex](../../structure.html#type-lex) | 10,444 (99.9%) |
| [word](../../structure.html#type-word) | 405,736 (81.0%) |

## Frequent values

12,419 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "w◊" | 45,091 | 10.8% |
| "lV" | 21,550 | 5.2% |
| "b;V" | 19,711 | 4.7% |
| "hA" | 18,759 | 4.5% |
| "aEt" | 7,672 | 1.8% |
| "k;Ol" | 7,411 | 1.8% |
| "mIN" | 7,201 | 1.7% |
| "oAl" | 5,430 | 1.3% |
| "løa" | 5,078 | 1.2% |
| "aSvRr" | 4,873 | 1.2% |
| "yhwh" | 4,844 | 1.2% |
| "k;Iy" | 4,100 | 1.0% |

## Correlated features

- [glex](glex.md) word · φ +1.00

- [glexe](glexe.md) word · φ +1.00

- [lex_utf8_etcbc](lex_utf8_etcbc.md) word · φ +0.99

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | glexo present when compared feature is present | glexo present when compared feature is absent |
| --- | --- | --- | --- |
| [glex](glex.md), [glexe](glexe.md) | +1.00 | 405,736 / 405,736 (100.0%) | 0 / 95,259 (0.0%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.99 | 405,649 / 406,914 (99.7%) | 87 / 94,081 (0.1%) |
| [glyph](glyph.md), [glyphe](glyphe.md), [glypho](glypho.md) | +0.98 | 405,715 / 408,125 (99.4%) | 21 / 92,870 (0.0%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -0.52 | 1 / 29,927 (0.0%) | 405,735 / 471,068 (86.1%) |
| [after](after.md) | -0.25 | 294,604 / 389,180 (75.7%) | 111,132 / 111,815 (99.4%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [lex-source-full rendering format](../../text.html#format-a48c95b2ff30) | `word#{lang:h}-{glexo}{punco}{after}` Uses: `lang:h`, [glexo](glexo.md), [punco](punco.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:01:59Z |
| description | representation (original source) of a lexeme leaving out non-letters |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
