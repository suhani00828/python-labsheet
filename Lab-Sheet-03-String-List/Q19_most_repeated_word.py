from collections import Counter
import re
words = re.findall('\\b\\w+\\b', input('Sentence: ').lower())
counts = Counter(words)
print(counts.most_common(1)[0] if counts else 'No words')
