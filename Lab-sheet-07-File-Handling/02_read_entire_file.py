# Read and display all text from a file.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
