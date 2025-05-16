# Attendance Manager 📘

A simple interactive web app to track and manage attendance per subject with:

- Attendance percentage calculation
- Classes needed to meet minimum attendance criteria
- Clean UI powered by Tailwind CSS
- Backend API with FastAPI and persistent storage via pickle

---

## Features

- Add attendance records for multiple subjects
- View attendance summary with detailed stats
- Calculates additional classes required to reach 75% attendance threshold
- Fully responsive and modern frontend design
- Easy deployment on Vercel or any Python web hosting

---

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML, JavaScript, Tailwind CSS
- **Data Storage:** Pickle (simple file-based persistence)

---

## Project Structure

```text
attendance-app/
├── api/
│ └── index.py # FastAPI backend API
├── static/
│ ├── style.css # Tailwind CSS styles
│ └── script.js # Frontend JavaScript
├── templates/
│ └── index.html # Frontend HTML page
├── attendance.pkl # Attendance data (auto-generated)
├── requirements.txt # Python dependencies
└── vercel.json # Vercel deployment config
```

---

## Setup & Run Locally

1. **Clone the repo:**

```bash
git clone (https://github.com/unusualmold2003/attendance-manager)
cd attendance-manager
```
2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
uvicorn api.index:app --reload
```

Visit http://127.0.0.1:8000 in your browser.

## Deployment on Vercel

1) Push your code to GitHub.

2) Connect the repo to Vercel.

3) Vercel auto-detects FastAPI via vercel.json.

4) Deploy and access your live app instantly!

## Usage

1) Enter a subject name, classes attended, and total classes.

2) Click Submit to save attendance.

3) Click Show Summary to view all attendance data.

4) See how many additional classes you need to reach 75%.

## Future Enhancements

1) User authentication & multi-user support

2) Export attendance reports (CSV, PDF)

3) Notifications for low attendance alerts

4) More detailed analytics and charts
