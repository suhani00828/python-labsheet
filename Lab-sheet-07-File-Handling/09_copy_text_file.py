# Copy all text from one file into another.
from pathlib import Path

folder = Path(__file__).parent
source = folder / "sample.txt"
destination = folder / "copy.txt"
try:
    with source.open("r", encoding="utf-8") as source_file:
        content = source_file.read()
    with destination.open("w", encoding="utf-8") as destination_file:
        destination_file.write(content)
    print(f"Copied {source.name} to {destination.name}.")
except FileNotFoundError:
    print(f"Create {source.name} first.")
