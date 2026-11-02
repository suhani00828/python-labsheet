# Read and display every row in a CSV file.
from pathlib import Path
import csv

csv_path = Path(__file__).with_name("students.csv")
try:
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            print(" | ".join(row))
except FileNotFoundError:
    print(f"Create {csv_path.name} first.")
