# Find the student or students with the highest marks.
from pathlib import Path
import sqlite3

db_path = Path(__file__).with_name("crud_students.sqlite3")
connection = None
try:
    connection = sqlite3.connect(db_path)
    rows = connection.execute("SELECT id, name, age, marks FROM students WHERE marks=(SELECT MAX(marks) FROM students)").fetchall()
    print(*rows, sep="\n") if rows and rows[0][3] is not None else print("No student records.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
