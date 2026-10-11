a = abs(int(input('First integer: ')))
b = abs(int(input('Second integer: ')))
if a == 0 or b == 0:
    print('LCM = 0')
else:
    candidate = max(a, b)
    while candidate % a != 0 or candidate % b != 0:
        candidate += 1
    print('LCM =', candidate)
