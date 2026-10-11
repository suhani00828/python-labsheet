t = tuple(input('Items: ').split())
out = tuple(dict.fromkeys(t))
print(out)
