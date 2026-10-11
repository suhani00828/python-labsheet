a = set(input('First set items: ').split())
b = set(input('Second set items: ').split())
print({(x, y) for x in a for y in b})
