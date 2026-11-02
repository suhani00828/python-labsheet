# Sort words alphabetically and save them to a new file.
from pathlib import Path
import re

folder = Path(__file__).parent
source = folder / "sample.txt"
destination = folder / "sorted_words.txt"
try:
    with source.open("r", encoding="utf-8") as file:
        words = re.findall(r"\b\w+\b", file.read())
    words.sort(key=str.casefold)
    with destination.open("w", encoding="utf-8") as file:
        file.write("\n".join(words) + ("\n" if words else ""))
    print(f"Sorted words saved to {destination.name}.")
except FileNotFoundError:
    print(f"Create {source.name} first.")
