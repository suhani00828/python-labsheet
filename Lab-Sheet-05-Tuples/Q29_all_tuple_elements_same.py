t = tuple(input('Items: ').split())
print('All same' if not t or all((x == t[0] for x in t)) else 'Not all same')
