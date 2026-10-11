s = input('String: ')
t = s.replace(' ', '').lower()
print('Palindrome' if t == t[::-1] else 'Not palindrome')
