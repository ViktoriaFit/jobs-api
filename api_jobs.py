from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

PG_CONN = os.environ.get("DATABASE_URL")

@app.get("/")
def home():
    return {"message": "Jobs API is running"}

@app.get("/jobs")
def get_jobs():
    conn = psycopg2.connect(PG_CONN)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, url FROM jobs ORDER BY id")
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
