# Jobs API

REST API built with FastAPI that serves job vacancies from a SQLite database.

## Features

- GET `/` — health check endpoint
- GET `/jobs` — returns all job vacancies as JSON
- Auto-generated documentation at `/docs` (Swagger UI)

## Technologies

- **Python 3.12**
- **FastAPI** — modern web framework
- **Uvicorn** — ASGI server
- **SQLite** — database

## How to run

1. Install dependencies:
   pip install fastapi uvicorn

2. Run the server:
   uvicorn api_jobs:app --reload

3. Open in browser:
   - http://127.0.0.1:8000/jobs
   - http://127.0.0.1:8000/docs

## Author

Viktoria Zykova — Junior Python / AI Developer
GitHub: https://github.com/ViktoriaFit