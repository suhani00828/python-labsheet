# Create a text file and write user supplied text into it.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
text = input("Enter text to save: ")
with file_path.open("w", encoding="utf-8") as file:
    file.write(text + "\n")
print(f"Text saved to {file_path.name}.")
