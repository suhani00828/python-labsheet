# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    query = """SELECT s.name, c.course_name FROM students AS s
               LEFT JOIN enrollments AS e ON e.student_id=s.id
               LEFT JOIN courses AS c ON c.id=e.course_id ORDER BY s.name"""
    cursor.execute(query)
    rows = cursor.fetchall()
    for name, course in rows:
        print(f"{name} - {course or 'No course enrolled'}")
    if not rows:
        print("No students found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
