data = {'name': 'Aman', 'age': 20}
key = input('Enter key to update (name/age): ')
if key in data:
    value = input('Enter new value: ')
    data[key] = int(value) if key == 'age' else value
    print(data)
else:
    print('Key not found.')
