# Collect lines from the user until a blank line is entered.
from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
print("Enter lines; press Enter on a blank line to finish.")
lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)
with file_path.open("w", encoding="utf-8") as file:
    file.write("\n".join(lines) + ("\n" if lines else ""))
print(f"Saved {len(lines)} line(s) to {file_path.name}.")
