# Jobs API (FastAPI + PostgreSQL)

## Overview
A REST API built with FastAPI that serves job vacancies stored in a PostgreSQL database. This project demonstrates backend development skills, database integration, environment variable management, and containerization with Docker.

## Features
- **REST API:** Clean endpoints to fetch job vacancies.
- **Swagger Documentation:** Auto-generated interactive API docs at `/docs`.
- **Cloud Database:** Connected to Neon PostgreSQL.
- **Security:** Credentials stored securely using environment variables (`.env`).
- **Dockerized:** Fully containerized with `Dockerfile` and `docker-compose`.

## Tech Stack
- **Backend:** Python, FastAPI, Uvicorn
- **Database:** PostgreSQL (Neon), psycopg2
- **Tools:** Docker, python-dotenv, Git
- **Deployment:** Render (or any Docker-ready cloud)

## API Documentation
Once running, open `http://127.0.0.1:8000/docs` to see the Swagger UI.

## Author
**Viktoria Zykova** – [GitHub](https://github.com/ViktoriaFit)