# Database tasks use a local SQLite database beside this script.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    import csv
    csv_path = Path(__file__).with_name("students_import.csv")
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, marks REAL NOT NULL)")
    try:
        with csv_path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = [(row["name"].strip(), int(row["age"]), float(row["marks"])) for row in reader]
        cursor.executemany("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", rows)
        connection.commit()
        print(f"Imported {len(rows)} student(s) from {csv_path.name}.")
    except FileNotFoundError:
        print(f"Place {csv_path.name} beside this script with name,age,marks headers.")
    except (KeyError, ValueError) as error:
        print("CSV data/headers are invalid:", error)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
