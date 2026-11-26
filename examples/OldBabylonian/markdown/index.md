# AbB Old Babylonian Cuneiform

Generated with [Doc4CF](https://github.com/tonyjurg/Doc4CF).

Browse the linked feature descriptions and measured profiles below.

## Features

| Feature | Kind | Description | Applies to | Two most common values |
| --- | --- | --- | --- | --- |
| [after](features/after.md) | Node | what comes after a sign or word (- or space) | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"-"` (118,903); `" "` (100,198) |
| [afterr](features/afterr.md) | Node | what comes after a sign or word (- or space); between adjacent signs a ␣ is inserted | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"-"` (118,903); `" "` (100,198) |
| [afteru](features/afteru.md) | Node | what comes after a sign when represented as unicode (space) | [sign](../structure.html#type-sign) | `" "` (50,099); `"/"` (15) |
| [ARK](features/ARK.md) | Node | persistent identifier of type ARK from metadata field "UCLA Library ARK" | [document](../structure.html#type-document) | `"21198/zz0020h36c"` (1); `"21198/zz0022c6r4"` (1) |
| [atf](features/atf.md) | Node | full atf of a sign (without cluster chars) or word (including cluster chars) | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"x"` (13,090); `"a"` (11,653) |
| [atfpost](features/atfpost.md) | Node | atf of cluster closings at sign | [sign](../structure.html#type-sign) | `"_"` (7,226); `"}"` (6,385) |
| [atfpre](features/atfpre.md) | Node | atf of cluster openings at sign | [sign](../structure.html#type-sign) | `"["` (6,942); `"_"` (6,405) |
| [author](features/author.md) | Node | author from metadata field "Author(s)" | [document](../structure.html#type-document) | `"Soldt, Wilfred H. van"` (398); `"Schroeder, Otto"` (203) |
| [col](features/col.md) | Node | ATF column number | [line](../structure.html#type-line) | `1` (145); `2` (142) |
| [collated](features/collated.md) | Node | whether a sign is collated (*) | [sign](../structure.html#type-sign) | `1` (13) |
| [collection](features/collection.md) | Node | collection of a document | [document](../structure.html#type-document) | `"AbB"` (492); `"CT"` (241) |
| [comment](features/comment.md) | Node | $ comment to line or inline comment to slot ($ and $) | [sign](../structure.html#type-sign) | `"blank space"` (256); `"rest broken"` (218) |
| [damage](features/damage.md) | Node | whether a sign is damaged | [sign](../structure.html#type-sign) | `1` (9,974) |
| [det](features/det.md) | Node | whether a sign is a determinative gloss - between braces { } | [sign](../structure.html#type-sign) | `1` (6,796) |
| [docnote](features/docnote.md) | Node | additional remarks in the document identification | [document](../structure.html#type-document) | `"pp. 980191 no. 1"` (1); `"Bu 1888-05-12, 200"` (1) |
| [docnumber](features/docnumber.md) | Node | number of a document within a collection-volume | [document](../structure.html#type-document) | `"001"` (10); `"003"` (10) |
| [excavation](features/excavation.md) | Node | excavation number from metadata field "Excavation no." | [document](../structure.html#type-document) | `"W 16743,az"` (1); `"HMR 686"` (1) |
| [excised](features/excised.md) | Node | whether a sign is excised - between double angle brackets << >> | [sign](../structure.html#type-sign) | `1` (99) |
| [face](features/face.md) | Node | full name of a face including the enclosing object | [face](../structure.html#type-face) | `"obverse"` (1,273); `"reverse"` (1,221) |
| [flags](features/flags.md) | Node | sequence of flags after a sign | [sign](../structure.html#type-sign) | `"#"` (9,830); `"?"` (421) |
| [fraction](features/fraction.md) | Node | fraction of a numeral | [sign](../structure.html#type-sign) | `"1/2"` (73); `"1/3"` (34) |
| [genre](features/genre.md) | Node | genre from metadata field "Genre" | [document](../structure.html#type-document) | `"Letter"` (1,280); `"Legal"` (2) |
| [grapheme](features/grapheme.md) | Node | grapheme of a sign | [sign](../structure.html#type-sign) | `"..."` (1,617); `"ARAD"` (119) |
| [graphemer](features/graphemer.md) | Node | grapheme of a sign using non-ascii characters | [sign](../structure.html#type-sign) | `"..."` (1,617); `"ARAD"` (119) |
| [graphemeu](features/graphemeu.md) | Node | grapheme of a sign using cuneiform unicode characters | [sign](../structure.html#type-sign) | `"..."` (1,617); `"𒀴"` (119) |
| [lang](features/lang.md) | Node | language of a document | [document](../structure.html#type-document) | `"akk"` (1,283); `"sux"` (2) |
| [langalt](features/langalt.md) | Node | 1 if a sign is in the alternate language (i.e. Sumerian) - between underscores _ _ | [sign](../structure.html#type-sign) | `1` (19,063) |
| [ln](features/ln.md) | Node | ATF line number of a numbered line, without prime | [line](../structure.html#type-line) | `1` (2,764); `2` (2,623) |
| [lnc](features/lnc.md) | Node | ATF line identification of a comment line ($) | [line](../structure.html#type-line) | `"$"` (969) |
| [lnno](features/lnno.md) | Node | ATF line number, may be $ or #, with prime; column number prepended | [line](../structure.html#type-line) | `"1"` (2,437); `"2"` (2,319) |
| [material](features/material.md) | Node | material indication from metadata field "Material" | [document](../structure.html#type-document) | `"clay"` (1,283); `"gypsum: plaster"` (1) |
| [missing](features/missing.md) | Node | whether a sign is missing - between square brackets [ ] | [sign](../structure.html#type-sign) | `1` (14,391) |
| [museumcode](features/museumcode.md) | Node | museum code from metadata field "Museum no." | [document](../structure.html#type-document) | `"BM 012839"` (1); `"BM 013174"` (1) |
| [museumname](features/museumname.md) | Node | museum name from metadata field "Collection" | [document](../structure.html#type-document) | `"British Museum, London, UK"` (725); `"Vorderasiatisches Museum, Berlin, Germany"` (221) |
| [object](features/object.md) | Node | name of an object of a document | [face](../structure.html#type-face) | `"tablet"` (2,778); `"envelope"` (43) |
| [operator](features/operator.md) | Node | the ! or x in a !() or x() construction | [sign](../structure.html#type-sign) | `"!"` (117); `"x"` (5) |
| [operatorr](features/operatorr.md) | Node | the ! or x in a !() or x() construction, represented as =, ␣ | [sign](../structure.html#type-sign) | `"="` (117); `"␣"` (5) |
| [operatoru](features/operatoru.md) | Node | the ! or x in a !() or x() construction, represented as =, ␣ | [sign](../structure.html#type-sign) | `"="` (117); `"␣"` (5) |
| [oslots](features/oslots.md) | Edge | Represents set of slots associated with an object | [document](../structure.html#type-document), [face](../structure.html#type-face), [line](../structure.html#type-line), [word](../structure.html#type-word), [cluster](../structure.html#type-cluster) | — |
| [otext](features/otext.md) | Config | Textformatting and corpus segmenting configuration used by the text API |  | — |
| [otype](features/otype.md) | Node | Maps node number to objecttype | [document](../structure.html#type-document), [face](../structure.html#type-face), [line](../structure.html#type-line), [word](../structure.html#type-word), [cluster](../structure.html#type-cluster), [sign](../structure.html#type-sign) | `"sign"` (203,219); `"word"` (76,505) |
| [period](features/period.md) | Node | period indication from metadata field "Period" | [document](../structure.html#type-document) | `"Old Babylonian (ca. 1900-1600 BC)"` (1,209); `"Early Old Babylonian (ca. 2000-1900 BC)"` (76) |
| [pnumber](features/pnumber.md) | Node | P number of a document | [document](../structure.html#type-document) | `"P509373"` (1); `"P509374"` (1) |
| [primecol](features/primecol.md) | Node | whether a prime is present on a column number | [line](../structure.html#type-line) | `1` (4) |
| [primeln](features/primeln.md) | Node | whether a prime is present on a line number | [line](../structure.html#type-line) | `1` (1,825) |
| [pubdate](features/pubdate.md) | Node | publication date from metadata field "Publication date" | [document](../structure.html#type-document) | `"1990"` (399); `"1917"` (304) |
| [question](features/question.md) | Node | whether a sign has the question flag (?) | [sign](../structure.html#type-sign) | `1` (560) |
| [reading](features/reading.md) | Node | reading of a sign | [sign](../structure.html#type-sign) | `"a"` (11,672); `"ma"` (11,449) |
| [readingr](features/readingr.md) | Node | reading of a sign using non-ascii characters | [sign](../structure.html#type-sign) | `"a"` (11,672); `"ma"` (11,449) |
| [readingu](features/readingu.md) | Node | reading of a sign using cuneiform unicode characters | [sign](../structure.html#type-sign) | `"𒀀"` (11,702); `"𒈠"` (11,449) |
| [remarkable](features/remarkable.md) | Node | whether a sign is remarkable (!) | [sign](../structure.html#type-sign) | `1` (99) |
| [remarks](features/remarks.md) | Node | # comment to line | [line](../structure.html#type-line) | `"word (li-ba-al-li-t,u2-ka) divided over two lines"` (1); `"word (i-li-ka-am) divided over two lines"` (1) |
| [repeat](features/repeat.md) | Node | repeat of a numeral; the value n (unknown) is represented as -1 | [sign](../structure.html#type-sign) | `1` (877); `2` (398) |
| [srcfile](features/srcfile.md) | Node | source file name of a document | [document](../structure.html#type-document), [face](../structure.html#type-face), [line](../structure.html#type-line) | `"AbB-secondary"` (21,299); `"AbB-primary"` (10,195) |
| [srcLn](features/srcLn.md) | Node | full line in source file | [document](../structure.html#type-document), [face](../structure.html#type-face), [line](../structure.html#type-line) | `"@obverse"` (1,289); `"@reverse"` (1,225) |
| [srcLnNum](features/srcLnNum.md) | Node | line number in source file | [document](../structure.html#type-document), [face](../structure.html#type-face), [line](../structure.html#type-line) | `15570` (3); `26327` (3) |
| [subgenre](features/subgenre.md) | Node | genre from metadata field "Sub-genre" | [document](../structure.html#type-document) | `"legal"` (1); `"deed"` (1) |
| [supplied](features/supplied.md) | Node | whether a sign is supplied - between angle brackets < > | [sign](../structure.html#type-sign) | `1` (246) |
| [sym](features/sym.md) | Node | essential part of a sign or of a word | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"x"` (15,818); `"a"` (11,720) |
| [symr](features/symr.md) | Node | essential part of a sign or of a word using non-ascii characters | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"x"` (15,818); `"a"` (11,720) |
| [symu](features/symu.md) | Node | essential part of a sign or of a word using cuneiform unicode characters | [word](../structure.html#type-word), [sign](../structure.html#type-sign) | `"x"` (15,818); `"𒀀"` (11,769) |
| [trans](features/trans.md) | Node | whether a line has a translation | [line](../structure.html#type-line) | `1` (134) |
| [transcriber](features/transcriber.md) | Node | person who did the encoding into ATF from metadata field "ATF source" | [document](../structure.html#type-document) | `"Jagersma, Bram"` (954); `"no atf"` (258) |
| [translation@en](features/translation%40en.md) | Node | translation of line in language en = English | [line](../structure.html#type-line) | `"speak,"` (3); `"for my sake forever"` (2) |
| [type](features/type.md) | Node | name of a type of cluster or kind of sign | [cluster](../structure.html#type-cluster), [sign](../structure.html#type-sign) | `"reading"` (188,292); `"unknown"` (8,761) |
| [uncertain](features/uncertain.md) | Node | whether a sign is uncertain - between brackets ( ) | [sign](../structure.html#type-sign) | `1` (1,194) |
| [volume](features/volume.md) | Node | volume of a document within a collection | [document](../structure.html#type-document) | `13` (210); `16` (201) |
