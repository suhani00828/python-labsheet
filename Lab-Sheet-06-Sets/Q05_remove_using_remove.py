s = {1, 2, 3}
x = int(input('Item to remove: '))
if x in s:
    s.remove(x)
    print(s)
else:
    print('Item not found')
