# nu.tf

[← Corpus index](../index.md)

number (morphology tag)

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 194,670 (38.9%) |

## Frequent values

4 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "s" | 139,444 | 71.6% |
| "p" | 51,752 | 26.6% |
| "d" | 2,392 | 1.2% |
| "unknown" | 1,082 | 0.6% |

## Correlated features

- [gn](gn.md) word · φ +1.00

- [st](st.md) word · φ +0.66

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | nu present when compared feature is present | nu present when compared feature is absent |
| --- | --- | --- | --- |
| [gn](gn.md) | +1.00 | 194,664 / 194,777 (99.9%) | 6 / 306,218 (0.0%) |
| [st](st.md) | +0.66 | 107,479 / 107,481 (100.0%) | 87,191 / 393,514 (22.2%) |
| [ps](ps.md) | +0.41 | 48,992 / 49,100 (99.8%) | 145,678 / 451,895 (32.2%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -0.20 | 0 / 29,927 (0.0%) | 194,670 / 471,068 (41.3%) |

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
| dateWritten | 2020-12-29T15:02:09Z |
| description | number (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | d, p, s, unknown |
| writtenBy | Text-Fabric |
