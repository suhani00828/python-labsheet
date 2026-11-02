# Connect to a local SQLite database and create the students table.
from pathlib import Path
import sqlite3

db_path = Path(__file__).with_name("crud_students.sqlite3")
connection = None
try:
    connection = sqlite3.connect(db_path)
    connection.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, marks REAL NOT NULL)")
    connection.commit()
    print("Connected; students table is ready.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
