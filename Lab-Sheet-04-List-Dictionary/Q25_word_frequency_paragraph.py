import re
paragraph = input('Enter a paragraph: ').lower()
words = re.findall('\\b\\w+\\b', paragraph)
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)
