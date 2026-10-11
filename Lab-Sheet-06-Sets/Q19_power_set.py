from itertools import combinations
s = set(input('Items: ').split())
items = list(s)
power = [set(combination) for size in range(len(items) + 1) for combination in combinations(items, size)]
print(power)
