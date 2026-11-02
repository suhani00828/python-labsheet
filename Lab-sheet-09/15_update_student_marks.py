# Update marks for a student identified by roll number.
from pathlib import Path
import sqlite3

db_path = Path(__file__).with_name("crud_students.sqlite3")
connection = None
try:
    roll, marks = int(input("Roll number: ")), float(input("New marks: "))
    connection = sqlite3.connect(db_path)
    cursor = connection.execute("UPDATE students SET marks=? WHERE id=?", (marks, roll))
    connection.commit()
    print("Marks updated." if cursor.rowcount else "Student not found.")
except (sqlite3.Error, ValueError) as error:
    print("Could not update:", error)
finally:
    if connection is not None:
        connection.close()
