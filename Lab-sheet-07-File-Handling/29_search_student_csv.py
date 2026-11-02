# Search the CSV for a student name, ignoring letter case.
from pathlib import Path
import csv

csv_path = Path(__file__).with_name("students.csv")
search_name = input("Student name to find: ").strip().casefold()
try:
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        matches = [row for row in csv.DictReader(file) if row.get("Name", "").strip().casefold() == search_name]
    if matches:
        for row in matches:
            print(row)
    else:
        print("No matching student found.")
except FileNotFoundError:
    print(f"Create {csv_path.name} first.")
