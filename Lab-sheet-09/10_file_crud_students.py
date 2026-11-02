# Add, view, modify, and delete records in a text file.
from pathlib import Path

file_path = Path(__file__).with_name("student_records.txt")

def read_records():
    """Read records stored as roll|name|marks lines."""
    if not file_path.exists():
        return []
    with file_path.open("r", encoding="utf-8") as file:
        records = []
        for line in file:
            parts = line.rstrip("\n").split("|", 2)
            if len(parts) == 3:
                records.append({"roll": parts[0], "name": parts[1], "marks": parts[2]})
        return records

def save_records(records):
    """Write all current records back to the file."""
    with file_path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(f"{record['roll']}|{record['name']}|{record['marks']}\n")

while True:
    print("\n1 Add  2 View  3 Modify marks  4 Delete  5 Exit")
    choice = input("Choose: ").strip()
    try:
        records = read_records()
        if choice == "1":
            roll = input("Roll number: ").strip()
            if any(row["roll"] == roll for row in records):
                print("Roll number already exists.")
            else:
                records.append({"roll": roll, "name": input("Name: ").strip(), "marks": str(float(input("Marks: ")))})
                save_records(records)
                print("Record added.")
        elif choice == "2":
            print(*records, sep="\n") if records else print("No records.")
        elif choice == "3":
            roll = input("Roll number: ").strip()
            row = next((row for row in records if row["roll"] == roll), None)
            if row:
                row["marks"] = str(float(input("New marks: ")))
                save_records(records)
                print("Record updated.")
            else:
                print("Record not found.")
        elif choice == "4":
            roll = input("Roll number: ").strip()
            updated = [row for row in records if row["roll"] != roll]
            if len(updated) < len(records):
                save_records(updated)
                print("Record deleted.")
            else:
                print("Record not found.")
        elif choice == "5":
            break
        else:
            print("Choose an option from 1 to 5.")
    except (OSError, ValueError) as error:
        print("Could not complete the operation:", error)
