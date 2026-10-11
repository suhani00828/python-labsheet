a = sorted(input('First string: ').replace(' ', '').lower())
b = sorted(input('Second string: ').replace(' ', '').lower())
print('Anagrams' if a == b else 'Not anagrams')
