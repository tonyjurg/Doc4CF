# after.tf

[← Corpus index](../index.md)

space behind the word, if any

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 389,180 (77.7%) |
| [sign](../../structure.html#type-sign) | 409,369 (28.6%) |

## Frequent values

1 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| " " | 798,549 | 100.0% |

## Correlated features

No features meet the strong positive association threshold (φ ≥ +0.50).

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | after present when compared feature is present | after present when compared feature is absent |
| --- | --- | --- | --- |
| [gn](gn.md) | +0.39 | 191,038 / 194,777 (98.1%) | 198,142 / 306,218 (64.7%) |
| [nu](nu.md) | +0.39 | 190,931 / 194,670 (98.1%) | 198,249 / 306,325 (64.7%) |
| [st](st.md) | +0.24 | 103,851 / 107,481 (96.6%) | 285,329 / 393,514 (72.5%) |
| [cl](cl.md) | -0.40 | 202,213 / 312,839 (64.6%) | 186,967 / 188,156 (99.4%) |
| [glex](glex.md), [glexe](glexe.md), [glexo](glexo.md) | -0.25 | 294,604 / 405,736 (72.6%) | 94,576 / 95,259 (99.3%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [lex-orig-full rendering format](../../text.html#format-36909c131b7b) | `word#{lang:h}-{glex}{punc}{after}` Uses: `lang:h`, [glex](glex.md), [punc](punc.md), [after](after.md) |
| [lex-source-full rendering format](../../text.html#format-a48c95b2ff30) | `word#{lang:h}-{glexo}{punco}{after}` Uses: `lang:h`, [glexo](glexo.md), [punco](punco.md), [after](after.md) |
| [lex-trans-full rendering format](../../text.html#format-449a2f9052e2) | `word#{lang:h}-{glexe}{punce}{after}` Uses: `lang:h`, [glexe](glexe.md), [punce](punce.md), [after](after.md) |
| [morph-source-full rendering format](../../text.html#format-70e7f3d1fdff) | `word#{morpho}{punco}{after}` Uses: [morpho](morpho.md), [punco](punco.md), [after](after.md) |
| [text-orig-extra rendering format](../../text.html#format-3601169d6ef0) | `word#{full}{after}` Uses: [full](full.md), [after](after.md) |
| [text-orig-full rendering format](../../text.html#format-15716cf41c30) | `{glyph}{punc}{after}` Uses: [glyph](glyph.md), [punc](punc.md), [after](after.md) |
| [text-source-extra rendering format](../../text.html#format-9983e7731e06) | `word#{fullo}{after}` Uses: [fullo](fullo.md), [after](after.md) |
| [text-source-full rendering format](../../text.html#format-411816244e4a) | `{glypho}{punco}{after}` Uses: [glypho](glypho.md), [punco](punco.md), [after](after.md) |
| [text-trans-extra rendering format](../../text.html#format-d680068e58cf) | `word#{fulle}{after}` Uses: [fulle](fulle.md), [after](after.md) |
| [text-trans-full rendering format](../../text.html#format-f3356eee45fd) | `{glyphe}{punce}{after}` Uses: [glyphe](glyphe.md), [punce](punce.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:01:55Z |
| description | space behind the word, if any |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | (space) |
| writtenBy | Text-Fabric |
