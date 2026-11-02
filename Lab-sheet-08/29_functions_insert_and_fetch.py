# Use functions to insert one student and fetch all students.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

def insert_student(connection, name, age, marks):
    """Insert one student using a parameterized query."""
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
    connection.commit()

def fetch_students(connection):
    """Return all students in ID order."""
    return connection.execute("SELECT id, name, age, marks FROM students ORDER BY id").fetchall()

connection = None
try:
    connection = sqlite3.connect(DB_PATH)
    connection.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, marks REAL NOT NULL)")
    insert_student(connection, "Sample Student", 20, 88)
    for student in fetch_students(connection):
        print(student)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
