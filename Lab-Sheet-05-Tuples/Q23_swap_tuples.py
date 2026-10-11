a = tuple(input('First tuple: ').split())
b = tuple(input('Second tuple: ').split())
a, b = (b, a)
print('a =', a, 'b =', b)
