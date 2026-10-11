t = tuple(input('Items: ').split())
x = input('Find index of: ')
print('Index =', t.index(x) if x in t else 'Item not found')
