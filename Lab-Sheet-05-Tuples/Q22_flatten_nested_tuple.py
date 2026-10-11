t = ((1, 2), (3, 4), (5,))
flat = tuple((x for group in t for x in group))
print(flat)
