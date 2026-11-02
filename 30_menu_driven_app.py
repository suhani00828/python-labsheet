# Program 30: Menu-driven student management application
import sqlite3

DB_NAME = "student_db.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    conn.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, age INTEGER, marks REAL)""")
    conn.commit()
    conn.close()

def add_student():
    try:
        name = input("Name: ").strip()
        age = int(input("Age: "))
        marks = float(input("Marks: "))
    except ValueError:
        print("Invalid input. Age must be an integer and marks a number.")
        return
    conn = get_connection()
    try:
        conn.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                     (name, age, marks))
        conn.commit()
        print("Student added.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def view_students():
    conn = get_connection()
    try:
        rows = conn.execute("SELECT id, name, age, marks FROM students").fetchall()
        if not rows:
            print("No records found.")
            return
        print(f"{'ID':<5}{'Name':<14}{'Age':<6}{'Marks'}")
        for r in rows:
            print(f"{r[0]:<5}{r[1]:<14}{r[2]:<6}{r[3]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def update_student():
    try:
        sid = int(input("ID of student to update: "))
        name = input("New name (blank = keep): ").strip()
        marks_txt = input("New marks (blank = keep): ").strip()
    except ValueError:
        print("Invalid ID.")
        return
    conn = get_connection()
    try:
        if name:
            conn.execute("UPDATE students SET name = ? WHERE id = ?", (name, sid))
        if marks_txt:
            conn.execute("UPDATE students SET marks = ? WHERE id = ?", (float(marks_txt), sid))
        conn.commit()
        print("Update done (if the ID exists).")
    except (sqlite3.Error, ValueError) as e:
        print("Error:", e)
    finally:
        conn.close()

def delete_student():
    try:
        sid = int(input("ID of student to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    conn = get_connection()
    try:
        cur = conn.execute("DELETE FROM students WHERE id = ?", (sid,))
        conn.commit()
        print("Deleted." if cur.rowcount else "No student with that ID.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def main():
    init_db()
    while True:
        print("\n===== Student Management =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
