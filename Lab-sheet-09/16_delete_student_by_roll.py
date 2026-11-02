# Delete a student record using its roll number.
from pathlib import Path
import sqlite3

db_path = Path(__file__).with_name("crud_students.sqlite3")
connection = None
try:
    roll = int(input("Roll number: "))
    connection = sqlite3.connect(db_path)
    cursor = connection.execute("DELETE FROM students WHERE id=?", (roll,))
    connection.commit()
    print("Student deleted." if cursor.rowcount else "Student not found.")
except (sqlite3.Error, ValueError) as error:
    print("Could not delete:", error)
finally:
    if connection is not None:
        connection.close()
