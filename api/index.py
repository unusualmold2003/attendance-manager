from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import pickle

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

ATTENDANCE_FILE = "attendance.pkl"
attendance = {}
MIN_ATTENDANCE_PERCENT = 75

def load_attendance():
    global attendance
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "rb") as f:
            attendance.update(pickle.load(f))

def save_attendance():
    with open(ATTENDANCE_FILE, "wb") as f:
        pickle.dump(attendance, f)

def classes_to_attend(attended, total, min_percent):
    min_att = min_percent / 100
    x = 0
    while (attended + x) / (total + x) < min_att:
        x += 1
    return x

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("templates/index.html") as f:
        return f.read()

@app.post("/api/attendance")
async def submit_attendance(request: Request):
    data = await request.json()
    subject = data.get("subject")
    attended = int(data.get("attended", 0))
    total = int(data.get("total", 0))

    if not subject or total == 0 or attended > total:
        return JSONResponse({"message": "Invalid input."}, status_code=400)

    percent = round((attended / total) * 100, 2)
    more_needed = classes_to_attend(attended, total, MIN_ATTENDANCE_PERCENT)

    attendance[subject] = [attended, total, percent, more_needed]
    save_attendance()

    return {"message": f"Attendance recorded for {subject}"}

@app.get("/api/summary")
async def fetch_summary():
    return [
        {
            "subject": sub,
            "attended": val[0],
            "total": val[1],
            "percentage": val[2],
            "additional_needed": val[3]
        }
        for sub, val in attendance.items()
    ]

load_attendance()
