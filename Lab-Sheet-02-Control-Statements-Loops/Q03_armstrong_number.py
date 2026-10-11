n = int(input('Non-negative integer: '))
s = str(n)
print('Armstrong' if n >= 0 and sum((int(d) ** len(s) for d in s)) == n else 'Not Armstrong')
