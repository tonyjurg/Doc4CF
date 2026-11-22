# Greek New Testament \(Nestle 1904\)

Generated with [Doc4CF](https://github.com/tonyjurg/Doc4CF).

Browse the feature descriptions and measured profiles below.

## Features

| Feature | Kind | Description | Applies to | Two most common values |
| --- | --- | --- | --- | --- |
| [after](features/after.md) | node | material after the end of the word | phrase, subphrase, word | `" "` (238,522); `", "` (18,878) |
| [appositioncontainer](features/appositioncontainer.md) | node | 1 if it is an apposition container | clause, wg, phrase, subphrase | `1` (3,816) |
| [articular](features/articular.md) | node | 1 if the sentence, group, clause, phrase or wg has an article | sentence, group, clause, wg, phrase, subphrase | `1` (57,544) |
| [before](features/before.md) | node | this is XML attribute before | phrase, subphrase, word | `"—"` (32); `"("` (20) |
| [book](features/book.md) | node | book name \(full name\) | book, chapter, verse, sentence, group, clause, wg, phrase, subphrase, word | `"Luke"` (70,494); `"Acts"` (66,507) |
| [bookshort](features/bookshort.md) | node | book name \(abbreviated\) from ref attribute in xml | book, sentence, group, clause, wg, phrase, subphrase, word | `"LUK"` (69,321); `"ACT"` (65,477) |
| [case](features/case.md) | node | grammatical case | phrase, subphrase, word | `"nominative"` (48,394); `"accusative"` (46,062) |
| [chapter](features/chapter.md) | node | chapter number, from ref attribute in xml | chapter, verse, sentence, group, clause, wg, phrase, subphrase, word | `1` (42,442); `2` (35,630) |
| [clausetype](features/clausetype.md) | node | clause type | sentence, clause, wg | `"nominalized"` (10,592) |
| [cls](features/cls.md) | node | this is XML attribute cls | sentence, clause, wg, phrase, subphrase, word | `"np"` (61,822); `"cl"` (60,304) |
| [cltype](features/cltype.md) | node | clause type | sentence, clause, wg | `"VerbElided"` (2,100); `"Verbless"` (1,922) |
| [criticalsign](features/criticalsign.md) | node | this is XML attribute criticalsign | phrase, subphrase, word | `"—"` (50); `"("` (22) |
| [crule](features/crule.md) | node | clause rule \(from xml attribute Rule\) | sentence, clause, wg | `"ClCl"` (8,616); `"ClCl2"` (2,500) |
| [degree](features/degree.md) | node | grammatical degree | phrase, subphrase, word | `"comparative"` (626); `"superlative"` (400) |
| [discontinuous](features/discontinuous.md) | node | 1 if the word is out of sequence in the xml | phrase, subphrase, word | `1` (12,068) |
| [domain](features/domain.md) | node | domain | phrase, subphrase, word | `"092004"` (52,258); `"089017"` (8,740) |
| [frame](features/frame.md) | edge | frame | word | `"A0"` (25,654); `"A1"` (15,570) |
| [framespec](features/framespec.md) | node | this is XML attribute framespec | phrase, subphrase, word | `"A0:n00000000000"` (1,792); `"A1:n00000000000"` (338) |
| [function](features/function.md) | node | this is XML attribute function | sentence, clause, wg, phrase, word | `"Pred"` (49,714); `"Cmpl"` (26,024) |
| [gender](features/gender.md) | node | grammatical gender | phrase, subphrase, word | `"masculine"` (82,972); `"feminine"` (37,472) |
| [gloss](features/gloss.md) | node | English gloss \(BGVB\) | word | `"the"` (19,783); `"and, also, likewise"` (8,978) |
| [id](features/id.md) | node | xml id | phrase, subphrase, word | `"n40001001001"` (2); `"n40001001002"` (2) |
| [junction](features/junction.md) | node | type of junction | clause, wg, phrase, subphrase | `"coordinate"` (18,734); `"subordinate"` (17,108) |
| [lang](features/lang.md) | node | language the text is in | book | `"el"` (27) |
| [lemma](features/lemma.md) | node | lexical lemma | phrase, subphrase, word | `"ὁ"` (39,566); `"καί"` (17,956) |
| [lemmatranslit](features/lemmatranslit.md) | node | transliteration of the word lemma | phrase, subphrase, word | `"o"` (39,600); `"kai"` (17,956) |
| [ln](features/ln.md) | node | Louw–Nida semantic-domain codes (editorial clarification) | phrase, subphrase, word | `"92.24"` (39,476); `"92.11"` (9,436) |
| [mood](features/mood.md) | node | verbal mood | phrase, subphrase, word | `"indicative"` (31,234); `"participle"` (13,306) |
| [morph](features/morph.md) | node | morphological code | phrase, subphrase, word | `"CONJ"` (32,632); `"PREP"` (21,136) |
| [nodeid](features/nodeid.md) | node | node id \(as in the XML source data\) | sentence, clause, wg | `"400010200010490"` (2); `"400010200120390"` (2) |
| [normalized](features/normalized.md) | node | lemma normalized | phrase, subphrase, word | `"καί"` (17,152); `"ὁ"` (5,538) |
| [note](features/note.md) | node | annotation of linguistic nature | phrase, word | `"discontinuous discourse"` (2) |
| [num](features/num.md) | node | generated number \(not in xml\): book: \(Matthew=1, Mark=2, \.\.\., Revelation=27\); sentence: numbered per chapter; word: numbered per verse\. | book, sentence, group, clause, wg, phrase, subphrase, word | `17` (200); `27` (198) |
| [number](features/number.md) | node | grammatical number | phrase, subphrase, word | `"singular"` (139,692); `"plural"` (58,182) |
| [oslots](features/oslots.md) | edge | Maps each non\-slot node to the slot nodes that make up its textual span\. This core edge feature links structural units to the slots they cover and supports retrieving a node's text and relating it to the corpus's smallest units\. Its edges express slot membership; they do not by themselves identify semantic, syntactic, or parent\-child relationships between non\-slot units\. | book, chapter, verse, sentence, group, clause, wg, phrase, subphrase | — |
| [otext](features/otext.md) | config | Configures Text\-Fabric's Text API\. Depending on the corpus, its settings can define section levels and their identifying features, text formats, and formatting templates\. Text\-Fabric uses this configuration to locate and render text for nodes\. It is configuration rather than a node\- or edge\-valued feature, so its entries describe how the corpus is presented, not annotations attached to individual nodes\. |  | — |
| [otype](features/otype.md) | node | Maps every Text\-Fabric node to its node type\. The type identifies what kind of structural unit the node represents, such as a slot or a larger unit defined by the corpus\. This core node feature lets tools select nodes by type and interpret where other features apply\. Type labels describe the corpus data model; their names alone do not establish the linguistic or semantic role of a unit\. | book, chapter, verse, sentence, group, clause, wg, phrase, subphrase, word | `"word"` (137,779); `"subphrase"` (116,178) |
| [parent](features/parent.md) | edge | parent relationship between words | sentence, group, clause, wg, phrase, word | — |
| [person](features/person.md) | node | grammatical person | phrase, subphrase, word | `"p3"` (25,494); `"p2"` (7,458) |
| [punctuation](features/punctuation.md) | node | punctuation found after a word | phrase, subphrase, word | `","` (18,924); `"."` (11,434) |
| [ref](features/ref.md) | node | biblical reference with word counting | phrase, subphrase, word | `"MAT 1:1!1"` (2); `"MAT 1:1!2"` (2) |
| [referent](features/referent.md) | node | number of referent | phrase, subphrase, word | `"n40005001015"` (224); `"n43014023002"` (158) |
| [rela](features/rela.md) | node | this is XML attribute rela | wg, subphrase, word | `"Appo"` (1,958) |
| [role](features/role.md) | node | role | group, clause, wg, phrase, subphrase, word | `"v"` (50,344); `"adv"` (43,154) |
| [rule](features/rule.md) | node | syntactical rule | sentence, group, clause, wg, phrase, subphrase | `"DetNP"` (31,392); `"PrepNp"` (22,088) |
| [sp](features/sp.md) | node | part\-of\-speach | phrase, subphrase, word | `"subs"` (56,910); `"verb"` (56,714) |
| [strong](features/strong.md) | node | strong number | phrase, subphrase, word | `3588` (39,566); `2532` (17,956) |
| [subjref](features/subjref.md) | edge | number of subject referent | word | — |
| [subjrefspec](features/subjrefspec.md) | node | this is XML attribute subjrefspec | phrase, subphrase, word | `"n46003022002"` (344); `"n66001009002"` (262) |
| [tense](features/tense.md) | node | verbal tense | phrase, subphrase, word | `"aorist"` (23,606); `"present"` (23,158) |
| [text](features/text.md) | node | the text of a word | phrase, subphrase, word | `"καὶ"` (17,090); `"ὁ"` (5,538) |
| [trailer](features/trailer.md) | node | material after the end of the word \(excluding critical signs\) | phrase, subphrase, word | `" "` (238,540); `", "` (18,924) |
| [trans](features/trans.md) | node | translation of the word surface text according to the Berean Interlinear Bible | phrase, subphrase, word | `"the"` (19,714); `"and"` (12,424) |
| [translit](features/translit.md) | node | transliteration of the word surface text | phrase, subphrase, word | `"kai"` (17,152); `"en"` (6,304) |
| [typ](features/typ.md) | node | syntactical type \(on sentence, group, clause or phrase\) | group, clause, wg, phrase, subphrase | `"NP"` (61,822); `"PP"` (22,338) |
| [typems](features/typems.md) | node | morphological type \(on word\), syntactical type \(on sentence, group, clause, phrase or wg\) | sentence, group, clause, wg, phrase, subphrase, word | `"modifier-scope"` (59,290); `"common"` (47,288) |
| [unaccent](features/unaccent.md) | node | word in unicode characters without accents and diacritical markers | phrase, subphrase, word | `"και"` (17,152); `"ο"` (6,038) |
| [unicode](features/unicode.md) | node | word in unicode characters plus material after it | phrase, subphrase, word | `"καὶ"` (17,082); `"ὁ"` (5,536) |
| [variant](features/variant.md) | node | this is XML attribute variant | phrase, subphrase, word | `"2"` (302); `"1"` (36) |
| [verse](features/verse.md) | node | verse number, from ref attribute in xml | verse, sentence, group, clause, wg, phrase, subphrase, word | `12` (16,897); `10` (16,869) |
| [voice](features/voice.md) | node | verbal voice | phrase, subphrase, word | `"active"` (41,484); `"passive"` (6,986) |
