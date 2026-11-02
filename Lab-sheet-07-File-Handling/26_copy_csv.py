# Copy all rows from one CSV file into another.
from pathlib import Path
import csv

folder = Path(__file__).parent
source = folder / "students.csv"
destination = folder / "students_copy.csv"
try:
    with source.open("r", newline="", encoding="utf-8") as source_file:
        rows = list(csv.reader(source_file))
    with destination.open("w", newline="", encoding="utf-8") as destination_file:
        csv.writer(destination_file).writerows(rows)
    print(f"Copied {source.name} to {destination.name}.")
except FileNotFoundError:
    print(f"Create {source.name} first.")
