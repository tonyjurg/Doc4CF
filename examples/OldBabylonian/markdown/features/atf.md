# atf.tf

[← Corpus index](../index.md)

full atf of a sign (without cluster chars) or word (including cluster chars)

Node · UTF-8 · str

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The atf feature records the full ATF transcription of a sign or word node. For sign nodes it excludes cluster characters, while for word nodes it includes cluster characters. It is sourced from 203,219 sign nodes and 76,503 word nodes and has 23,577 distinct values. Frequent values include x, a, ma, na, sza, i, u3, szu, d, li, am, and a-na. The feature belongs to the Sign and Word Essential Forms family alongside sym, symr, symu, after, and afterr, and is used by the text-orig-full output format. The precise boundary between atf and sym, especially for word nodes, remains unspecified in the inventory.

## Applies to

| Node type | Populated nodes (% of node type) |
| --- | --- |
| [word](../../structure.html#type-word) | 76,503 (100.0%) |
| [sign](../../structure.html#type-sign) | 203,219 (100.0%) |

## Frequent values

23,577 distinct values. Whitespace is shown in quotes.

| Value | Occurrences | % of populated values |
| --- | --- | --- |
| "x" | 13,090 | 4.7% |
| "a" | 11,653 | 4.2% |
| "ma" | 10,842 | 3.9% |
| "na" | 8,036 | 2.9% |
| "sza" | 6,534 | 2.3% |
| "i" | 4,958 | 1.8% |
| "u3" | 4,950 | 1.8% |
| "szu" | 4,225 | 1.5% |
| "d" | 4,070 | 1.5% |
| "li" | 3,603 | 1.3% |
| "am" | 3,568 | 1.3% |
| "a-na" | 3,540 | 1.3% |

## How the app uses this feature

These settings describe configured app presentation and documented guidance; they are separate from the measured corpus data above.

| App setting or format | Configured value |
| --- | --- |
| [text-orig-full rendering format](../../text.html#format-15716cf41c30) | `{atfpre}{atf}{atfpost}{after}` Uses: [atfpre](atfpre.md), [atf](atf.md), [atfpost](atfpost.md), [after](after.md) |

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| description | full atf of a sign (without cluster chars) or word (including cluster chars) |
| editor | Cale Johnson et al. |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| valueType | str |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:07Z |
