# otext.tf

[← Corpus index](../index.md)

Configures Text-Fabric's Text API. Depending on the corpus, its settings can define section levels and their identifying features, text formats, and formatting templates. Text-Fabric uses this configuration to locate and render text for nodes. It is configuration rather than a node- or edge-valued feature, so its entries describe how the corpus is presented, not annotations attached to individual nodes.

Config · UTF-8 · configuration

### Source metadata

| Field | Value |
| --- | --- |
| acronym | dss |
| convertedBy | Jarod Jacobs, Martijn Naaijer and Dirk Roorda |
| createdBy | Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook |
| createdDate | 2015 |
| dateWritten | 2020-12-29T15:02:19Z |
| description | Dead Sea Scrolls: biblical and non-biblical scrolls |
| fmt:lex-default | word#{lang:h}-{lex}-{lexe}-{lexo} |
| fmt:lex-orig-full | word#{lang:h}-{glex}{punc}{after} |
| fmt:lex-source-full | word#{lang:h}-{glexo}{punco}{after} |
| fmt:lex-trans-full | word#{lang:h}-{glexe}{punce}{after} |
| fmt:morph-source-full | word#{morpho}{punco}{after} |
| fmt:text-orig-extra | word#{full}{after} |
| fmt:text-orig-full | {glyph}{punc}{after} |
| fmt:text-source-extra | word#{fullo}{after} |
| fmt:text-source-full | {glypho}{punco}{after} |
| fmt:text-trans-extra | word#{fulle}{after} |
| fmt:text-trans-full | {glyphe}{punce}{after} |
| license | Creative Commons Attribution-NonCommercial 4.0 International License |
| licenseUrl | http://creativecommons.org/licenses/by-nc/4.0/ |
| sectionFeatures | scroll,fragment,line |
| sectionTypes | scroll,fragment,line |
| source | Martin Abegg's data files, personal communication |
| writtenBy | Text-Fabric |
