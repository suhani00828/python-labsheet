# Append a new line without replacing existing file content.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
text = input("Enter text to append: ")
with file_path.open("a", encoding="utf-8") as file:
    file.write(text + "\n")
print(f"Text appended to {file_path.name}.")
