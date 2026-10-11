items = input('Enter list items separated by spaces: ').split()
n = int(input('Rotate right by how many positions? '))
if items:
    n %= len(items)
    rotated = items[-n:] + items[:-n] if n else items[:]
    print('Rotated list =', rotated)
else:
    print('List is empty.')
