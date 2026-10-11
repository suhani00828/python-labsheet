a = input('First string: ').replace(' ', '').lower()
b = input('Second string: ').replace(' ', '').lower()
print('Anagrams' if set(a) == set(b) and sorted(a) == sorted(b) else 'Not anagrams')
