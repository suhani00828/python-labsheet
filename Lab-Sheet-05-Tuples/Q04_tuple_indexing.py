t = ('red', 'green', 'blue')
i = int(input('Index: '))
print(t[i] if -len(t) <= i < len(t) else 'Index out of range')
