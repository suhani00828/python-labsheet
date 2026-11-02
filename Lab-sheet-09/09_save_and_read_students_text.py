# Store student rows in a simple comma-separated text file and read them back.
from pathlib import Path

file_path = Path(__file__).with_name("students.txt")
students = [(101, "Asha", 85), (102, "Ravi", 78)]
try:
    with file_path.open("w", encoding="utf-8") as file:
        for roll, name, marks in students:
            file.write(f"{roll},{name},{marks}\n")
    print("Saved student data.")
    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            roll, name, marks = line.rstrip("\n").split(",")
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
except OSError as error:
    print("File error:", error)
