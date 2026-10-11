a = abs(int(input('First integer: ')))
b = abs(int(input('Second integer: ')))
hcf = 0
for d in range(1, min(a, b) + 1):
    if a % d == 0 and b % d == 0:
        hcf = d
print('HCF =', hcf if a and b else max(a, b))
