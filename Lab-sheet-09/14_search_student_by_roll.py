# Find a student by their database ID/roll number.
from pathlib import Path
import sqlite3

db_path = Path(__file__).with_name("crud_students.sqlite3")
connection = None
try:
    roll = int(input("Roll number: "))
    connection = sqlite3.connect(db_path)
    row = connection.execute("SELECT id, name, age, marks FROM students WHERE id=?", (roll,)).fetchone()
    print(row if row else "Student not found.")
except (sqlite3.Error, ValueError) as error:
    print("Could not search:", error)
finally:
    if connection is not None:
        connection.close()
