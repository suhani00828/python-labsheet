# Display the Name and Marks columns from the student CSV file.
from pathlib import Path
import csv

csv_path = Path(__file__).with_name("students.csv")
try:
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or not {"Name", "Marks"}.issubset(reader.fieldnames):
            print("CSV must have Name and Marks headers.")
        else:
            for row in reader:
                print(f"{row['Name']} | {row['Marks']}")
except FileNotFoundError:
    print(f"Create {csv_path.name} first.")
