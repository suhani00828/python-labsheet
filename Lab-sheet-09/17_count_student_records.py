# Count records in the students table.
from pathlib import Path
import sqlite3

db_path = Path(__file__).with_name("crud_students.sqlite3")
connection = None
try:
    connection = sqlite3.connect(db_path)
    count = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    print("Total student records:", count)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
