a = tuple(map(int, input('First tuple integers: ').split()))
b = tuple(map(int, input('Second tuple integers: ').split()))
print(tuple((x + y for x, y in zip(a, b))) if len(a) == len(b) else 'Tuples must have equal lengths')
