import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", "data/history.sqlite")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    input_text TEXT,
    response_text TEXT,
    mode TEXT
)
""")

conn.commit()
conn.close()

print("SQLite database initialized successfully at:", DB_PATH)
