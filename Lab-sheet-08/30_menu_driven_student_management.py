# Menu-driven CRUD application for student records.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

def show_students(connection):
    """Display all stored students."""
    rows = connection.execute("SELECT id, name, age, marks FROM students ORDER BY id").fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No students found.")

connection = None
try:
    connection = sqlite3.connect(DB_PATH)
    connection.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, marks REAL NOT NULL)")
    while True:
        print("\n1 Add  2 View  3 Update marks  4 Delete  5 Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            age = int(input("Age: "))
            marks = float(input("Marks: "))
            connection.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
            connection.commit()
            print("Student added.")
        elif choice == "2":
            show_students(connection)
        elif choice == "3":
            student_id = int(input("Student ID: "))
            marks = float(input("New marks: "))
            cursor = connection.execute("UPDATE students SET marks=? WHERE id=?", (marks, student_id))
            connection.commit()
            print("Marks updated." if cursor.rowcount else "Student ID not found.")
        elif choice == "4":
            student_id = int(input("Student ID to delete: "))
            cursor = connection.execute("DELETE FROM students WHERE id=?", (student_id,))
            connection.commit()
            print("Student deleted." if cursor.rowcount else "Student ID not found.")
        elif choice == "5":
            break
        else:
            print("Choose 1, 2, 3, 4, or 5.")
except (sqlite3.Error, ValueError) as error:
    print("Could not complete the operation:", error)
finally:
    if connection is not None:
        connection.close()
