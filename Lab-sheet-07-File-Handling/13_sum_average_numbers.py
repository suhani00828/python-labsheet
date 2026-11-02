# Read one number per line and calculate the sum and average.
from pathlib import Path

file_path = Path(__file__).with_name("numbers.txt")
try:
    with file_path.open("r", encoding="utf-8") as file:
        numbers = [float(line.strip()) for line in file if line.strip()]
    if numbers:
        print("Sum:", sum(numbers))
        print("Average:", sum(numbers) / len(numbers))
    else:
        print("The file contains no numbers.")
except FileNotFoundError:
    print(f"Create {file_path.name} with one number per line.")
except ValueError:
    print("The file contains a value that is not a number.")
