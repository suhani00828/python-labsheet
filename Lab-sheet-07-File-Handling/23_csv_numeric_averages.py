# Calculate averages for CSV columns whose data rows are all numeric.
from pathlib import Path
import csv

csv_path = Path(__file__).with_name("students.csv")
try:
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    if len(rows) < 2:
        print("The CSV has no data rows.")
    else:
        for column, heading in enumerate(rows[0]):
            try:
                values = [float(row[column]) for row in rows[1:] if len(row) > column and row[column].strip()]
            except ValueError:
                continue
            if values:
                print(f"{heading} average: {sum(values) / len(values):.2f}")
except FileNotFoundError:
    print(f"Create {csv_path.name} first.")
