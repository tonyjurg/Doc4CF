# lnno.tf

[← Corpus index](../index.md)

ATF line number, may be $ or #, with prime; column number prepended

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The `lnno` feature records the ATF line number on line nodes in the AbB Old Babylonian Cuneiform corpus. Values may include a prime and may have a column number prepended. The feature is attested on all 27,375 line nodes, has 85 distinct values, and frequent values include `1` (2,437), `2` (2,319), and `3` (2,169). As a section feature, `lnno` combines with `pnumber` and `face` to compute reference sections for `otext`. It overlaps conceptually with `ln`, which records an ATF line number without prime, but the inventory does not specify disambiguation or co-occurrence rules between them, nor how `lnno` interacts with `col` and `primecol`.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [line](../../structure.html#type-line) | 27,375 (100.0%) |

## Frequent values

85 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "1" | 2,437 | 8.9% |
| "2" | 2,319 | 8.5% |
| "3" | 2,169 | 7.9% |
| "4" | 2,062 | 7.5% |
| "5" | 1,981 | 7.2% |
| "6" | 1,891 | 6.9% |
| "7" | 1,790 | 6.5% |
| "8" | 1,667 | 6.1% |
| "9" | 1,533 | 5.6% |
| "10" | 1,366 | 5.0% |
| "11" | 1,174 | 4.3% |
| "12" | 956 | 3.5% |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | ATF line number, may be $ or #, with prime; column number prepended |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:08Z |
