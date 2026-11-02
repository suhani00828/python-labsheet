# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, age, marks FROM students ORDER BY marks DESC, id")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
