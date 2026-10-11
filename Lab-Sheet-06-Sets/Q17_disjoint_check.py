a = set(input('First set items: ').split())
b = set(input('Second set items: ').split())
print('Disjoint' if a.isdisjoint(b) else 'Not disjoint')
