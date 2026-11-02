# Menu-driven student CRUD application backed by SQLite.
from pathlib import Path
import sqlite3

db_path = Path(__file__).with_name("crud_students.sqlite3")
connection = None
try:
    connection = sqlite3.connect(db_path)
    connection.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, marks REAL NOT NULL)")
    while True:
        print("\n1 Add  2 View  3 Update marks  4 Delete  5 Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                name = input("Name: ").strip()
                age, marks = int(input("Age: ")), float(input("Marks: "))
                connection.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
                connection.commit()
                print("Student added.")
            elif choice == "2":
                rows = connection.execute("SELECT id, name, age, marks FROM students ORDER BY id").fetchall()
                print(*rows, sep="\n") if rows else print("No student records.")
            elif choice == "3":
                roll, marks = int(input("Roll number: ")), float(input("New marks: "))
                cursor = connection.execute("UPDATE students SET marks=? WHERE id=?", (marks, roll))
                connection.commit()
                print("Marks updated." if cursor.rowcount else "Student not found.")
            elif choice == "4":
                roll = int(input("Roll number: "))
                cursor = connection.execute("DELETE FROM students WHERE id=?", (roll,))
                connection.commit()
                print("Student deleted." if cursor.rowcount else "Student not found.")
            elif choice == "5":
                break
            else:
                print("Choose 1, 2, 3, 4, or 5.")
        except (sqlite3.Error, ValueError) as error:
            print("Could not complete the operation:", error)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
