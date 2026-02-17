# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# דף 1 + דף 4 – משפטים הגיוניים (בחר משפט אחד מהזוג) + כיתה א
LOGICAL_SENTENCES = [
    {"id": 1, "option1": "לוֹחֲשׁוֹת קוֹף.", "option2": "לוֹחֲשׁוֹת סוֹד.", "correct": 2},
    {"id": 2, "option1": "כּוֹתְבִים עַל דַּף.", "option2": "כּוֹתְבִים עַל כַּף.", "correct": 1},
    {"id": 3, "option1": "קוֹפְצִים בַּחוֹל.", "option2": "קוֹפְצִים בַּבּוֹר.", "correct": 1},
    {"id": 4, "option1": "רוֹכְבוֹת עַל בָּלוֹן.", "option2": "רוֹכְבוֹת עַל חֲמוֹר.", "correct": 2},
    {"id": 5, "option1": "שׁוֹרְקוֹת פִּילִים.", "option2": "שׁוֹרְקוֹת שִׁירִים.", "correct": 2},
    {"id": 6, "option1": "שׁוֹמְרִים עַל תִּינוֹק.", "option2": "שׁוֹמְרִים עַל קִיפּוֹד.", "correct": 1},
    # כיתה א – משפטים פשוטים
    {"id": 7, "option1": "אִמָּא קוֹרְאָה סֵפֶר.", "option2": "אִמָּא קוֹרְאָה כִּסֵּא.", "correct": 1},
    {"id": 8, "option1": "הַכֶּלֶב רָץ בַּגַּן.", "option2": "הַכֶּלֶב רָץ בֶּעָנָן.", "correct": 1},
    {"id": 9, "option1": "הַיֶלֶד אָכַל תַּפּוּחַ.", "option2": "הַיֶלֶד אָכַל כּוֹכָב.", "correct": 1},
    {"id": 10, "option1": "הַחֲתוּל יָשַׁן עַל הַסַּפָּה.", "option2": "הַחֲתוּל יָשַׁן עַל הַיָּרֵחַ.", "correct": 1},
    {"id": 11, "option1": "אַבָּא נוֹהֵג בַּמְּכוֹנִית.", "option2": "אַבָּא נוֹהֵג בַּתַּפּוּחַ.", "correct": 1},
    {"id": 12, "option1": "הַדָּג שָׂחָה בַּמַּיִם.", "option2": "הַדָּג שָׂחָה בַּסֵּפֶר.", "correct": 1},
    {"id": 13, "option1": "הַשֶּׁמֶשׁ זוֹרַחַת בַּבֹּקֶר.", "option2": "הַשֶּׁמֶשׁ זוֹרַחַת בַּכּוֹס.", "correct": 1},
    {"id": 14, "option1": "הַיַּלְדָּה אוֹהֶבֶת פְּרָחִים.", "option2": "הַיַּלְדָּה אוֹהֶבֶת מַקְלֵדַת.", "correct": 1},
    # דפים נוספים – משפט הגיוני
    {"id": 15, "option1": "הַצִּיפּוֹר עָפָה בַּשָּׁמַיִם.", "option2": "הַצִּיפּוֹר עָפָה בַּכּוֹס.", "correct": 1},
    {"id": 16, "option1": "הַתַּפּוּחַ טָעִים וּמָתוֹק.", "option2": "הַתַּפּוּחַ טָעִים וּמְדַבֵּר.", "correct": 1},
    {"id": 17, "option1": "אַבָּא קָנָה לֶחֶם בַּמַּגָּל.", "option2": "אַבָּא קָנָה לֶחֶם בַּחֲנוּת.", "correct": 2},
    {"id": 18, "option1": "הַיֶלֶד שָׂחַק בַּחָצֵר.", "option2": "הַיֶלֶד שָׂחַק בַּמֶּרְקָחָה.", "correct": 1},
    {"id": 19, "option1": "הַכֶּלֶב שָׁמַר עַל הַבַּיִת.", "option2": "הַכֶּלֶב שָׁמַר עַל הַמִּשְׁקָף.", "correct": 1},
    {"id": 20, "option1": "הַיַּלְדָּה צָבְעָה צִיּוּר בַּגְּבִיעַ.", "option2": "הַיַּלְדָּה צָבְעָה צִיּוּר בְּעִפָּרוֹן.", "correct": 2},
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
    # כיתה א – איזה משפט הגיוני
    {"id": 10, "option1": "דָּנִי אוֹכֵל סַנְדְּוִיץ.", "option2": "דָּנִי אוֹכֵל עִפָּרוֹן.", "correct": 1},
    {"id": 11, "option1": "מַיָּה שִׂחֲקָה עִם הַבֻּבָּה.", "option2": "מַיָּה שִׂחֲקָה עִם הַיָּם.", "correct": 1},
    {"id": 12, "option1": "הַיֶלֶד קוֹרֵא סֵפֶר.", "option2": "הַיֶלֶד קוֹרֵא מַיִם.", "correct": 1},
    {"id": 13, "option1": "אִמָּא הֵכִינָה אֲרוּחַת בֹּקֶר.", "option2": "אִמָּא הֵכִינָה הָר.", "correct": 1},
    # דפים נוספים – איזה משפט הגיוני
    {"id": 14, "option1": "רָן הִשְׁקָה אֶת הַפֶּרַח.", "option2": "רָן הִשְׁקָה אֶת הַשֻּׁלְחָן.", "correct": 1},
    {"id": 15, "option1": "נֹעַם אָכַל אֲבַטִּיחַ בַּקַּיִץ.", "option2": "נֹעַם אָכַל מַחְבֶּרֶת בַּקַּיִץ.", "correct": 1},
    {"id": 16, "option1": "הַגַּן יָפֶה בַּאֲבִיב.", "option2": "הַגַּן יָפֶה בַּמֶּרְקָחָה.", "correct": 1},
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
    # כיתה א – התאמת פועל
    {"id": 9, "subject": "הַבָּנוֹת", "verbFem": "רוֹקְדוֹת", "verbMasc": "רוֹקְדִים", "subjectLabel": "בנות"},
    {"id": 10, "subject": "הַבָּנִים", "verbFem": "שׁוֹתוֹת", "verbMasc": "שׁוֹתִים", "subjectLabel": "בנים"},
    {"id": 11, "subject": "הַבָּנוֹת", "verbFem": "צוֹעֲדוֹת", "verbMasc": "צוֹעֲדִים", "subjectLabel": "בנות"},
    {"id": 12, "subject": "הַבָּנִים", "verbFem": "שׁוֹחוֹת", "verbMasc": "שׁוֹחִים", "subjectLabel": "בנים"},
]

