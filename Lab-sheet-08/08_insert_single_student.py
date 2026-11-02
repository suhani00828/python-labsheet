# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    # Ensure the standard table exists, then insert one student safely.
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, marks REAL NOT NULL)")
    name, age, marks = input("Name: ").strip(), int(input("Age: ")), float(input("Marks: "))
    cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
    connection.commit()
    print("Student added with ID", cursor.lastrowid)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
