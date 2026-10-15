from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Jobs API is running"}

@app.get("/jobs")
def get_jobs():
    conn = sqlite3.connect("djinni.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, url FROM jobs")
    rows = cursor.fetchall()
    conn.close()
    
    jobs = []
    for row in rows:
        jobs.append({
            "id": row[0],
            "title": row[1],
            "url": row[2]
        })
    return jobs
