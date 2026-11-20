# lex_utf8_etcbc.tf

[← Corpus index](../index.md)

The pointed representation of the lexeme of a word

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 406,914 (81.2%) |

## Frequent values

8,943 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "וְ" | 45,199 | 11.1% |
| "לְ" | 21,603 | 5.3% |
| "בְּ" | 19,751 | 4.9% |
| "הַ" | 18,766 | 4.6% |
| "אֵת" | 7,676 | 1.9% |
| "כֹּל" | 7,448 | 1.8% |
| "מִן" | 7,207 | 1.8% |
| "עַל" | 5,443 | 1.3% |
| "לֹא" | 5,109 | 1.3% |
| "יהוה" | 4,308 | 1.1% |
| "אֲשֶׁר" | 4,252 | 1.0% |
| "כִּי" | 4,135 | 1.0% |

## Correlated features

- [glex](glex.md) word · φ +0.99

- [glexe](glexe.md) word · φ +0.99

- [glexo](glexo.md) word · φ +0.99

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | lex_utf8_etcbc present when compared feature is present | lex_utf8_etcbc present when compared feature is absent |
| --- | --- | --- | --- |
| [glex](glex.md), [glexe](glexe.md), [glexo](glexo.md) | +0.99 | 405,649 / 405,736 (100.0%) | 1,265 / 95,259 (1.3%) |
| [glyph](glyph.md), [glyphe](glyphe.md), [glypho](glypho.md) | +0.98 | 405,813 / 408,125 (99.4%) | 1,101 / 92,870 (1.2%) |
| [g_prs_etcbc](g_prs_etcbc.md) | +0.73 | 355,014 / 357,210 (99.4%) | 51,900 / 143,785 (36.1%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -0.52 | 1 / 29,927 (0.0%) | 406,913 / 471,068 (86.4%) |
| [after](after.md) | -0.25 | 295,734 / 389,180 (76.0%) | 111,180 / 111,815 (99.4%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:11+00:00Z |
| description | The pointed representation of the lexeme of a word |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
