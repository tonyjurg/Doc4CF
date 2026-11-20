# sp.tf

[← Corpus index](../index.md)

part of speech (morphology tag)

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 470,845 (94.0%) |

## Frequent values

8 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "ptcl" | 154,464 | 32.8% |
| "subs" | 108,562 | 23.1% |
| "unknown" | 80,256 | 17.0% |
| "verb" | 58,873 | 12.5% |
| "suff" | 45,747 | 9.7% |
| "adjv" | 10,633 | 2.3% |
| "numr" | 6,526 | 1.4% |
| "pron" | 5,784 | 1.2% |

## Correlated features

- [morpho](morpho.md) word · φ +1.00

- [lex](lex.md) word · φ +1.00

- [lexe](lexe.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | sp present when compared feature is present | sp present when compared feature is absent |
| --- | --- | --- | --- |
| [morpho](morpho.md) | +1.00 | 470,845 / 470,845 (100.0%) | 0 / 30,150 (0.0%) |
| [lex](lex.md), [lexe](lexe.md), [lexo](lexo.md) | +1.00 | 470,841 / 470,845 (100.0%) | 4 / 30,150 (0.0%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.53 | 406,910 / 406,914 (100.0%) | 63,935 / 94,081 (68.0%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -1.00 | 2 / 29,927 (0.0%) | 470,843 / 471,068 (100.0%) |
| [after](after.md) | -0.13 | 359,249 / 389,180 (92.3%) | 111,596 / 111,815 (99.8%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.word.featuresBare` | sp |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:12Z |
| description | part of speech (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | adjv, numr, pron, ptcl, subs, suff, unknown, verb |
| writtenBy | Text-Fabric |
