# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# דף 1 + דף 4 – משפטים הגיוניים (בחר משפט אחד מהזוג)
LOGICAL_SENTENCES = [
    {"id": 1, "option1": "לוֹחֲשׁוֹת קוֹף.", "option2": "לוֹחֲשׁוֹת סוֹד.", "correct": 2},
    {"id": 2, "option1": "כּוֹתְבִים עַל דַּף.", "option2": "כּוֹתְבִים עַל כַּף.", "correct": 1},
    {"id": 3, "option1": "קוֹפְצִים בַּחוֹל.", "option2": "קוֹפְצִים בַּבּוֹר.", "correct": 1},
    {"id": 4, "option1": "רוֹכְבוֹת עַל בָּלוֹן.", "option2": "רוֹכְבוֹת עַל חֲמוֹר.", "correct": 2},
    {"id": 5, "option1": "שׁוֹרְקוֹת פִּילִים.", "option2": "שׁוֹרְקוֹת שִׁירִים.", "correct": 2},
    {"id": 6, "option1": "שׁוֹמְרִים עַל תִּינוֹק.", "option2": "שׁוֹמְרִים עַל קִיפּוֹד.", "correct": 1},
]

# דף 5 – עוד משפטים הגיוניים (בחר את ההגיוני)
LOGICAL_PAIRS_PG5 = [
    {"id": 1, "option1": "שִׁירִי הִבְרִיחָה עַכְבָּר.", "option2": "שִׁירִי הִצְחִיקָה עַכְבָּר.", "correct": 1},
    {"id": 2, "option1": "מִיכַל אֶכְלָה כָּרִיךְ עִם רִיבָּה.", "option2": "מִיכַל לָבְשָׁה כָּרִיךְ עִם רִיבָּה.", "correct": 1},
    {"id": 3, "option1": "הַתַּנִּין אָכַל חֲטִיף טָעִים.", "option2": "נִיב אָכַל חֲטִיף טָעִים.", "correct": 1},
    {"id": 4, "option1": "גִיל שָׁתַל שְׁתִיל בַּגִּינָּה.", "option2": "גִיל שָׁתֵל תַּנִּין בַּגִּינָּה.", "correct": 1},
    {"id": 5, "option1": "דָּנִי שָׁט בְּסִיכָּה יָפָה.", "option2": "דָּנִי שָׁט בְּסִירָה יָפָה.", "correct": 2},
    {"id": 6, "option1": "לִירִי קִיבְּלָה תַּכְשִׁיט זָהָב.", "option2": "לִירִי קִיבְּלָה תַּרְמִיל זָהָב.", "correct": 1},
    {"id": 7, "option1": "נִילִי סִיפְּרָה בְּדִיחָה מַצְחִיקָה.", "option2": "נִילִי לָקְחָה בְּדִיחָה מַצְחִיקָה.", "correct": 1},
    {"id": 8, "option1": "הַנְּסִיכָה נִישְׁקָה אֶת הַנָּסִיךְ.", "option2": "הַנְּסִיכָה נִישְׁקָה אֶת הַצָּעִיף.", "correct": 1},
    {"id": 9, "option1": "טַלִי בִּיקְשָׁה מֵרָנִי סְלִיחָה.", "option2": "טַלִי בִּיקְשָׁה מֵרָנִי בְּדִיחָה.", "correct": 1},
]

# דף 1, דף 4 – התאמת פועל (הבנות/הבנים)
SUBJECT_VERB_PAIRS = [
    {"id": 1, "subject": "הַבָּנוֹת", "verbFem": "כּוֹתְבוֹת", "verbMasc": "כּוֹתְבִים", "subjectLabel": "בנות"},
    {"id": 2, "subject": "הַבָּנִים", "verbFem": "גּוֹזְרוֹת", "verbMasc": "גּוֹזְרִים", "subjectLabel": "בנים"},
    {"id": 3, "subject": "הַבָּנוֹת", "verbFem": "לוֹבְשׁוֹת", "verbMasc": "לוֹבְשִׁים", "subjectLabel": "בנות"},
    {"id": 4, "subject": "הַבָּנִים", "verbFem": "קוֹפְצוֹת", "verbMasc": "קוֹפְצִים", "subjectLabel": "בנים"},
    {"id": 5, "subject": "הַבָּנוֹת", "verbFem": "חוֹשְׁבוֹת", "verbMasc": "חוֹשְׁבִים", "subjectLabel": "בנות"},
    {"id": 6, "subject": "הַבָּנִים", "verbFem": "בּוֹרְחוֹת", "verbMasc": "בּוֹרְחִים", "subjectLabel": "בנים"},
    {"id": 7, "subject": "הַבָּנוֹת", "verbFem": "מוֹצְאוֹת", "verbMasc": "מוֹצְאִים", "subjectLabel": "בנות"},
    {"id": 8, "subject": "הַבָּנִים", "verbFem": "חוֹלְמוֹת", "verbMasc": "חוֹלְמִים", "subjectLabel": "בנים"},
]

