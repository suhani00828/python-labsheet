# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    # SQLite has no TRUNCATE TABLE; DELETE removes rows and preserves table structure.
    cursor.execute("DELETE FROM students")
    connection.commit()
    print(f"Removed {cursor.rowcount} row(s); students table structure remains.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
