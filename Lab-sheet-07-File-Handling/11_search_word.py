# Search for a word without considering letter case.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
word = input("Word to search: ").strip()
try:
    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()
    if word and word.casefold() in content.casefold():
        print(f"'{word}' was found.")
    else:
        print(f"'{word}' was not found.")
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