# דף 3 – צירוף + כן/לא (משפט אחד, הגיוני או לא)
YESNO_PHRASES_PG3 = [
    {"id": 1, "phrase": "חוֹפֶשׁ עָגוֹל", "correct": False},
    {"id": 2, "phrase": "אִישׁ קוֹפֵץ", "correct": True},
    {"id": 3, "phrase": "אוֹגֵר אַמִּיץ", "correct": True},
    {"id": 4, "phrase": "שֶׁלֶג קַר", "correct": True},
    {"id": 5, "phrase": "חוֹפֶשׁ גָּדוֹל", "correct": True},
    {"id": 6, "phrase": "אִישׁ נוֹצֵץ", "correct": False},
    {"id": 7, "phrase": "שׁוֹטֵר אַמִּיץ", "correct": True},
    {"id": 8, "phrase": "שֶׁלֶג חַם", "correct": False},
    {"id": 9, "phrase": "הַכֶּתֶר בַּכַּסֶפֶת", "correct": True},
    {"id": 10, "phrase": "רַגֶּפֶת בַּגִּינָּה", "correct": True},
    {"id": 11, "phrase": "נָמֵר מַפְחִיד", "correct": True},
    {"id": 12, "phrase": "פָּרָה בָּרֶפֶת", "correct": True},
    {"id": 13, "phrase": "הַלֶּחֶם בַּכַּסֶפֶת", "correct": True},
    {"id": 14, "phrase": "רַכֶּבֶת בַּגִּינָּה", "correct": True},
    {"id": 15, "phrase": "נָמֵר מַצְחִיק", "correct": True},
    {"id": 16, "phrase": "פָּרָה בַּחֶדֶר", "correct": False},
]

# דף 6 – משפט + כן/לא (קמץ-פתח)
YESNO_PHRASES_PG6 = [
    {"id": 1, "phrase": "צָב קָפַץ", "correct": True},
    {"id": 2, "phrase": "נָדָב רֶץ", "correct": True},
    {"id": 3, "phrase": "הַדָּג רָקָד", "correct": False},
    {"id": 4, "phrase": "הָדַף בַּמָּרָק", "correct": True},
    {"id": 5, "phrase": "אַרְנָב קָפַץ", "correct": True},
    {"id": 6, "phrase": "נָדָב עֶף", "correct": False},
    {"id": 7, "phrase": "הַדָּג שָׂחָה", "correct": True},
    {"id": 8, "phrase": "הַכַּף בַּמָּרָק", "correct": True},
    {"id": 9, "phrase": "דָּן זָרַע חִטָּה", "correct": True},
    {"id": 10, "phrase": "קַרְנַף בַּיָּם", "correct": False},
    {"id": 11, "phrase": "בָּרָד קַר", "correct": True},
    {"id": 12, "phrase": "הַכַּלְבָּה נָבְחָה", "correct": True},
    {"id": 13, "phrase": "דָּן זָרַע מַמְתָּק", "correct": False},
    {"id": 14, "phrase": "דָּג בַּיָּם", "correct": True},
    {"id": 15, "phrase": "בָּרָד חַם", "correct": False},
    {"id": 16, "phrase": "הָעַכְבָּר נָבַח", "correct": False},
]

