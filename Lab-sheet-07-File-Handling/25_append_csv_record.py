# Append a student name and marks as a new CSV row.
from pathlib import Path
import csv

csv_path = Path(__file__).with_name("students.csv")
name = input("Student name: ").strip()
try:
    marks = float(input("Marks: "))
    with csv_path.open("a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([name, marks])
    print("Record appended.")
except ValueError:
    print("Marks must be numeric.")
