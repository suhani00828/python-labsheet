data = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
result = {}
for key, value in data.items():
    if value not in result.values():
        result[key] = value
print(result)
