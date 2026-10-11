nested = [[int(x) for x in group.split(',') if x.strip()] for group in input('Enter groups separated by spaces; numbers in each group separated by commas (e.g. 1,2 3,4): ').split()]
flat = [item for group in nested for item in group]
print('Flattened list =', flat)
