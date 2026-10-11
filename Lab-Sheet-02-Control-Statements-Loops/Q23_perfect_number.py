n = int(input('Positive integer: '))
total = sum((d for d in range(1, n) if n % d == 0))
print('Perfect' if n > 0 and total == n else 'Not perfect')
