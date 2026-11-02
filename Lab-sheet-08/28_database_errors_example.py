# Demonstrate SQLite error handling and always close the database connection.
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("student_db.sqlite3")
connection = None
try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    # This deliberately invalid query demonstrates catching a database error.
    cursor.execute("SELEC name FROM students")
except sqlite3.Error as error:
    print(f"Caught database error ({type(error).__name__}): {error}")
finally:
    if connection is not None:
        connection.close()
