s = input('Sentence: ')
words = s.split()
print(' '.join((w[:1].upper() + w[1:].lower() for w in words)))
