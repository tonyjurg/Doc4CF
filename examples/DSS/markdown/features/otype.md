# otype.tf

[← Corpus index](../index.md)

Maps every Text-Fabric node to its node type. The type identifies what kind of structural unit the node represents, such as a slot or a larger unit defined by the corpus. This core node feature lets tools select nodes by type and interpret where other features apply. Type labels describe the corpus data model; their names alone do not establish the linguistic or semantic role of a unit.

Node · UTF-8 · str

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [scroll](../../structure.html#type-scroll) | 1,001 (100.0%) |
| [lex](../../structure.html#type-lex) | 10,450 (100.0%) |
| [fragment](../../structure.html#type-fragment) | 11,182 (100.0%) |
| [line](../../structure.html#type-line) | 52,895 (100.0%) |
| [clause](../../structure.html#type-clause) | 125 (100.0%) |
| [cluster](../../structure.html#type-cluster) | 101,099 (100.0%) |
| [phrase](../../structure.html#type-phrase) | 315 (100.0%) |
| [word](../../structure.html#type-word) | 500,995 (100.0%) |
| [sign](../../structure.html#type-sign) | 1,430,241 (100.0%) |

## Frequent values

9 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "sign" | 1,430,241 | 67.8% |
| "word" | 500,995 | 23.8% |
| "cluster" | 101,099 | 4.8% |
| "line" | 52,895 | 2.5% |
| "fragment" | 11,182 | 0.5% |
| "lex" | 10,450 | 0.5% |
| "scroll" | 1,001 | 0.0% |
| "phrase" | 315 | 0.0% |
| "clause" | 125 | 0.0% |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:10Z |
| description | Dead Sea Scrolls: biblical and non-biblical scrolls |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| writtenBy | Text-Fabric |
