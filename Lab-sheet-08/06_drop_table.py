# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    table_name = input("Table to drop (students/courses/enrollments): ").strip()
    allowed = {"students", "courses", "enrollments"}
    if table_name not in allowed:
        print("Choose one of:", ", ".join(sorted(allowed)))
    else:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        connection.commit()
        print(f"{table_name} table dropped if it existed.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
