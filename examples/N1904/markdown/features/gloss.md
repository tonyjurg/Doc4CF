# gloss.tf

[← Corpus index](../index.md)

English gloss (BGVB)

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The gloss feature is a node-level string annotation on word nodes, with 137,779 populated word nodes and 5,202 distinct values. Metadata identifies it as an English gloss (BGVB), sourced from Nestle1904.csv and MACULA Greek Linguistic Datasets, with editors including Oliver Glanz and Bible Online Learner. Frequent values include “the” (19,783) and “and, also, likewise” (8,978), illustrating observed lexical gloss distribution.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 137,779 (100.0%) |

## Frequent values

5,202 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "the" | 19,783 | 14.4% |
| "and, also, likewise" | 8,978 | 6.5% |
| "he, she, it, himself, herself, itself; even, very; same" | 5,550 | 4.0% |
| "you" | 2,892 | 2.1% |
| "but, and" | 2,787 | 2.0% |
| "(with dat.) in" | 2,743 | 2.0% |
| "I" | 2,567 | 1.9% |
| "am, exist" | 2,457 | 1.8% |
| "say, tell" | 2,255 | 1.6% |
| "no, not" | 1,622 | 1.2% |
| "who, which, what, that" | 1,407 | 1.0% |
| "this, he, she, it" | 1,388 | 1.0% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| `configuration.typeDisplay.word.featuresBare[0]` | gloss |
| Feature documentation | [Open source documentation](https://github.com/CenterBLC/N1904/blob/main/docs/features/gloss.md) Source: `docs/features/gloss.md`; configured at `configuration.docs.featureBase` |

### Source metadata

| Field | Value |
| --- | --- |
| author | Evangelists and apostles |
| converterSourceLocation | https://github.com/saulocantanhede/tfgreek2/tree/main/programs |
| converterVersion | 1.0.0 (July 9, 2024) |
| converters | Saulo de Oliveira Cantanhêde, Tony Jurg, Dirk Roorda, Oliver Glanz |
| dataSource | MACULA Greek Linguistic Datasets, available at https://github.com/Clear-Bible/macula-greek/tree/main/Nestle1904/lowfat |
| dataSourceFormat | XML lowfat tree data |
| dataSourceLocation | https://github.com/saulocantanhede/tfgreek2/tree/main/xml/2022-11-01/gnt |
| description | English gloss (BGVB) |
| editors | Ulrik Sandborg Petersen, Eliran Wong, Oliver Glanz, Bible Online Learner |
| institute | ETCBC (Eep Talstra Centre for Bible and Computer) at Vrije Universiteit Amsterdam, CBLC (Center of Biblical Languages and Computing) at Andrews University |
| source | https://github.com/biblicalhumanities/Nestle1904/blob/master/morph/Nestle1904.csv |
| title | Greek New Testament (Nestle 1904) |
| valueType | str |
| version | 1.0.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022-11-01 |
| writtenBy | Text-Fabric |
| dateWritten | 2024-07-28T01:57:09Z |
