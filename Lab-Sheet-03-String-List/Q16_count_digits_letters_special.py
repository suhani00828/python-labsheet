s = input('String: ')
digits = sum((ch.isdigit() for ch in s))
letters = sum((ch.isalpha() for ch in s))
print('Digits =', digits, 'Alphabets =', letters, 'Special characters =', len(s) - digits - letters)
