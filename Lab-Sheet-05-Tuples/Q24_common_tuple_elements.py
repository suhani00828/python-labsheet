a = tuple(input('First tuple: ').split())
b = tuple(input('Second tuple: ').split())
print(tuple((x for x in a if x in b)))