# דף 7 – השלמת משפט (בחר מילה)
SENTENCE_COMPLETION = [
    {"id": 1, "sentence": "בֶּחָצֵר שֶׁלָּנוּ הָיָה ______ שֶׁאָכַל גֶזֶר.", "option1": "גלשן", "option2": "ארנב", "correct": 2},
    {"id": 2, "sentence": "דִיבַּרְנוּ בַּטֶלֶפוֹן וְקָבַעְנוּ ______ חֲשׁוּבָה.", "option1": "פגישה", "option2": "בדיחה", "correct": 1},
    {"id": 3, "sentence": "הַנָּסִיךְ נָתַן לַנְּסִיכָה ______.", "option1": "סליחה", "option2": "נשיקה", "correct": 2},
    {"id": 4, "sentence": "אֶתְמוֹל יָצָאנוּ לְטִיּוּל וְצָפִינוּ בְּצִיפּוֹרִים עִם ______.", "option1": "מקלדת", "option2": "משקפת", "correct": 2},
    {"id": 5, "sentence": "אָכַלְתִּי הָמוֹן מַמְתַּקִים וּבַסּוֹף הָיְתָה לִי ______.", "option1": "בחילה", "option2": "פציעה", "correct": 1},
    {"id": 6, "sentence": "הַ______ הַשׁוֹבָב זָלַל אֶת כָּל הַגְּבִינָה.", "option1": "ארגז", "option2": "עכבר", "correct": 2},
    {"id": 7, "sentence": "בַּחוֹרֶף הֶחְלַקְנוּ בְּ______ עַל הַשֶׁלֶג.", "option1": "מברשת", "option2": "מזחלת", "correct": 2},
    {"id": 8, "sentence": "הַ______ עף בֵּין פֶּרַח לְפֶרַח וְאָסַף צוּף.", "option1": "גלגל", "option2": "פרפר", "correct": 2},
    {"id": 9, "sentence": "הַיֶלֶד נִבְהָל מְאוֹד בִּגְלַל הַ______.", "option1": "מברשת", "option2": "מפלצת", "correct": 2},
]

# דף 2 – קראו והשלימו (החלפת גוף/מספר – בחר פועל מתאים)
SENTENCE_TRANSFORM = [
    {"id": 1, "original": "הַשׁוֹטֵר רָדַף אַחֲרֵי הַגַּנָּב.", "newSubject": "הַשׁוֹטֶרֶת", "options": ["רָדְפָה", "רָדַף"], "correct": 1},
    {"id": 2, "original": "הַקוֹסֵם יִלְבַּשׁ גְלִימָה בְּצֶבַע אָדוֹם.", "newSubject": "הַקוֹסְמִים", "options": ["יִלְבְּשׁוּ", "יִלְבַּשׁ"], "correct": 1},
    {"id": 3, "original": "הַסּוֹפֵר כָּתַב סֵפֶר עַל קוֹסֵם.", "newSubject": "הַסּוֹפֶרֶת", "options": ["כָּתְבָה", "כָּתַב"], "correct": 1},
    {"id": 4, "original": "הָרוֹפֵא בּוֹדֶק אֶת הַחוֹלֶה.", "newSubject": "הָרוֹפָאוֹת", "options": ["בּוֹדְקוֹת", "בּוֹדֶק"], "correct": 1},
    {"id": 5, "original": "הַשׁוֹפֶטֶת הִכְרִיזָה מִי נָצֶחַ בַּמִּשְׂחָק.", "newSubject": "הַשׁוֹפְטוֹת", "options": ["הִכְרִיזוּ", "הִכְרִיזָה"], "correct": 1},
    {"id": 6, "original": "הָאוֹפֶה אָפָה חַלּוֹת לְשַׁבָּת.", "newSubject": "הָאוֹפִים", "options": ["אָפוּ", "אָפָה"], "correct": 1},
]

