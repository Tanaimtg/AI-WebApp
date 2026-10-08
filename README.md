# AI Web App Coding

A 90-minute hands-on workshop in which participants progressively build a web
application using GitHub Copilot Agent.

This repository is intentionally a minimal starter:

- **Frontend:** the standard React + Vite JavaScript starter page.
- **Backend:** a Python + FastAPI skeleton, served with Uvicorn.
- **Database:** SQLite with eight fictional employee records already included.

The frontend and backend are **not connected initially**. Employee API endpoints
and CRUD operations will be built during the workshop, not provided here.

## Prerequisites

Install Node.js 22.12+ (or a supported newer LTS version), npm, Python 3.10+,
and Git. Open two terminals: one for each application.

## Run the Frontend

From the repository root:

```sh
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite (normally http://localhost:5173). You should
see the default Vite + React page. On Windows, if PowerShell blocks `npm.ps1`,
use `npm.cmd install` and `npm.cmd run dev` instead.

## Run the Backend

From the repository root, create and activate a virtual environment.

Windows PowerShell:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

If PowerShell blocks activation, use `.\.venv\Scripts\python.exe` in place of
`python` for the installation and Uvicorn commands; activation is optional.

macOS / Linux:

```sh
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

The backend normally runs at http://127.0.0.1:8000. Open
http://127.0.0.1:8000/docs to see FastAPI's built-in documentation. There are no
application endpoints yet; visiting the root URL returns 404, which is expected.

## Starting Database

`backend/database/app.db` is included in Git and already contains an `employees`
table with `id`, `name`, `email`, `department`, `role`, and `status` columns.
There is no seed command to run. `backend/database/database.py` supplies only
the database path and a basic SQLite connection helper.

Do not delete, recreate, replace, reset, or reseed this database unless the
instructor explicitly asks. Starting the backend does not change the database.
Every participant begins with the same eight fictional records.

## Repository Structure

```text
AI-WebApp/
|-- README.md
|-- AGENTS.md
|-- .gitignore
|-- frontend/
|   |-- package.json
|   |-- package-lock.json
|   |-- vite.config.js
|   |-- index.html
|   |-- public/              Standard Vite assets
|   `-- src/
|       |-- assets/          Standard React assets
|       |-- App.jsx
|       |-- App.css
|       |-- index.css
|       `-- main.jsx
`-- backend/
    |-- requirements.txt
    |-- main.py
    `-- database/
        |-- database.py
        `-- app.db
```

The frontend also retains the default template's lint configuration, ignore
file, and template README. Installed dependencies and virtual environments are
local only and are not committed.

## Workshop Development Loop

Understand -> Communicate -> Build -> Run -> Evaluate -> Iterate -> Debug

Understand the goal and existing code. Communicate a focused request to Copilot.
Build a small change, run it, and evaluate the result. Iterate on what you learn
and debug problems before moving on.

"AI can write the code. The human decides whether the code is correct."