# גרירה – הכנסת הברה נכונה במקום הריק (חולם). ההברה כוללת אות+חולם; המקום הריק = תחילת המילה (ימין ב-RTL).
# מילה = correctOption + after (למשל סוֹפֵר = סוֹ + פֵר)
DRAG_SYLLABLE_TASKS = [
    {"id": 1, "before": "", "after": "פֵר", "options": ["סוֹ", "כּוֹ", "טוֹ"], "correctOption": "סוֹ"},
    {"id": 2, "before": "", "after": "ל", "options": ["פּוֹ", "סוֹ", "לוֹ"], "correctOption": "פּוֹ"},
    {"id": 3, "before": "", "after": "פֵא", "options": ["רוֹ", "כּוֹ", "חוֹ"], "correctOption": "רוֹ"},
    {"id": 4, "before": "", "after": "כָב", "options": ["כּוֹ", "סוֹ", "טוֹ"], "correctOption": "כּוֹ"},
    {"id": 5, "before": "", "after": "חֵם", "options": ["לוֹ", "כּוֹ", "פּוֹ"], "correctOption": "לוֹ"},
    {"id": 6, "before": "", "after": "לֵם", "options": ["חוֹ", "רוֹ", "סוֹ"], "correctOption": "חוֹ"},
    {"id": 7, "before": "", "after": "טֵר", "options": ["שׁוֹ", "לוֹ", "כּוֹ"], "correctOption": "שׁוֹ"},
    {"id": 8, "before": "", "after": "לֶה", "options": ["גּוֹ", "בּוֹ", "פּוֹ"], "correctOption": "גּוֹ"},
    {"id": 9, "before": "", "after": "נֶה", "options": ["בּוֹ", "סוֹ", "חוֹ"], "correctOption": "בּוֹ"},
    {"id": 10, "before": "", "after": "רָה", "options": ["תּוֹ", "כּוֹ", "לוֹ"], "correctOption": "תּוֹ"},
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
    {"id": 13, "phrase": "הַלֶּחֶם בַּכַּסֶפֶת", "correct": False},
    {"id": 14, "phrase": "רַכֶּבֶת בַּגִּינָּה", "correct": False},
    {"id": 15, "phrase": "נָמֵר מַצְחִיק", "correct": True},
    {"id": 16, "phrase": "פָּרָה בַּחֶדֶר", "correct": False},
    # כיתה א – כן/לא צירוף
    {"id": 17, "phrase": "אִמָּא טוֹבָה", "correct": True},
    {"id": 18, "phrase": "כֶּלֶב עָף", "correct": False},
    {"id": 19, "phrase": "שֶׁמֶשׁ חַמָּה", "correct": True},
    {"id": 20, "phrase": "דָּג בַּיָּם", "correct": True},
    {"id": 21, "phrase": "בַּיִת גָּבוֹהַּ", "correct": True},
    {"id": 22, "phrase": "עֵץ יָרוֹק", "correct": True},
    {"id": 23, "phrase": "חֲתוּל נוֹבֵחַ", "correct": False},
    {"id": 24, "phrase": "יֶלֶד קוֹרֵא", "correct": True},
    {"id": 25, "phrase": "סֵפֶר עַל שֻׁלְחָן", "correct": True},
    {"id": 26, "phrase": "מַיִם בַּכּוֹס", "correct": True},
    {"id": 27, "phrase": "כֶּלֶב בָּרָקִיעַ", "correct": False},
    {"id": 28, "phrase": "פֶּרַח בַּגַּן", "correct": True},
    {"id": 29, "phrase": "חַמָּה בַּלַּיְלָה", "correct": False},
]

