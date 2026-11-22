# cls.tf

[← Corpus index](../index.md)

**Node feature** · UTF\-8 · str

## Description

this is XML attribute cls

## Generated description

The node feature cls records the XML attribute cls as a string on clause, phrase, sentence, subphrase, wg, and word nodes; sources list populated nodes only, so unlisted nodes have no recorded value\. It appears in the clause node label template alongside typ, function, rela, role, and junction\. Frequent values include np and cl, suggesting it may encode syntactic category or clause/phrase type, though the inventory does not define its value set\.

*AI-assisted · OpenRouter · nvidia/nemotron\-3\.5\-super\-vl:free*

## Applies to

| Node type | Populated nodes |
| --- | ---: |
| sentence | 1,476 (18.4%) |
| clause | 28,676 (67.5%) |
| wg | 72,788 (68.1%) |
| phrase | 66,851 (96.9%) |
| subphrase | 113,564 (97.8%) |
| word | 137,779 (100.0%) |

## Frequent values

| Value | Occurrences | % of populated values |
| --- | ---: | ---: |
| `"np"` | 61,822 | 14.7% |
| `"cl"` | 60,304 | 14.3% |
| `"noun"` | 56,910 | 13.5% |
| `"verb"` | 56,714 | 13.5% |
| `"det"` | 39,572 | 9.4% |
| `"conj"` | 36,456 | 8.7% |
| `"pron"` | 32,354 | 7.7% |
| `"pp"` | 22,338 | 5.3% |
| `"prep"` | 21,828 | 5.2% |
| `"adj"` | 16,904 | 4.0% |
| `"adv"` | 12,308 | 2.9% |
| `"ptcl"` | 1,546 | 0.4% |

<details>
<summary>Source metadata</summary>

| Field | Value |
| --- | --- |
| author | Evangelists and apostles |
| converterSourceLocation | https://github\.com/saulocantanhede/tfgreek2/tree/main/programs |
| converterVersion | 1\.0\.0 \(July 9, 2024\) |
| converters | Saulo de Oliveira Cantanhêde, Tony Jurg, Dirk Roorda |
| dataSource | MACULA Greek Linguistic Datasets, available at https://github\.com/Clear\-Bible/macula\-greek/tree/main/Nestle1904/lowfat |
| dataSourceFormat | XML lowfat tree data |
| dataSourceLocation | https://github\.com/saulocantanhede/tfgreek2/tree/main/xml/2022\-11\-01/gnt |
| description | this is XML attribute cls |
| editors | Eberhart Nestle \(1904\) |
| institute | ETCBC \(Eep Talstra Centre for Bible and Computer\) at Vrije Universiteit Amsterdam, CBLC \(Center of Biblical Languages and Computing\) at Andrews University |
| title | Greek New Testament \(Nestle 1904\) |
| valueType | str |
| version | 1\.0\.0 |
| xmlSourceDate | February 9, 2023 |
| xmlVersion | 2022\-11\-01 |
| writtenBy | Text\-Fabric |
| dateWritten | 2024\-07\-28T01:57:11Z |

</details>
