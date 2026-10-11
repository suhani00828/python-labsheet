b = float(input('Base: '))
e = int(input('Non-negative exponent: '))
result = 1
if e < 0:
    print('Exponent must be non-negative')
else:
    for _ in range(e):
        result *= b
    print('Power =', result)
