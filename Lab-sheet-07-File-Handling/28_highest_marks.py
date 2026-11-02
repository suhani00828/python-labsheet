# Find and display the student with the highest marks.
from pathlib import Path
import csv

csv_path = Path(__file__).with_name("students.csv")
try:
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))
    valid = []
    for row in records:
        try:
            valid.append((float(row["Marks"]), row["Name"]))
        except (KeyError, ValueError):
            continue
    if valid:
        marks, name = max(valid)
        print(f"Highest marks: {name} - {marks:g}")
    else:
        print("No valid student marks found.")
except FileNotFoundError:
    print(f"Create {csv_path.name} first.")
