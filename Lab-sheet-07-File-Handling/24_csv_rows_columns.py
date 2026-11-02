# Count CSV data rows and columns (the first row is treated as a header).
from pathlib import Path
import csv

csv_path = Path(__file__).with_name("students.csv")
try:
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    print("Data rows:", max(0, len(rows) - 1))
    print("Columns:", max((len(row) for row in rows), default=0))
except FileNotFoundError:
    print(f"Create {csv_path.name} first.")
