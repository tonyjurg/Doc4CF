# gn.tf

[← Corpus index](../index.md)

gender (morphology tag)

Node · UTF-8 · str

## Generated description

The gn feature is a node\-level morphological annotation on word nodes in the Dead Sea Scrolls corpus, recording gender as a morphology tag\. Populated assignments indicate recorded values; missing assignments mean no value is recorded rather than a negative class\. Concrete values include m and f, with additional values documented in the feature metadata sourced from Martin Abegg's data files\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 194,777 (38.9%) |

## Frequent values

5 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "m" | 137,217 | 70.4% |
| "f" | 36,093 | 18.5% |
| "c" | 10,492 | 5.4% |
| "b" | 9,951 | 5.1% |
| "unknown" | 1,024 | 0.5% |

## Correlated features

- [nu](nu.md) word · φ +1.00

- [st](st.md) word · φ +0.66

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | gn present when compared feature is present | gn present when compared feature is absent |
| --- | --- | --- | --- |
| [nu](nu.md) | +1.00 | 194,664 / 194,670 (100.0%) | 113 / 306,325 (0.0%) |
| [st](st.md) | +0.66 | 107,478 / 107,481 (100.0%) | 87,299 / 393,514 (22.2%) |
| [ps](ps.md) | +0.41 | 49,092 / 49,100 (100.0%) | 145,685 / 451,895 (32.2%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -0.20 | 0 / 29,927 (0.0%) | 194,777 / 471,068 (41.3%) |

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
| dateWritten | 2020-12-29T15:02:06Z |
| description | gender (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | b, c, f, m, unknown |
| writtenBy | Text-Fabric |
