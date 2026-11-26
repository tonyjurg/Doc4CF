# book.tf

[← Corpus index](../index.md)

acronym of the book in which the word occurs

Node · UTF-8 · str

## Generated description

The node feature book records, as a string acronym, the book in which each word occurs\. Values are observed on word nodes only; unassigned words have no recorded book rather than a negative class\. Distinct acronyms include Is and Deut\. Source metadata credits Martin Abegg's data files via personal communication, and the value type is string\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 218,189 (43.6%) |

## Frequent values

123 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "Is" | 47,932 | 22.0% |
| "Deut" | 30,043 | 13.8% |
| "Ex" | 27,822 | 12.8% |
| "Ps" | 16,941 | 7.8% |
| "Lev" | 11,820 | 5.4% |
| "Num" | 10,651 | 4.9% |
| "2Sam" | 9,153 | 4.2% |
| "Gen" | 7,902 | 3.6% |
| "1Sam" | 7,435 | 3.4% |
| "Jer" | 6,577 | 3.0% |
| "Dan" | 5,236 | 2.4% |
| "Amos" | 3,332 | 1.5% |

## Correlated features

- [biblical](biblical.md) word · φ +1.00

- [chapter](chapter.md) word · φ +1.00

- [verse](verse.md) word · φ +1.00

### Presence/absence associations

Each comparison is calculated separately across all nodes of the listed type. Present means the feature has an assigned value; absent means no assignment. φ ranges from −1 (opposite presence patterns) to +1 (matching patterns). Only non-constant pairs with at least 10 present and 10 absent nodes per feature, and |φ| ≥ 0.10, are shown. Identical presence patterns are grouped. These are descriptive associations, not causal claims. [Read the scoring method](https://tonyjurg.github.io/Doc4CF/api/architecture.html#measured-feature-associations).

### word nodes

| Compared feature(s) | φ | book present when compared feature is present | book present when compared feature is absent |
| --- | --- | --- | --- |
| [biblical](biblical.md), [chapter](chapter.md), [verse](verse.md) | +1.00 | 218,189 / 218,189 (100.0%) | 0 / 282,806 (0.0%) |
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
| dateWritten | 2020-12-29T15:01:56Z |
| description | acronym of the book in which the word occurs |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
