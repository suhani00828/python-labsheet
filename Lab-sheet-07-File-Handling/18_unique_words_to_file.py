# Store each distinct word from a text file in a second file.
from pathlib import Path
import re

folder = Path(__file__).parent
source = folder / "sample.txt"
destination = folder / "unique_words.txt"
try:
    with source.open("r", encoding="utf-8") as file:
        words = re.findall(r"\b\w+\b", file.read())
    unique = list(dict.fromkeys(word.casefold() for word in words))
    with destination.open("w", encoding="utf-8") as file:
        file.write("\n".join(unique) + ("\n" if unique else ""))
    print(f"Saved {len(unique)} unique word(s) to {destination.name}.")
except FileNotFoundError:
    print(f"Create {source.name} first.")
