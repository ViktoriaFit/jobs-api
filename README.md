# Jobs API

REST API built with FastAPI that serves job vacancies from a PostgreSQL database.

## Features

- GET `/` — health check endpoint
- GET `/jobs` — returns all job vacancies as JSON
- Auto-generated documentation at `/docs` (Swagger UI)

## Technologies

- **Python 3.12**
- **FastAPI** — modern web framework
- **PostgreSQL** — cloud database (Neon)
- **psycopg2** — PostgreSQL adapter for Python
- **python-dotenv** — environment variables management
- **Uvicorn** — ASGI server

## Security

Database credentials are stored in environment variables (`.env` file)
and are NOT included in the repository. See `.gitignore`.

## How to run

1. Install dependencies:
   pip install fastapi uvicorn psycopg2-binary python-dotenv

2. Create a `.env` file with your database connection string:
   DATABASE_URL=postgresql://user:password@host:5432/dbname

3. Run the server:
   uvicorn api_jobs:app --reload

4. Open in browser:
   - http://127.0.0.1:8000/jobs — list of jobs
   - http://127.0.0.1:8000/docs — interactive documentation

## Author

Viktoria Zykova — Junior Python / AI Developer
GitHub: https://github.com/ViktoriaFit