# דף 6 – משפט + כן/לא (קמץ-פתח)
YESNO_PHRASES_PG6 = [
    {"id": 1, "phrase": "צָב קָפַץ", "correct": True},
    {"id": 2, "phrase": "נָדָב רֶץ", "correct": True},
    {"id": 3, "phrase": "הַדָּג רָקָד", "correct": False},
    {"id": 4, "phrase": "הָדַף בַּמָּרָק", "correct": False},
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
    # כיתה א – כן/לא משפט
    {"id": 17, "phrase": "הָאִמָּא אוֹכֶלֶת", "correct": True},
    {"id": 18, "phrase": "הַכֶּלֶב קוֹרֵא", "correct": False},
    {"id": 19, "phrase": "הַיֶלֶד שָׂחַק", "correct": True},
    {"id": 20, "phrase": "הַדָּג הָלַךְ", "correct": False},
    {"id": 21, "phrase": "הַתַּפּוּחַ טָעִים", "correct": True},
    {"id": 22, "phrase": "הַצִּיפּוֹר שָׁרָה", "correct": True},
    {"id": 23, "phrase": "הַכֶּלֶב קָרָא סֵפֶר", "correct": False},
    {"id": 24, "phrase": "הָאִמָּא הֵכִינָה אֲרוּחָה", "correct": True},
    {"id": 25, "phrase": "הַיָּם עָפָה", "correct": False},
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
    # כיתה א – השלם את המשפט
    {"id": 10, "sentence": "אֲנִי אוֹכֵל ______ לַאֲרוּחַת בֹּקֶר.", "option1": "דְּגָנִים", "option2": "מְכוֹנִית", "correct": 1},
    {"id": 11, "sentence": "בַּ______ יֵשׁ מַיִם.", "option1": "כּוֹס", "option2": "עֵץ", "correct": 1},
    {"id": 12, "sentence": "הַיֶלֶד רוֹצֶה ______.", "option1": "מַמְתָּק", "option2": "שָׁמַיִם", "correct": 1},
    {"id": 13, "sentence": "הַ______ שָׁחוֹר וְלָבָן.", "option1": "כֶּלֶב", "option2": "תַּפּוּחַ", "correct": 1},
    {"id": 14, "sentence": "אִמָּא קָנְתָה ______ לַבַּיִת.", "option1": "לֶחֶם", "option2": "יָרֵחַ", "correct": 1},
    {"id": 15, "sentence": "הַיֶלֶד כּוֹתֵב בְּ______.", "option1": "עִפָּרוֹן", "option2": "שָׁמַיִם", "correct": 1},
    {"id": 16, "sentence": "בַּבֹּקֶר הָ______ זוֹרַחַת.", "option1": "שֶׁמֶשׁ", "option2": "כַּף", "correct": 1},
    {"id": 17, "sentence": "הַ______ יָשַׁן עַל הַמִּטָּה.", "option1": "תִּינוֹק", "option2": "מָטוֹס", "correct": 1},
    {"id": 18, "sentence": "הַגַּן מָלֵא בִּ______ יָפִים.", "option1": "פְּרָחִים", "option2": "מְכוֹנִיּוֹת", "correct": 1},
]

