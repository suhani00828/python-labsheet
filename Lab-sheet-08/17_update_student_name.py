# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    student_id = int(input("Student ID: "))
    new_name = input("New name: ").strip()
    cursor.execute("UPDATE students SET name=? WHERE id=?", (new_name, student_id))
    connection.commit()
    print("Name updated." if cursor.rowcount else "Student ID not found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
