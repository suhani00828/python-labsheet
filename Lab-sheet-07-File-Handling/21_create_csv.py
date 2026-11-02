# Create a CSV file of student names and marks.
from pathlib import Path
import csv

csv_path = Path(__file__).with_name("students.csv")
records = [["Name", "Marks"], ["Asha", 85], ["Ravi", 78], ["Neha", 92]]
with csv_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(records)
print(f"Created {csv_path.name} with {len(records) - 1} student records.")