# דף 2 – השלמת טבלה לפי שורש (בחר את המילה הנכונה מהשורש)
ROOT_TABLE = [
    {"id": 1, "root": "ש.פ.ט", "ask": "יָחִיד", "word": "שׁוֹפֵט", "options": ["שׁוֹפֵט", "שׁוֹפֶטֶת", "שׁוֹפְטִים", "שׁוֹפְטוֹת"]},
    {"id": 2, "root": "ש.פ.ט", "ask": "רַבִּים", "word": "שׁוֹפְטִים", "options": ["שׁוֹפֵט", "שׁוֹפֶטֶת", "שׁוֹפְטִים", "שׁוֹפְטוֹת"]},
    {"id": 3, "root": "פ.ע.ל", "ask": "יְחִידָה", "word": "פּוֹעֶלֶת", "options": ["פּוֹעֵל", "פּוֹעֶלֶת", "פּוֹעֲלִים", "פּוֹעֲלוֹת"]},
    {"id": 4, "root": "ס.פ.ר", "ask": "רַבִּים", "word": "סוֹפְרִים", "options": ["סוֹפֵר", "סוֹפֶרֶת", "סוֹפְרִים", "סוֹפְרוֹת"]},
    {"id": 5, "root": "ר.פ.א", "ask": "יְחִידָה", "word": "רוֹפְאָה", "options": ["רוֹפֵא", "רוֹפְאָה", "רוֹפְאִים", "רוֹפְאוֹת"]},
]

