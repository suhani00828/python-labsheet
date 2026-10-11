m = float(input('Marks (0-100): '))
print('Invalid marks' if not 0 <= m <= 100 else 'A' if m >= 90 else 'B' if m >= 75 else 'C' if m >= 50 else 'F')
