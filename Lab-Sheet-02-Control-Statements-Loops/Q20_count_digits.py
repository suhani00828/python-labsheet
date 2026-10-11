n = abs(int(input('Integer: ')))
count = 1 if n == 0 else 0
while n:
    count += 1
    n //= 10
print('Digits =', count)
