# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(students)")
    columns = cursor.fetchall()
    if columns:
        for column in columns:
            print(f"{column[1]}: {column[2]} (primary key: {bool(column[5])})")
    else:
        print("students table does not exist. Run program 03 first.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
