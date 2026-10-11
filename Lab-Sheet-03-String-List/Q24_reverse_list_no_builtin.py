items = input('Items separated by spaces: ').split()
out = []
for x in items:
    out.insert(0, x)
print(out)
