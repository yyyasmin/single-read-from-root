# פריסה: Netlify (פרונטאנד) + Render (בקאנד)

פרויקט **reading-from-root** (לקרוא מן השורש) – ריפו אחד ב-GitHub, פרונטאנד ב-Netlify ובקאנד ב-Render.

---

## 1. ריפו חדש ב-GitHub

1. היכנסי ל-[GitHub](https://github.com) (חשבון **yyyasmin**).
2. **New repository**
   - Name: `reading-from-root`
   - Public
   - אל תוסיפי README / .gitignore (כבר קיימים בפרויקט).
3. צרי את הריפו.

---

## 2. דחיפה מהמחשב ל-GitHub

בטרמינל, מתיקיית הפרויקט (איפה ש־`backend`, `frontend`, `netlify.toml`):

```bash
git init
git add .
git commit -m "Initial: reading-from-root frontend + backend"
git branch -M main
git remote add origin https://github.com/yyyasmin/reading-from-root.git
git push -u origin main
```

אם GitHub מבקש אימות – השתמשי ב-**Personal Access Token** (לא בסיסמת החשבון).  
ב-GitHub: Settings → Developer settings → Personal access tokens → Generate new token (עם scope `repo`).

---

## 3. בקאנד ב-Render

1. היכנסי ל-[Render](https://render.com) (התחברי עם GitHub).
2. **New** → **Web Service**.
3. **Connect** את הריפו `yyyasmin/reading-from-root`.
4. הגדרות:
   - **Name:** `reading-from-root-api` (או כל שם).
   - **Root Directory:** `backend`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
5. **Create Web Service**.
6. אחרי הפריסה – העתיקי את כתובת ה-API, למשל:  
   `https://reading-from-root-api.onrender.com`  
   (בלי `/api` בסוף – הפרונטאנד יוסיף `/api` בעצמו).

---

## 4. פרונטאנד ב-Netlify

1. היכנסי ל-[Netlify](https://app.netlify.com) (צוות **yasminamran**).
2. **Add new site** → **Import an existing project**.
3. **Connect to Git** → GitHub → בחרי את `yyyasmin/reading-from-root`.
4. הגדרות Build:
   - **Base directory:** `frontend`
   - **Build command:** `npm install && npm run build`
   - **Publish directory:** `frontend/dist`
   - **Environment variables** – הוסיפי:
     - **Key:** `VITE_API_URL`  
     - **Value:** כתובת הבקאנד מ-Render, למשל:  
       `https://reading-from-root-api.onrender.com`  
       (בלי `/api`, בלי סלאש בסוף.)
5. **Deploy site**.

אחרי הדפלוי, האתר יהיה זמין בכתובת Netlify (למשל `https://something.netlify.app`).

---

## 5. בדיקה

- פתחי את האתר ב-Netlify – התפריט והמשחקים אמורים לעבוד.
- אם יש שגיאות ברשת (Network) – וודאי ש־`VITE_API_URL` ב-Netlify מצביע בדיוק לכתובת ה-URL של השירות ב-Render (ללא `/api`).

---

**חשוב:** אל תשימי סיסמאות או tokens בתוך הקוד או ב־commit. החיבורים ל-Netlify ול-Render נעשים דרך GitHub (OAuth) ומשתני סביבה בממשק של כל שירות.
