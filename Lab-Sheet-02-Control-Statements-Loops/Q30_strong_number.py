n = int(input('Non-negative integer: '))
total = 0
for ch in str(max(0, n)):
    f = 1
    for i in range(2, int(ch) + 1):
        f *= i
    total += f
print('Strong number' if n >= 0 and total == n else 'Not a strong number')
