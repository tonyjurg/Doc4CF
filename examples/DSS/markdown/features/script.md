# script.tf

[← Corpus index](../index.md)

script in which the word or sign is written if it is not Hebrew

Node · UTF-8 · str

## Generated description

The node feature script records the writing system of word and sign nodes when it is not Hebrew, using the values paleohebrew and greekcapital\. Populated nodes appear on sign and word types; absent assignments mean no value is recorded rather than a negative class\. The metadata defines the annotation as script used if the writing system is not Hebrew\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 796 (0.2%) |
| [sign](../../structure.html#type-sign) | 3,314 (0.2%) |

## Frequent values

2 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "paleohebrew" | 4,087 | 99.4% |
| "greekcapital" | 23 | 0.6% |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:12Z |
| description | script in which the word or sign is written if it is not Hebrew |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Martin Abegg's data files, personal communication |
| valueType | str |
| values | paleohebrew greekcapital |
| writtenBy | Text-Fabric |