# דף 2 – קראו והשלימו (החלפת גוף/מספר – בחר פועל מתאים)
SENTENCE_TRANSFORM = [
    {"id": 1, "original": "הַשׁוֹטֵר רָדַף אַחֲרֵי הַגַּנָּב.", "newSubject": "הַשׁוֹטֶרֶת", "options": ["רָדְפָה", "רָדַף"], "correct": 1},
    {"id": 2, "original": "הַקוֹסֵם יִלְבַּשׁ גְלִימָה בְּצֶבַע אָדוֹם.", "newSubject": "הַקוֹסְמִים", "options": ["יִלְבְּשׁוּ", "יִלְבַּשׁ"], "correct": 1},
    {"id": 3, "original": "הַסּוֹפֵר כָּתַב סֵפֶר עַל קוֹסֵם.", "newSubject": "הַסּוֹפֶרֶת", "options": ["כָּתְבָה", "כָּתַב"], "correct": 1},
    {"id": 4, "original": "הָרוֹפֵא בּוֹדֶק אֶת הַחוֹלֶה.", "newSubject": "הָרוֹפָאוֹת", "options": ["בּוֹדְקוֹת", "בּוֹדֶק"], "correct": 1},
    {"id": 5, "original": "הַשׁוֹפֶטֶת הִכְרִיזָה מִי נָצֶחַ בַּמִּשְׂחָק.", "newSubject": "הַשׁוֹפְטוֹת", "options": ["הִכְרִיזוּ", "הִכְרִיזָה"], "correct": 1},
    {"id": 6, "original": "הָאוֹפֶה אָפָה חַלּוֹת לְשַׁבָּת.", "newSubject": "הָאוֹפִים", "options": ["אָפוּ", "אָפָה"], "correct": 1},
    {"id": 7, "original": "הַיֶלֶד רָץ בַּחָצֵר.", "newSubject": "הַיַּלְדָּה", "options": ["רָצְתָה", "רָץ"], "correct": 1},
    {"id": 8, "original": "הַכֶּלֶב יָשַׁן בַּמִּטָּה.", "newSubject": "הַכְּלָבִים", "options": ["יָשְׁנוּ", "יָשַׁן"], "correct": 1},
]

