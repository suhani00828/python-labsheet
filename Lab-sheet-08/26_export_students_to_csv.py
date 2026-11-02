# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    import csv
    csv_path = Path(__file__).with_name("students_export.csv")
    cursor.execute("SELECT id, name, age, marks FROM students ORDER BY id")
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "age", "marks"])
        writer.writerows(cursor.fetchall())
    print(f"Exported students to {csv_path.name}.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
