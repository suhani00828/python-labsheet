n = int(input('Integer: '))
prime = n >= 2
for d in range(2, int(n ** 0.5) + 1):
    if n % d == 0:
        prime = False
        break
print('Prime' if prime else 'Not prime')
