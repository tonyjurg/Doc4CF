# Dead Sea Scrolls: biblical and non-biblical scrolls

Generated with [Doc4CF](https://github.com/tonyjurg/Doc4CF).

Browse the linked feature descriptions and measured profiles below.

## Features

| Feature | Kind | Description | Applies to | Two most common values |
| --- | --- | --- | --- | --- |
| [after](features/after.md) | Node | space behind the word, if any | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `" "` (798,549) |
| [alt](features/alt.md) | Node | alternative reading | [sign](../structure.html#type-sign) | `1` (577) |
| [biblical](features/biblical.md) | Node | whether we are in biblical material or not | [scroll](../structure.html#type-scroll), [fragment](../structure.html#type-fragment), [line](../structure.html#type-line), [cluster](../structure.html#type-cluster), [word](../structure.html#type-word) | `1` (267,419); `2` (255) |
| [book](features/book.md) | Node | acronym of the book in which the word occurs | [word](../structure.html#type-word) | `"Is"` (47,932); `"Deut"` (30,043) |
| [book_etcbc](features/book_etcbc.md) | Node | Dead Sea Scrolls: additions based on BHSA | [scroll](../structure.html#type-scroll), [lex](../structure.html#type-lex), [fragment](../structure.html#type-fragment), [line](../structure.html#type-line), [clause](../structure.html#type-clause), [cluster](../structure.html#type-cluster), [phrase](../structure.html#type-phrase), [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `""` (1,890,114); `"Isaiah"` (47,932) |
| [chapter](features/chapter.md) | Node | label of the chapter in which the word occurs | [word](../structure.html#type-word) | `"1"` (11,977); `"5"` (10,580) |
| [cl](features/cl.md) | Node | class (morphology tag) | [word](../structure.html#type-word) | `"cmn"` (113,674); `"prep"` (60,943) |
| [cl2](features/cl2.md) | Node | class (for part 2) (morphology tag) | [word](../structure.html#type-word) | `"d"` (697); `"n"` (353) |
| [cor](features/cor.md) | Node | correction made by an ancient or modern editor | [sign](../structure.html#type-sign) | `3` (4,027); `2` (1,387) |
| [fragment](features/fragment.md) | Node | label of a fragment of a scroll | [fragment](../structure.html#type-fragment), [line](../structure.html#type-line) | `"f1"` (4,497); `"f2"` (2,025) |
| [full](features/full.md) | Node | full transcription (Unicode) of a word including flags and brackets | [word](../structure.html#type-word) | `"ε"` (53,862); `"ו"` (37,369) |
| [fulle](features/fulle.md) | Node | full transcription (ETCBC transliteration) of a word including flags and brackets | [word](../structure.html#type-word) | `" 0 "` (53,862); `"W"` (37,369) |
| [fullo](features/fullo.md) | Node | full transcription (original source) of a word including flags and brackets | [word](../structure.html#type-word) | `"--"` (53,862); `"w"` (37,369) |
| [g_cons](features/g_cons.md) | Node | The consonantal representation of a word or sign in BHSA transliteration. | [word](../structure.html#type-word) | `"W"` (6,738); `"L"` (2,836) |
| [g_lex_etcbc](features/g_lex_etcbc.md) | Node | The consonantal representation of the realised lexeme of a word occurrence in BHSA transliteration | [word](../structure.html#type-word) | `"W"` (6,739); `"L"` (3,302) |
| [g_nme_etcbc](features/g_nme_etcbc.md) | Node | The consonantal representation of the nominal ending of a word in BHSA transliteration. | [word](../structure.html#type-word) | `""` (421,851); `"/J"` (4,866) |
| [g_pfm_etcbc](features/g_pfm_etcbc.md) | Node | The consonantal representation of the preformative of a word in BHSA transliteration. | [word](../structure.html#type-word) | `"J"` (2,220); `"T"` (846) |
| [g_prs_etcbc](features/g_prs_etcbc.md) | Node | The consonantal representation of the pronominal suffix of a word in BHSA transliteration. | [word](../structure.html#type-word) | `"NA"` (312,208); `"W"` (10,194) |
| [g_vbe_etcbc](features/g_vbe_etcbc.md) | Node | The consonantal representation of the verbal ending of a word in BHSA transliteration. | [word](../structure.html#type-word) | `"W"` (1,907); `"TH"` (350) |
| [g_vbs_etcbc](features/g_vbs_etcbc.md) | Node | The consonantal representation of the root formation of a verb in BHSA transliteration. | [word](../structure.html#type-word) | `"H"` (738); `"N"` (465) |
| [glex](features/glex.md) | Node | representation (Unicode) of a lexeme leaving out non-letters | [lex](../structure.html#type-lex), [word](../structure.html#type-word) | `"וְ"` (45,091); `"לְ"` (21,550) |
| [glexe](features/glexe.md) | Node | representation (ETCBC transliteration) of a lexeme leaving out non-letters | [lex](../structure.html#type-lex), [word](../structure.html#type-word) | `"W:"` (45,091); `"L:"` (21,550) |
| [glexo](features/glexo.md) | Node | representation (original source) of a lexeme leaving out non-letters | [lex](../structure.html#type-lex), [word](../structure.html#type-word) | `"w◊"` (45,091); `"lV"` (21,550) |
| [glyph](features/glyph.md) | Node | representation (Unicode) of a word or sign | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"ו"` (188,859); `"י"` (125,341) |
| [glyphe](features/glyphe.md) | Node | representation (ETCBC transliteration) of a word or sign | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"W"` (188,859); `"J"` (125,341) |
| [glypho](features/glypho.md) | Node | representation (original source) of a word or sign | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"w"` (188,859); `"y"` (125,341) |
| [gn](features/gn.md) | Node | gender (morphology tag) | [word](../structure.html#type-word) | `"m"` (137,217); `"f"` (36,093) |
| [gn2](features/gn2.md) | Node | gender (for part 2) (morphology tag) | [word](../structure.html#type-word) | `"m"` (32,063); `"c"` (8,233) |
| [gn3](features/gn3.md) | Node | gender (for part 3) (morphology tag) | [word](../structure.html#type-word) | `"c"` (5); `"m"` (5) |
| [gn_etcbc](features/gn_etcbc.md) | Node | Dead Sea Scrolls: additions based on BHSA and machine learning | [word](../structure.html#type-word) | `"NA"` (86,611); `"m"` (84,962) |
| [halfverse](features/halfverse.md) | Node | label of the half-verse in which the word occurs | [word](../structure.html#type-word) | `"b"` (645); `"a"` (287) |
| [intl](features/intl.md) | Node | interlinear material, the value indicates the sequence number of the interlinear line | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `1` (1,573); `2` (59) |
| [lang](features/lang.md) | Node | language of a word or sign, only if it is not Hebrew | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"a"` (185,116); `"g"` (23) |
| [lang_etcbc](features/lang_etcbc.md) | Node | Dead Sea Scrolls: additions based on BHSA | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"Hebrew"` (1,746,097); `"Aramaic"` (185,116) |
| [lex](features/lex.md) | Node | representation (Unicode) of a lexeme | [lex](../structure.html#type-lex), [word](../structure.html#type-word) | `" # "` (54,190); `"וְ"` (45,091) |
| [lex_etcbc](features/lex_etcbc.md) | Node | The consonantal representation of the lexeme of a word occurrence in BHSA transliteration | [word](../structure.html#type-word) | `""` (75,392); `"W"` (46,390) |
| [lex_utf8_etcbc](features/lex_utf8_etcbc.md) | Node | The pointed representation of the lexeme of a word | [word](../structure.html#type-word) | `"וְ"` (45,199); `"לְ"` (21,603) |
| [lexe](features/lexe.md) | Node | representation (ETCBC transliteration) of a lexeme | [lex](../structure.html#type-lex), [word](../structure.html#type-word) | `" # "` (54,190); `"W:"` (45,091) |
| [lexo](features/lexo.md) | Node | representation (original source) of a lexeme | [lex](../structure.html#type-lex), [word](../structure.html#type-word) | `"\\"` (54,190); `"w◊"` (45,091) |
| [line](features/line.md) | Node | label of a line of a fragment of a scroll | [line](../structure.html#type-line) | `"1"` (10,577); `"2"` (8,931) |
| [md](features/md.md) | Node | mood (morphology tag) | [word](../structure.html#type-word) | `"juss"` (1,333); `"coho"` (546) |
| [merr](features/merr.md) | Node | errors in parsing the morphology tag | [word](../structure.html#type-word) | `"vnPfpa"` (1) |
| [morph_etcbc](features/morph_etcbc.md) | Node | The complete morphological parsing of a word in the BHSA convention. | [word](../structure.html#type-word) | `"W"` (6,455); `"H"` (2,782) |
| [morpho](features/morpho.md) | Node | morphological tag (by Abegg) | [word](../structure.html#type-word) | `"0"` (80,250); `"Pc"` (51,775) |
| [note_etcbc](features/note_etcbc.md) | Node | Notes by Thijs Amersfoort (11Q19, 1Qisaa) and Saulo de Oliveira Cantanhêde (1QpHab) during the morphological parsing of the text. | [word](../structure.html#type-word) | `"Afgebroken"` (5); `"Weer afgebroken"` (2) |
| [nr](features/nr.md) | Node | Dead Sea Scrolls: additions based on BHSA and machine learning | [clause](../structure.html#type-clause), [phrase](../structure.html#type-phrase) | `"1"` (2); `"2"` (2) |
| [nu](features/nu.md) | Node | number (morphology tag) | [word](../structure.html#type-word) | `"s"` (139,444); `"p"` (51,752) |
| [nu2](features/nu2.md) | Node | number (for part 2) (morphology tag) | [word](../structure.html#type-word) | `"s"` (32,611); `"p"` (11,783) |
| [nu3](features/nu3.md) | Node | number (for part 3) (morphology tag) | [word](../structure.html#type-word) | `"s"` (14) |
| [nu_etcbc](features/nu_etcbc.md) | Node | Dead Sea Scrolls: additions based on BHSA and machine learning | [word](../structure.html#type-word) | `"NA"` (304,570); `"sg"` (141,183) |
| [occ](features/occ.md) | Edge | edge feature from a lexeme to its occurrences | [lex](../structure.html#type-lex) | — |
| [oslots](features/oslots.md) | Edge | Represents set of slots associated with an object | [scroll](../structure.html#type-scroll), [lex](../structure.html#type-lex), [fragment](../structure.html#type-fragment), [line](../structure.html#type-line), [clause](../structure.html#type-clause), [cluster](../structure.html#type-cluster), [phrase](../structure.html#type-phrase), [word](../structure.html#type-word) | — |
| [otext](features/otext.md) | Config | Textformatting and corpus segmenting configuration used by the text API |  | — |
| [otype](features/otype.md) | Node | Maps node number to objecttype | [scroll](../structure.html#type-scroll), [lex](../structure.html#type-lex), [fragment](../structure.html#type-fragment), [line](../structure.html#type-line), [clause](../structure.html#type-clause), [cluster](../structure.html#type-cluster), [phrase](../structure.html#type-phrase), [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"sign"` (1,430,241); `"word"` (500,995) |
| [ps](features/ps.md) | Node | person (morphology tag) | [word](../structure.html#type-word) | `"3"` (33,880); `"2"` (7,924) |
| [ps2](features/ps2.md) | Node | person (for part 2) (morphology tag) | [word](../structure.html#type-word) | `"3"` (23,750); `"2"` (12,427) |
| [ps3](features/ps3.md) | Node | person (for part 3) (morphology tag) | [word](../structure.html#type-word) | `"2"` (7); `"1"` (5) |
| [ps_etcbc](features/ps_etcbc.md) | Node | Dead Sea Scrolls: additions based on BHSA and machine learning | [word](../structure.html#type-word) | `"NA"` (451,931); `"p3"` (33,853) |
| [punc](features/punc.md) | Node | trailing punctuation (Unicode) of a word | [word](../structure.html#type-word) | `"׃"` (29,909); `"׃׃"` (18) |
| [punce](features/punce.md) | Node | trailing punctuation (ETCBC transliteration) of a word | [word](../structure.html#type-word) | `"00"` (29,909); `"0000"` (18) |
| [punco](features/punco.md) | Node | trailing punctuation (original source) of a word | [word](../structure.html#type-word) | `"."` (29,909); `"±"` (18) |
| [rec](features/rec.md) | Node | reconstructed by a modern editor | [sign](../structure.html#type-sign) | `1` (661,789) |
| [rem](features/rem.md) | Node | removed by an ancient or modern editor | [sign](../structure.html#type-sign) | `2` (1,921); `1` (343) |
| [script](features/script.md) | Node | script in which the word or sign is written if it is not Hebrew | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"paleohebrew"` (4,087); `"greekcapital"` (23) |
| [scroll](features/scroll.md) | Node | acronym of a scroll | [scroll](../structure.html#type-scroll), [fragment](../structure.html#type-fragment), [line](../structure.html#type-line) | `"1Qisaa"` (1,660); `"4Q418"` (1,367) |
| [sim](features/sim.md) | Edge | similarity between lines, as a percentage of the common material wrt the combined material | [line](../structure.html#type-line) | `60` (24,546); `67` (11,761) |
| [sp](features/sp.md) | Node | part of speech (morphology tag) | [word](../structure.html#type-word) | `"ptcl"` (154,464); `"subs"` (108,562) |
| [sp_etcbc](features/sp_etcbc.md) | Node | The part of speech (morphology tag) | [word](../structure.html#type-word) | `""` (281,093); `"subs"` (66,145) |
| [srcLn](features/srcLn.md) | Node | the line number of the word in the source data file | [word](../structure.html#type-word) | `4` (2); `5` (2) |
| [st](features/st.md) | Node | state (morphology tag) | [word](../structure.html#type-word) | `"c"` (60,210); `"a"` (43,218) |
| [type](features/type.md) | Node | type of sign or cluster | [cluster](../structure.html#type-cluster), [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"cons"` (1,156,780); `"glyph"` (470,605) |
| [unc](features/unc.md) | Node | uncertain material in various degrees: higher degree is less certain | [sign](../structure.html#type-sign) | `4` (40,167); `2` (27,146) |
| [uvf_etcbc](features/uvf_etcbc.md) | Node | The consonantal representation of the univalent final consonant of a word in BHSA transliteration. | [word](../structure.html#type-word) | `""` (440,941); `"H"` (498) |
| [vac](features/vac.md) | Node | empty, unwritten space | [sign](../structure.html#type-sign) | `1` (3,524) |
| [verse](features/verse.md) | Node | label of the verse in which the word occurs | [word](../structure.html#type-word) | `"1"` (12,290); `"2"` (11,890) |
| [vs](features/vs.md) | Node | verbal stem (morphology tag) | [word](../structure.html#type-word) | `"qal"` (38,989); `"hifil"` (8,350) |
| [vs_etcbc](features/vs_etcbc.md) | Node | Dead Sea Scrolls: additions based on BHSA and machine learning | [word](../structure.html#type-word) | `"NA"` (434,689); `"qal"` (39,022) |
| [vt](features/vt.md) | Node | verbal tense/aspect (morphology tag) | [word](../structure.html#type-word) | `"perf"` (19,210); `"impf"` (18,719) |
| [vt_etcbc](features/vt_etcbc.md) | Node | Dead Sea Scrolls: additions based on BHSA and machine learning | [word](../structure.html#type-word) | `"NA"` (434,704); `"perf"` (19,191) |