# קריאת פירמידה – הדרגתי: פתח, קמץ, חיריק, חולם, צירה/סגול, משולב
# level: patach, kamatz, chirik, cholam, tsere_segol, mixed
# mode: "read" = רק קריאה והבא, "choose" = בחר את המילה שקראת
PYRAMID_TASKS = [
    # === פתח (קל) ===
    {"id": 1, "level": "patach", "rows": ["ב", "בָּ", "בָּא"], "fullWord": "בָּא"},
    {"id": 2, "level": "patach", "rows": ["ר", "רַ", "רַב"], "fullWord": "רַב"},
    {"id": 3, "level": "patach", "rows": ["ג", "גַּ", "גַּן"], "fullWord": "גַּן"},
    {"id": 4, "level": "patach", "rows": ["ד", "דַּ", "דַּל"], "fullWord": "דַּל"},
    {"id": 5, "level": "patach", "rows": ["ה", "הַ", "הַר"], "fullWord": "הַר"},
    {"id": 6, "level": "patach", "rows": ["כ", "כַּ", "כַּף"], "fullWord": "כַּף"},
    {"id": 7, "level": "patach", "rows": ["מ", "מַ", "מַת"], "fullWord": "מַת"},
    {"id": 8, "level": "patach", "rows": ["פ", "פַּ", "פַּר"], "fullWord": "פַּר"},
    {"id": 9, "level": "patach", "rows": ["ש", "שַׁ", "שַׁר"], "fullWord": "שַׁר"},
    {"id": 10, "level": "patach", "rows": ["ת", "תַּ", "תַּם"], "fullWord": "תַּם"},
    # === קמץ ===
    {"id": 11, "level": "kamatz", "rows": ["כ", "כָּ", "כָּן"], "fullWord": "כָּן"},
    {"id": 12, "level": "kamatz", "rows": ["פ", "פָּ", "פָּה"], "fullWord": "פָּה"},
    {"id": 13, "level": "kamatz", "rows": ["ד", "דָּ", "דָּם"], "fullWord": "דָּם"},
    {"id": 14, "level": "kamatz", "rows": ["ח", "חָ", "חָם"], "fullWord": "חָם"},
    {"id": 15, "level": "kamatz", "rows": ["ק", "קָ", "קָם"], "fullWord": "קָם"},
    {"id": 16, "level": "kamatz", "rows": ["ר", "רָ", "רָץ"], "fullWord": "רָץ"},
    {"id": 17, "level": "kamatz", "rows": ["ש", "שָׁ", "שָׁם"], "fullWord": "שָׁם"},
    {"id": 18, "level": "kamatz", "rows": ["כָּ", "כָּן", "כָּנָף"], "fullWord": "כָּנָף"},
    {"id": 19, "level": "kamatz", "rows": ["פָּ", "פָּנִי", "פָּנִים"], "fullWord": "פָּנִים"},
    {"id": 20, "level": "kamatz", "rows": ["דָּ", "דָּג", "דָּגִים"], "fullWord": "דָּגִים"},
    # === חיריק ===
    {"id": 21, "level": "chirik", "rows": ["ד", "דִּ", "דִּבְ"], "fullWord": "דִּבְ"},
    {"id": 22, "level": "chirik", "rows": ["כ", "כְּ", "כְּתִי"], "fullWord": "כְּתִי"},
    {"id": 23, "level": "chirik", "rows": ["מ", "מִ", "מִשְׁ"], "fullWord": "מִשְׁ"},
    {"id": 24, "level": "chirik", "rows": ["ס", "סִ", "סִיר"], "fullWord": "סִיר"},
    {"id": 25, "level": "chirik", "rows": ["פ", "פִּ", "פִּרְ"], "fullWord": "פִּרְ"},
    {"id": 26, "level": "chirik", "rows": ["דִּ", "דִּבְרָה"], "fullWord": "דִּבְרָה"},
    {"id": 27, "level": "chirik", "rows": ["כְּ", "כְּתִיבָה"], "fullWord": "כְּתִיבָה"},
    {"id": 28, "level": "chirik", "rows": ["מִ", "מִשְׁפָּחָה"], "fullWord": "מִשְׁפָּחָה"},
    {"id": 29, "level": "chirik", "rows": ["פִּ", "פִּרְחֵי"], "fullWord": "פִּרְחֵי"},
    {"id": 30, "level": "chirik", "rows": ["שִׁ", "שִׁיר", "שִׁירָה"], "fullWord": "שִׁירָה"},
    # === חולם ===
    {"id": 31, "level": "cholam", "rows": ["ס", "סוֹ", "סוֹפֵר"], "fullWord": "סוֹפֵר"},
    {"id": 32, "level": "cholam", "rows": ["פ", "פּוֹ", "פּוֹל"], "fullWord": "פּוֹל"},
    {"id": 33, "level": "cholam", "rows": ["ר", "רוֹ", "רוֹפֵא"], "fullWord": "רוֹפֵא"},
    {"id": 34, "level": "cholam", "rows": ["כ", "כּוֹ", "כּוֹכָב"], "fullWord": "כּוֹכָב"},
    {"id": 35, "level": "cholam", "rows": ["ל", "לוֹ", "לוֹחֵם"], "fullWord": "לוֹחֵם"},
    {"id": 36, "level": "cholam", "rows": ["ח", "חוֹ", "חוֹלֵם"], "fullWord": "חוֹלֵם"},
    {"id": 37, "level": "cholam", "rows": ["שׁ", "שׁוֹ", "שׁוֹטֵר"], "fullWord": "שׁוֹטֵר"},
    {"id": 38, "level": "cholam", "rows": ["ג", "גּוֹ", "גּוֹלֶה"], "fullWord": "גּוֹלֶה"},
    {"id": 39, "level": "cholam", "rows": ["ב", "בּוֹ", "בּוֹנֶה"], "fullWord": "בּוֹנֶה"},
    {"id": 40, "level": "cholam", "rows": ["סוֹ", "סוֹפֵר", "סוֹפְרִים"], "fullWord": "סוֹפְרִים"},
    # === צירה, סגול ===
    {"id": 41, "level": "tsere_segol", "rows": ["ב", "בֶּ", "בֶּן"], "fullWord": "בֶּן"},
    {"id": 42, "level": "tsere_segol", "rows": ["ש", "שֶׁ", "שֶׁל"], "fullWord": "שֶׁל"},
    {"id": 43, "level": "tsere_segol", "rows": ["כ", "כֶּ", "כֶּף"], "fullWord": "כֶּף"},
    {"id": 44, "level": "tsere_segol", "rows": ["ג", "גֶּ", "גֶּרֶן"], "fullWord": "גֶּרֶן"},
    {"id": 45, "level": "tsere_segol", "rows": ["ד", "דֶּ", "דֶּלֶת"], "fullWord": "דֶּלֶת"},
    {"id": 46, "level": "tsere_segol", "rows": ["ה", "הֶ", "הֶחְ"], "fullWord": "הֶחְ"},
    {"id": 47, "level": "tsere_segol", "rows": ["מ", "מֶ", "מֶלֶךְ"], "fullWord": "מֶלֶךְ"},
    {"id": 48, "level": "tsere_segol", "rows": ["פ", "פֶּ", "פֶּרַח"], "fullWord": "פֶּרַח"},
    {"id": 49, "level": "tsere_segol", "rows": ["שֶׁ", "שֶׁמֶשׁ"], "fullWord": "שֶׁמֶשׁ"},
    {"id": 50, "level": "tsere_segol", "rows": ["בֶּ", "בֶּגֶד", "בְּגָדִים"], "fullWord": "בְּגָדִים"},
    # === משולב (קושי עולה) ===
    {"id": 51, "level": "mixed", "rows": ["מ", "מַ", "מַחֲ", "מַחֲנֶה"], "fullWord": "מַחֲנֶה"},
    {"id": 52, "level": "mixed", "rows": ["ש", "שָׁ", "שָׁנִי", "שָׁנִיָּה"], "fullWord": "שָׁנִיָּה"},
    {"id": 53, "level": "mixed", "rows": ["כ", "כְּ", "כְּבָ", "כְּבָשִׂים"], "fullWord": "כְּבָשִׂים"},
    {"id": 54, "level": "mixed", "rows": ["פ", "פֶּ", "פֶּרַח", "פְּרָחִים"], "fullWord": "פְּרָחִים"},
    {"id": 55, "level": "mixed", "rows": ["ר", "רַ", "רַעֲ", "רַעֲמוֹן"], "fullWord": "רַעֲמוֹן"},
    {"id": 56, "level": "mixed", "rows": ["ד", "דֶּ", "דֶּרֶךְ", "דְּרָכִים"], "fullWord": "דְּרָכִים"},
    {"id": 57, "level": "mixed", "rows": ["ה", "הַ", "הַגָּ", "הַגָּדוֹל"], "fullWord": "הַגָּדוֹל"},
    {"id": 58, "level": "mixed", "rows": ["ב", "בַּ", "בַּיִת", "בָּתִּים"], "fullWord": "בָּתִּים"},
    {"id": 59, "level": "mixed", "rows": ["ס", "סַ", "סַפָּר", "סַפָּרִים"], "fullWord": "סַפָּרִים"},
    {"id": 60, "level": "mixed", "rows": ["ת", "תּוֹ", "תּוֹרָה", "תּוֹרָתִי"], "fullWord": "תּוֹרָתִי"},
    # מגוון: בחר את המילה שקראת (צורה שונה)
    {"id": 61, "level": "patach", "mode": "choose", "rows": ["ג", "גַּ", "גַּן"], "options": ["גַּן", "גָּן"], "correct": 1},
    {"id": 62, "level": "kamatz", "mode": "choose", "rows": ["פ", "פָּ", "פָּה"], "options": ["פֶּה", "פָּה"], "correct": 2},
    {"id": 63, "level": "cholam", "mode": "choose", "rows": ["ס", "סוֹ", "סוֹפֵר"], "options": ["סוֹפֵר", "סָפַר"], "correct": 1},
    {"id": 64, "level": "tsere_segol", "mode": "choose", "rows": ["ב", "בֶּ", "בֶּן"], "options": ["בֶּן", "בָּן"], "correct": 1},
    {"id": 65, "level": "mixed", "mode": "choose", "rows": ["מ", "מַ", "מַחֲ", "מַחֲנֶה"], "options": ["מַחֲנֶה", "מְחָנָה"], "correct": 1},
]


