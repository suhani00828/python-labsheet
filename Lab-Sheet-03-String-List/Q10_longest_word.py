words = input('Sentence: ').split()
print('Longest word =', max(words, key=len) if words else 'No words')