# דף 2 – השלמת טבלה לפי שורש (בחר את המילה הנכונה מהשורש)
ROOT_TABLE = [
    {"id": 1, "root": "ש.פ.ט", "ask": "יָחִיד", "word": "שׁוֹפֵט", "options": ["שׁוֹפֵט", "שׁוֹפֶטֶת", "שׁוֹפְטִים", "שׁוֹפְטוֹת"]},
    {"id": 2, "root": "ש.פ.ט", "ask": "רַבִּים", "word": "שׁוֹפְטִים", "options": ["שׁוֹפֵט", "שׁוֹפֶטֶת", "שׁוֹפְטִים", "שׁוֹפְטוֹת"]},
    {"id": 3, "root": "פ.ע.ל", "ask": "יְחִידָה", "word": "פּוֹעֶלֶת", "options": ["פּוֹעֵל", "פּוֹעֶלֶת", "פּוֹעֲלִים", "פּוֹעֲלוֹת"]},
    {"id": 4, "root": "ס.פ.ר", "ask": "רַבִּים", "word": "סוֹפְרִים", "options": ["סוֹפֵר", "סוֹפֶרֶת", "סוֹפְרִים", "סוֹפְרוֹת"]},
    {"id": 5, "root": "ר.פ.א", "ask": "יְחִידָה", "word": "רוֹפְאָה", "options": ["רוֹפֵא", "רוֹפְאָה", "רוֹפְאִים", "רוֹפְאוֹת"]},
    {"id": 6, "root": "כ.ת.ב", "ask": "יָחִיד", "word": "כּוֹתֵב", "options": ["כּוֹתֵב", "כּוֹתֶבֶת", "כּוֹתְבִים", "כּוֹתְבוֹת"]},
    {"id": 7, "root": "כ.ת.ב", "ask": "יְחִידָה", "word": "כּוֹתֶבֶת", "options": ["כּוֹתֵב", "כּוֹתֶבֶת", "כּוֹתְבִים", "כּוֹתְבוֹת"]},
    {"id": 8, "root": "ר.צ.ה", "ask": "יָחִיד", "word": "רָץ", "options": ["רָץ", "רָצְתָה", "רָצוּ", "רָצוֹת"]},
]