@app.route("/api/logical-sentences", methods=["GET"])
def get_logical_sentences():
    return jsonify(LOGICAL_SENTENCES)


@app.route("/api/logical-pairs-pg5", methods=["GET"])
def get_logical_pairs_pg5():
    return jsonify(LOGICAL_PAIRS_PG5)


@app.route("/api/subject-verb-tasks", methods=["GET"])
def get_subject_verb_tasks():
    return jsonify(SUBJECT_VERB_PAIRS)


@app.route("/api/yesno-phrases-pg3", methods=["GET"])
def get_yesno_pg3():
    return jsonify(YESNO_PHRASES_PG3)


@app.route("/api/yesno-phrases-pg6", methods=["GET"])
def get_yesno_pg6():
    return jsonify(YESNO_PHRASES_PG6)


@app.route("/api/sentence-completion", methods=["GET"])
def get_sentence_completion():
    return jsonify(SENTENCE_COMPLETION)


@app.route("/api/sentence-transform", methods=["GET"])
def get_sentence_transform():
    return jsonify(SENTENCE_TRANSFORM)


@app.route("/api/root-table", methods=["GET"])
def get_root_table():
    return jsonify(ROOT_TABLE)


@app.route("/api/pyramid", methods=["GET"])
def get_pyramid():
    return jsonify(PYRAMID_TASKS)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
