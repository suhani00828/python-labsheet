t = tuple(input('Items: ').split())
print(tuple((x for x in dict.fromkeys(t) if t.count(x) > 1)))
