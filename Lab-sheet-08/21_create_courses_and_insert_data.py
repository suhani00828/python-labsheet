# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, course_name TEXT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS enrollments (student_id INTEGER NOT NULL, course_id INTEGER NOT NULL, PRIMARY KEY (student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(id), FOREIGN KEY(course_id) REFERENCES courses(id))")
    cursor.executemany("INSERT OR IGNORE INTO courses (id, course_name) VALUES (?, ?)", [(1, "Python"), (2, "Database Systems")])
    connection.commit()
    print("courses and enrollments tables are ready; sample courses inserted.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
