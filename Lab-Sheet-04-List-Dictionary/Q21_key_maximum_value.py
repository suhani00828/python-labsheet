data = {'Aman': 78, 'Riya': 92, 'Karan': 65}
if data:
    key = max(data, key=lambda item: data[item])
    print('Key with maximum value =', key, 'Value =', data[key])
