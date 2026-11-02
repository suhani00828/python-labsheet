# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, marks FROM students ORDER BY marks DESC, id LIMIT 3")
    rows = cursor.fetchall()
    for rank, row in enumerate(rows, start=1):
        print(f"{rank}. ID {row[0]} - {row[1]}: {row[2]:g}")
    if not rows:
        print("No students found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
