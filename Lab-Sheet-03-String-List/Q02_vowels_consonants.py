s = input('String: ')
v = c = 0
for ch in s.lower():
    if ch.isalpha():
        if ch in 'aeiou':
            v += 1
        else:
            c += 1
print('Vowels =', v, 'Consonants =', c)
