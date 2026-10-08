# AGENTS.md

## Purpose

This repository is the starter project for the AI Web App Coding workshop.

The project is intentionally skeletal. Participants will progressively build a working web application with the help of an AI coding agent.

The application uses:

- React + Vite for the frontend
- Python + FastAPI for the backend
- SQLite for persistent data

This is an educational workshop environment. Prefer simple, understandable solutions over production-level complexity.

---

## Before Making Changes

Before implementing any feature:

1. Read `README.md`.
2. Read this `AGENTS.md`.
3. Inspect the existing project structure and relevant source files.
4. Understand the existing implementation before changing it.
5. Identify which files need to change.
6. Make the smallest appropriate change that satisfies the request.

Do not assume that functionality exists simply because it would be useful.

Do not implement future workshop features unless they are explicitly requested.

---

## Current Project Structure

### Frontend

```text
frontend/
├── public/
├── src/
│   ├── assets/
│   ├── App.css
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
├── index.html
├── package.json
└── package-lock.json



backend/
├── database/
│   ├── app.db
│   └── database.py
├── main.py
└── requirements.txt