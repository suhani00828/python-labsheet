n = abs(int(input('Integer: ')))
total = 0
while n:
    total += n % 10
    n //= 10
print('Sum of digits =', total)
