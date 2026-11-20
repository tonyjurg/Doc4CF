# otext.tf

[← Corpus index](../index.md)

Configures Text-Fabric's Text API. Depending on the corpus, its settings can define section levels and their identifying features, text formats, and formatting templates. Text-Fabric uses this configuration to locate and render text for nodes. It is configuration rather than a node- or edge-valued feature, so its entries describe how the corpus is presented, not annotations attached to individual nodes.

Config · UTF-8 · configuration

## Generated description

*AI-assisted · OpenRouter · nvidia/nemotron-3.5-super-vl:free*

The otext configuration defines four original-text rendering formats for the AbB Old Babylonian Cuneiform corpus. text-orig-full concatenates atfpre, atf, atfpost, and after; text-orig-plain combines sym and afterr; text-orig-rich combines symr and afterr; text-orig-unicode combines symu and afteru. Reference sections are computed from the section features pnumber, face, and lnno, yielding document, face, and line references across the document > face > line hierarchy with sign as the slot type. The exact boundaries among the ATF, sym, reading, and grapheme layers, and the normalization rules between sym, symr, and symu, remain unspecified.

### Source metadata

| Field | Value |
| --- | --- |
| converters | Cale Johnson, Dirk Roorda |
| editor | Cale Johnson et al. |
| fmt:text-orig-full | {atfpre}{atf}{atfpost}{after} |
| fmt:text-orig-plain | {sym}{afterr} |
| fmt:text-orig-rich | {symr}{afterr} |
| fmt:text-orig-unicode | {symu}{afteru} |
| institute | CDL |
| name | AbB Old Babylonian Cuneiform |
| sectionFeatures | pnumber,face,lnno |
| sectionTypes | document,face,line |
| writtenBy | Text-Fabric |
| dateWritten | 2020-06-26T09:20:10Z |
