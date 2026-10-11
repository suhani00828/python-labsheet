items = input('Enter items separated by spaces: ').split()
result = ''
for item in items:
    if result:
        result += ' '
    result += item
print('String =', result)
