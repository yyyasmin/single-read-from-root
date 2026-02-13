# לקרוא מן השורש – משחק לילדי כיתה א׳

משחק להפעלה עצמית עם משימות מהדף: **משפטים הגיוניים** (כן/לא) ו**התאמת פועל** (הבנות/הבנים).

## הרצה בהפעלה אחת

מתיקיית שורש הפרויקט:

```bash
python run.py
```

הסקריפט יוצר venv (אם אין), מתקין תלויות backend ו-frontend, ומפעיל את Flask ואת Vite יחד. המשחק זמין ב־`http://localhost:3000`. לעצירה: Ctrl+C.

## הרצה נפרדת

### רק Backend (Flask)

```bash
cd backend
python pip_install.py
```

(או: `python -m venv venv`, `venv\Scripts\activate`, `pip install -r requirements.txt`, `python app.py`)

### רק Frontend (React)

```bash
cd frontend
npm install
npm start
```

## שימוש

- בתפריט: לבחור **קראו והחליטו: כן או לא?** או **התאמת פועל – הבנות והבנים**.
- במשחק: ללחוץ על התשובה הנכונה; מוצג משוב ואז כפתור "הבא" או "סיום וחזרה לתפריט".
