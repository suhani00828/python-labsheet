t = tuple(input('Words: ').split())
print(max((len(w) for w in t), default=0))
