# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT name, marks FROM students ORDER BY name")
    rows = cursor.fetchall()
    for name, marks in rows:
        print(f"{name}: {marks:g}")
    if not rows:
        print("No students found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
