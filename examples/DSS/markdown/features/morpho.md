# morpho.tf

[← Corpus index](../index.md)

morphological tag (by Abegg)

Node · UTF-8 · str

## Generated description

The morpho feature is a node\-level morphological tag observed on word nodes in the Dead Sea Scrolls corpus\. Populated assignments appear on word nodes, while nodes without a value have no recorded tag rather than a negative class\. Metadata attributes the tag to Martin Abegg's data files; values such as Pc and np may encode parts of speech and nominal forms\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 470,845 (94.0%) |

## Frequent values

2,008 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "0" | 80,250 | 17.0% |
| "Pc" | 51,775 | 11.0% |
| "Pp" | 50,293 | 10.7% |
| "Pa" | 22,259 | 4.7% |
| "np" | 19,493 | 4.1% |
| "ncmsc" | 17,493 | 3.7% |
| "ncmsa" | 15,023 | 3.2% |
| "ncms" | 12,647 | 2.7% |
| "Pd" | 6,621 | 1.4% |
| "Pr" | 6,325 | 1.3% |
| "Po" | 6,085 | 1.3% |
| "ncmpc" | 5,884 | 1.2% |

## Correlated features

- [sp](sp.md) word · φ +1.00

- [lex](lex.md) word · φ +1.00

- [lexe](lexe.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | morpho present when compared feature is present | morpho present when compared feature is absent |
| --- | --- | --- | --- |
| [sp](sp.md) | +1.00 | 470,845 / 470,845 (100.0%) | 0 / 30,150 (0.0%) |
| [lex](lex.md), [lexe](lexe.md), [lexo](lexo.md) | +1.00 | 470,841 / 470,845 (100.0%) | 4 / 30,150 (0.0%) |
| [lex_utf8_etcbc](lex_utf8_etcbc.md) | +0.53 | 406,910 / 406,914 (100.0%) | 63,935 / 94,081 (68.0%) |
| [punc](punc.md), [punce](punce.md), [punco](punco.md) | -1.00 | 2 / 29,927 (0.0%) | 470,843 / 471,068 (100.0%) |
| [after](after.md) | -0.13 | 359,249 / 389,180 (92.3%) | 111,596 / 111,815 (99.8%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [morph-source-full rendering format](../../text.html#format-70e7f3d1fdff) | `word#{morpho}{punco}{after}` Uses: [morpho](morpho.md), [punco](punco.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:08Z |
| description | morphological tag (by Abegg) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
