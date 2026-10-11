n = int(input('Enter n: '))
if n < 1:
    print('Enter a positive integer.')
else:
    print([number ** 2 for number in range(1, n + 1)])
