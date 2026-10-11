s = {1, 2, 3}
items = map(int, input('Integers to add separated by spaces: ').split())
s.update(items)
print(s)
