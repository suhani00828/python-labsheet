# Combine CSV files whose names match input_*.csv into combined.csv.
from pathlib import Path
import csv

folder = Path(__file__).parent
sources = sorted(folder.glob("input_*.csv"))
destination = folder / "combined.csv"
if not sources:
    print("Add source CSV files named input_1.csv, input_2.csv, etc.")
else:
    header = None
    total = 0
    try:
        with destination.open("w", newline="", encoding="utf-8") as output_file:
            writer = csv.writer(output_file)
            for source in sources:
                with source.open("r", newline="", encoding="utf-8") as input_file:
                    reader = csv.reader(input_file)
                    current_header = next(reader, None)
                    if header is None:
                        header = current_header
                        if header:
                            writer.writerow(header)
                    elif current_header != header:
                        print(f"Skipped {source.name}: header differs.")
                        continue
                    for row in reader:
                        writer.writerow(row)
                        total += 1
        print(f"Combined {total} data row(s) from {len(sources)} file(s) into {destination.name}.")
    except OSError as error:
        print("Could not process CSV files:", error)
