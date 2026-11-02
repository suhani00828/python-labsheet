# Display the first and last lines of a text file.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()
    if lines:
        print("First line:", lines[0].rstrip())
        print("Last line:", lines[-1].rstrip())
    else:
        print("The file is empty.")
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
