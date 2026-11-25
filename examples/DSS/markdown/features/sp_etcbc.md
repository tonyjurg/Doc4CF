# sp_etcbc.tf

[← Corpus index](../index.md)

The part of speech (morphology tag)

Node · UTF-8 · str

## Generated description

The sp\_etcbc feature records part\-of\-speech morphology tags as string values on word nodes in the Dead Sea Scrolls Text\-Fabric corpus\. Populated nodes carry values such as verb or subs; missing assignments mean no tag is recorded, not a negative class\. The source is automatic morphological parsing corrected by Thijs Amersfoort under the dss\-additions family\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 500,995 (100.0%) |

## Frequent values

15 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "" | 281,093 | 56.1% |
| "subs" | 66,145 | 13.2% |
| "verb" | 41,571 | 8.3% |
| "prep" | 39,130 | 7.8% |
| "conj" | 31,764 | 6.3% |
| "nmpr" | 13,196 | 2.6% |
| "art" | 10,970 | 2.2% |
| "adjv" | 4,809 | 1.0% |
| "nega" | 3,791 | 0.8% |
| "prps" | 2,809 | 0.6% |
| "advb" | 2,310 | 0.5% |
| "prde" | 1,380 | 0.3% |

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss-additions |
| convertedBy | Martijn Naaijer, Dirk Roorda and Thijs Amersfoort |
| createdBy | Martin G. Abegg, Martijn Naaijer, ETCBC |
| createdDate | 2026 |
| dateWritten | 2026-11-04T12:00:13+00:00Z |
| description | The part of speech (morphology tag) |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| source | Automatic generated morphological parsing corrected by Thijs Amersfoort |
| valueType | str |
| writtenBy | Text-Fabric |
