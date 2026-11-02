# Display lines numbered 2, 4, 6, and so on.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            if number % 2 == 0:
                print(f"{number}: {line.rstrip()}")
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
