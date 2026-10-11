data = {'name': 'Aman', 'age': 20, 'course': 'MCA'}
key = input('Enter key to remove: ')
if key in data:
    del data[key]
    print(data)
else:
    print('Key not found.')
