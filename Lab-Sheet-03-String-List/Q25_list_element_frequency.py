items = input('Items separated by spaces: ').split()
freq = {}
for x in items:
    freq[x] = freq.get(x, 0) + 1
print(freq)
