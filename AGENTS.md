# Workshop Development Instructions

This is an intentionally minimal starter for the 90-minute "AI Web App Coding"
workshop. Participants progressively build the application using GitHub Copilot
Agent. The frontend starts as the standard Vite + React template. The backend
starts as a FastAPI skeleton, with no employee API or CRUD implementation.

## Working Practices

- Inspect the existing codebase before making changes.
- Follow the existing structure and reuse existing files where appropriate.
- Do not introduce unnecessary dependencies.
- Do not modify unrelated files.
- Preserve existing functionality.
- Make targeted changes instead of unnecessarily rewriting code.
- Test changes after implementation.
- Explain significant changes and the checks performed.

## Database Rule

`backend/database/app.db` is the workshop's pre-populated starting dataset.
Do NOT delete, recreate, replace, reset, or reseed it unless the instructor
explicitly asks for it. Do not initialize or seed the database during application
startup. The database exists before the API exists. Participants will build the
API layer themselves during the workshop.