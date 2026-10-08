import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent / "app.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(f"{DATABASE_PATH.as_uri()}?mode=rw", uri=True)
    connection.row_factory = sqlite3.Row
    return connection