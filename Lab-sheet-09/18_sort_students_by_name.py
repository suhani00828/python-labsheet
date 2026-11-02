# Display student rows ordered by name.
from pathlib import Path
import sqlite3

db_path = Path(__file__).with_name("crud_students.sqlite3")
connection = None
try:
    connection = sqlite3.connect(db_path)
    rows = connection.execute("SELECT id, name, age, marks FROM students ORDER BY name COLLATE NOCASE").fetchall()
    print(*rows, sep="\n") if rows else print("No student records.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
