"""Program 18: Display all records sorted by student name.
Output: records in A-Z order of name.
"""
import sqlite3
conn = None
try:
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY name ASC")
    rows = cur.fetchall()
    if not rows: print("No records found.")
    for r in rows:
        print(f"ID: {r[0]}, Name: {r[1]}, Age: {r[2]}, Marks: {r[3]}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn: conn.close()
