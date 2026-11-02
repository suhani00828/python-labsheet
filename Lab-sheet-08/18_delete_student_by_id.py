# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    student_id = int(input("Student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    connection.commit()
    print("Student deleted." if cursor.rowcount else "Student ID not found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
