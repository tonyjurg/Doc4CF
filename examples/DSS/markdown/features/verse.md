# verse.tf

[← Corpus index](../index.md)

label of the verse in which the word occurs

Node · UTF-8 · str

## Generated description

The verse feature is a node\-level annotation recording the verse label in which each word occurs, with string values observed on 218,189 word nodes\. It does not cover every word node; missing values mean no verse label is recorded rather than a negative assignment\. Distinct verse labels number 152, and examples include "1" and "2"\. The feature may support locating words within biblical verse divisions, though coverage of non\-biblical material is unclear\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 218,189 (43.6%) |

## Frequent values

152 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "1" | 12,290 | 5.6% |
| "2" | 11,890 | 5.4% |
| "3" | 10,676 | 4.9% |
| "5" | 10,319 | 4.7% |
| "6" | 9,681 | 4.4% |
| "4" | 9,665 | 4.4% |
| "7" | 9,266 | 4.2% |
| "8" | 9,250 | 4.2% |
| "9" | 8,864 | 4.1% |
| "11" | 8,449 | 3.9% |
| "10" | 8,307 | 3.8% |
| "12" | 8,093 | 3.7% |

## Correlated features

- [biblical](biblical.md) word · φ +1.00

- [book](book.md) word · φ +1.00

- [chapter](chapter.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | verse present when compared feature is present | verse present when compared feature is absent |
| --- | --- | --- | --- |
| [biblical](biblical.md), [book](book.md), [chapter](chapter.md) | +1.00 | 218,189 / 218,189 (100.0%) | 0 / 282,806 (0.0%) |
| [gn_etcbc](gn_etcbc.md) | +0.83 | 197,922 / 219,259 (90.3%) | 20,267 / 281,736 (7.2%) |
| [glex](glex.md), [glexe](glexe.md), [glexo](glexo.md) | +0.23 | 199,317 / 405,736 (49.1%) | 18,872 / 95,259 (19.8%) |
| [lang](lang.md) | -0.24 | 3,438 / 49,411 (7.0%) | 214,751 / 451,584 (47.6%) |
| [st](st.md) | -0.14 | 32,485 / 107,481 (30.2%) | 185,704 / 393,514 (47.2%) |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:15Z |
| description | label of the verse in which the word occurs |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
