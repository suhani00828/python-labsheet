# Combine the contents of two text files into a third file.
from pathlib import Path

folder = Path(__file__).parent
first = folder / "first.txt"
second = folder / "second.txt"
merged = folder / "merged.txt"
try:
    with first.open("r", encoding="utf-8") as file:
        first_text = file.read()
    with second.open("r", encoding="utf-8") as file:
        second_text = file.read()
    with merged.open("w", encoding="utf-8") as file:
        file.write(first_text)
        if first_text and not first_text.endswith("\n"):
            file.write("\n")
        file.write(second_text)
    print(f"Merged files into {merged.name}.")
except FileNotFoundError as error:
    print(f"Missing input file: {Path(error.filename).name}")
