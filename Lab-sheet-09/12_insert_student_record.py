# Insert one student record into the shared SQLite database.
from pathlib import Path
import sqlite3

db_path = Path(__file__).with_name("crud_students.sqlite3")
connection = None
try:
    connection = sqlite3.connect(db_path)
    connection.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, marks REAL NOT NULL)")
    name, age, marks = input("Name: ").strip(), int(input("Age: ")), float(input("Marks: "))
    cursor = connection.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
    connection.commit()
    print("Student added with ID", cursor.lastrowid)
except (sqlite3.Error, ValueError) as error:
    print("Could not add student:", error)
finally:
    if connection is not None:
        connection.close()
