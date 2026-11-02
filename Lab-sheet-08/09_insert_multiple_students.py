# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, marks REAL NOT NULL)")
    records = [("Asha", 19, 85), ("Ravi", 20, 78), ("Neha", 19, 92)]
    cursor.executemany("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", records)
    connection.commit()
    print(f"Inserted {cursor.rowcount} sample students.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
