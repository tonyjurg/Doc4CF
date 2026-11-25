# biblical.tf

[← Corpus index](../index.md)

whether we are in biblical material or not

Node · UTF-8 · int

## Generated description

The biblical node feature classifies Dead Sea Scrolls nodes as biblical material \(value 1\) or biblical material that also has nonbiblical material \(value 2\)\. Values are observed on scroll, fragment, line, cluster, and word nodes\. For lines, value 2 may mark reconstruction where biblical material substitutes for nearly absent or identical nonbiblical material\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [scroll](../../structure.html#type-scroll) | 266 (26.6%) |
| [fragment](../../structure.html#type-fragment) | 2,305 (20.6%) |
| [line](../../structure.html#type-line) | 16,278 (30.8%) |
| [cluster](../../structure.html#type-cluster) | 30,636 (30.3%) |
| [word](../../structure.html#type-word) | 218,189 (43.6%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| 1 | 267,419 | 99.9% |
| 2 | 255 | 0.1% |

## Correlated features

- [book](book.md) word · φ +1.00

- [chapter](chapter.md) word · φ +1.00

- [verse](verse.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | biblical present when compared feature is present | biblical present when compared feature is absent |
| --- | --- | --- | --- |
| [book](book.md), [chapter](chapter.md), [verse](verse.md) | +1.00 | 218,189 / 218,189 (100.0%) | 0 / 282,806 (0.0%) |
| [gn_etcbc](gn_etcbc.md) | +0.83 | 197,922 / 219,259 (90.3%) | 20,267 / 281,736 (7.2%) |
| [glex](glex.md), [glexe](glexe.md), [glexo](glexo.md) | +0.23 | 199,317 / 405,736 (49.1%) | 18,872 / 95,259 (19.8%) |
| [lang](lang.md) | -0.24 | 3,438 / 49,411 (7.0%) | 214,751 / 451,584 (47.6%) |
| [st](st.md) | -0.14 | 32,485 / 107,481 (30.2%) | 185,704 / 393,514 (47.2%) |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.fragment.features` | biblical |
| `configuration.typeDisplay.line.features` | biblical |
| `configuration.typeDisplay.scroll.features` | biblical |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| applies | scroll fragment line cluster word |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:01:56Z |
| description | whether we are in biblical material or not |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| remark | for lines it means that the material is taken from the bib source while there is also material for this line in the nonbib source. But the nonbib material is either identical or virtually absent, in which case the bib material is a reconstruction and marked as such. |
| source | Martin Abegg's data files, personal communication |
| valueType | int |
| values | 1=biblical, 2=biblical but also with nonbiblical material |
| writtenBy | Text-Fabric |
