# Count lines and characters in a text file.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()
    print("Lines:", len(content.splitlines()))
    print("Characters:", len(content))
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
