import string
s = input('String: ')
print(''.join((ch for ch in s if ch not in string.punctuation)))
