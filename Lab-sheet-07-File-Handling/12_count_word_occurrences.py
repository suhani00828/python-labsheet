# Count whole-word occurrences, ignoring letter case and punctuation.
from pathlib import Path
import re

file_path = Path(__file__).with_name("sample.txt")
word = input("Word to count: ").strip()
try:
    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()
    count = len(re.findall(r"\b" + re.escape(word) + r"\b", content, flags=re.IGNORECASE)) if word else 0
    print(f"'{word}' occurs {count} time(s).")
except FileNotFoundError:
    print(f"Create {file_path.name} first.")
