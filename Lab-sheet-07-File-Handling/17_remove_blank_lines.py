# Remove empty or whitespace-only lines from a text file.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()
    nonblank = [line for line in lines if line.strip()]
    with file_path.open("w", encoding="utf-8") as file:
        file.writelines(nonblank)
    print(f"Removed {len(lines) - len(nonblank)} blank line(s).")
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
