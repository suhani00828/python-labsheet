# Count whitespace-separated words in a text file.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        word_count = sum(len(line.split()) for line in file)
    print("Word count:", word_count)
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
