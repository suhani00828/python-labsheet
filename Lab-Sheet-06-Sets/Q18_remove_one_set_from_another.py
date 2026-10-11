a = set(input('Main set items: ').split())
b = set(input('Items to remove: ').split())
a.difference_update(b)
print(a)
