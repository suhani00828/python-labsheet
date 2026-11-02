# Replace whole-word matches in a file and save the changes.
from pathlib import Path
import re

file_path = Path(__file__).with_name("sample.txt")
old_word = input("Word to replace: ")
new_word = input("Replacement word: ")
try:
    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()
    updated = re.sub(r"\b" + re.escape(old_word) + r"\b", lambda _: new_word, content, flags=re.IGNORECASE)
    with file_path.open("w", encoding="utf-8") as file:
        file.write(updated)
    print("File updated.")
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
