# cl.tf

[← Corpus index](../index.md)

class (morphology tag)

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 312,839 (62.4%) |

## Frequent values

18 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "cmn" | 113,674 | 36.3% |
| "prep" | 60,943 | 19.5% |
| "conj" | 51,778 | 16.6% |
| "art" | 22,260 | 7.1% |
| "prp" | 19,597 | 6.3% |
| "objm" | 7,222 | 2.3% |
| "advb" | 7,163 | 2.3% |
| "rela" | 6,325 | 2.0% |
| "card" | 5,617 | 1.8% |
| "nega" | 5,470 | 1.7% |
| "indp" | 4,842 | 1.5% |
| "artp" | 3,812 | 1.2% |

## Correlated features

- [glex](glex.md) word · φ +0.62

- [glexe](glexe.md) word · φ +0.62

- [glexo](glexo.md) word · φ +0.62

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | cl present when compared feature is present | cl present when compared feature is absent |
| --- | --- | --- | --- |
| [glex](glex.md), [glexe](glexe.md), [glexo](glexo.md) | +0.62 | 312,829 / 405,736 (77.1%) | 10 / 95,259 (0.0%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.62 | 312,814 / 406,914 (76.9%) | 25 / 94,081 (0.0%) |
| [glyph](glyph.md), [glyphe](glyphe.md), [glypho](glypho.md) | +0.61 | 312,825 / 408,125 (76.6%) | 14 / 92,870 (0.0%) |
| [vs](vs.md) | -0.50 | 0 / 66,332 (0.0%) | 312,839 / 434,663 (72.0%) |
| [vt](vt.md) | -0.50 | 0 / 66,317 (0.0%) | 312,839 / 434,678 (72.0%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.word.features` | lang lex cl ps gn nu st vs vt md |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:01:56Z |
| description | class (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | advb, art, artp, card, cmn, conj, gent, indp, intj, intr, mult, nega, objm, ord, prep, prp, rela, unknown |
| writtenBy | Text-Fabric |