# קריאת פירמידה – הדרגתי: פתח, קמץ, חיריק, חולם, צירה/סגול, משולב
# level: patach, kamatz, chirik, cholam, tsere_segol, mixed
# mode: "read" = רק קריאה והבא, "choose" = בחר את המילה שקראת
PYRAMID_TASKS = [
    # === פתח (קל) ===
    {"id": 1, "level": "patach", "rows": ["ב", "בָּ", "בָּא"], "fullWord": "בָּא"},
    {"id": 2, "level": "patach", "rows": ["ר", "רַ", "רַב"], "fullWord": "רַב"},
    {"id": 3, "level": "patach", "rows": ["ג", "גַּ", "גַּן"], "fullWord": "גַּן"},
    {"id": 66, "level": "patach", "rows": ["א", "אַ", "אַבָּא"], "fullWord": "אַבָּא"},
    {"id": 67, "level": "patach", "rows": ["א", "אִ", "אִמָּא"], "fullWord": "אִמָּא"},
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
    # === מילה למשפט (5 מילים) – פירמידה ממשפט ===
    {"id": 101, "level": "word_to_sentence", "rows": ["הַיֶלֶד", "הַיֶלֶד קָרָא", "הַיֶלֶד קָרָא סֵפֶר", "הַיֶלֶד קָרָא סֵפֶר יָפֶה", "הַיֶלֶד קָרָא סֵפֶר יָפֶה מְאוֹד"], "fullWord": "הַיֶלֶד קָרָא סֵפֶר יָפֶה מְאוֹד"},
    {"id": 102, "level": "word_to_sentence", "rows": ["הַשֶּׁמֶשׁ", "הַשֶּׁמֶשׁ זָרְחָה", "הַשֶּׁמֶשׁ זָרְחָה בַּבֹּקֶר", "הַשֶּׁמֶשׁ זָרְחָה בַּבֹּקֶר הַיָּפֶה", "הַשֶּׁמֶשׁ זָרְחָה בַּבֹּקֶר הַיָּפֶה מְאוֹד"], "fullWord": "הַשֶּׁמֶשׁ זָרְחָה בַּבֹּקֶר הַיָּפֶה מְאוֹד"},
    {"id": 103, "level": "word_to_sentence", "rows": ["הַתִּינוֹק", "הַתִּינוֹק אָכַל", "הַתִּינוֹק אָכַל בָּנָנָה", "הַתִּינוֹק אָכַל בָּנָנָה גְּדוֹלָה", "הַתִּינוֹק אָכַל בָּנָנָה גְּדוֹלָה וּמְתוּקָה"], "fullWord": "הַתִּינוֹק אָכַל בָּנָנָה גְּדוֹלָה וּמְתוּקָה"},
    {"id": 104, "level": "word_to_sentence", "rows": ["הַכֶּלֶב", "הַכֶּלֶב רָץ", "הַכֶּלֶב רָץ בַּגִּינָּה", "הַכֶּלֶב רָץ בַּגִּינָּה הַיְּרֻקָּה", "הַכֶּלֶב רָץ בַּגִּינָּה הַיְּרֻקָּה הַיּוֹם"], "fullWord": "הַכֶּלֶב רָץ בַּגִּינָּה הַיְּרֻקָּה הַיּוֹם"},
    {"id": 105, "level": "word_to_sentence", "rows": ["אִמָּא", "אִמָּא הֵכִינָה", "אִמָּא הֵכִינָה עוּגָה", "אִמָּא הֵכִינָה עוּגָה טָעִימָה", "אִמָּא הֵכִינָה עוּגָה טָעִימָה לַמִּשְׁפָּחָה"], "fullWord": "אִמָּא הֵכִינָה עוּגָה טָעִימָה לַמִּשְׁפָּחָה"},
    {"id": 106, "level": "word_to_sentence", "rows": ["הַגַּן", "הַגַּן שֶׁלָּנוּ", "הַגַּן שֶׁלָּנוּ יָפֶה", "הַגַּן שֶׁלָּנוּ יָפֶה מְאוֹד", "הַגַּן שֶׁלָּנוּ יָפֶה מְאוֹד בַּקַּיִץ"], "fullWord": "הַגַּן שֶׁלָּנוּ יָפֶה מְאוֹד בַּקַּיִץ"},
    {"id": 107, "level": "word_to_sentence", "rows": ["הַחֲתוּל", "הַחֲתוּל יָשַׁן", "הַחֲתוּל יָשַׁן עַל", "הַחֲתוּל יָשַׁן עַל הַסַּפָּה", "הַחֲתוּל יָשַׁן עַל הַסַּפָּה הָרַכָּה"], "fullWord": "הַחֲתוּל יָשַׁן עַל הַסַּפָּה הָרַכָּה"},
    {"id": 108, "level": "word_to_sentence", "rows": ["אֲנִי", "אֲנִי אוֹהֵב", "אֲנִי אוֹהֵב לִשְׂחוֹת", "אֲנִי אוֹהֵב לִשְׂחוֹת בַּיָּם", "אֲנִי אוֹהֵב לִשְׂחוֹת בַּיָּם הַכָּחוֹל"], "fullWord": "אֲנִי אוֹהֵב לִשְׂחוֹת בַּיָּם הַכָּחוֹל"},
    {"id": 109, "level": "word_to_sentence", "rows": ["הַיֶלֶד", "הַיֶלֶד שָׂחַק", "הַיֶלֶד שָׂחַק בַּחָצֵר", "הַיֶלֶד שָׂחַק בַּחָצֵר הַיָּפָה", "הַיֶלֶד שָׂחַק בַּחָצֵר הַיָּפָה כָּל הַיּוֹם"], "fullWord": "הַיֶלֶד שָׂחַק בַּחָצֵר הַיָּפָה כָּל הַיּוֹם"},
    {"id": 110, "level": "word_to_sentence", "rows": ["הַצִּיפּוֹר", "הַצִּיפּוֹר עָפָה", "הַצִּיפּוֹר עָפָה אֶל", "הַצִּיפּוֹר עָפָה אֶל הַגַּן", "הַצִּיפּוֹר עָפָה אֶל הַגַּן הַיָּרוֹק"], "fullWord": "הַצִּיפּוֹר עָפָה אֶל הַגַּן הַיָּרוֹק"},
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


@app.route("/api/drag-syllable", methods=["GET"])
def get_drag_syllable():
    return jsonify(DRAG_SYLLABLE_TASKS)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
