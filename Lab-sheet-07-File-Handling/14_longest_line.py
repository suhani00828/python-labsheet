# Display the longest line in a text file.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()
    if lines:
        longest = max(lines, key=len)
        print("Longest line:", longest.rstrip())
        print("Length:", len(longest.rstrip("\r\n")))
    else:
        print("The file is empty.")
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
