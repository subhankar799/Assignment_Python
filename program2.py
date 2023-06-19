from collections import Counter


with open('sentence.txt', 'r') as file:
    text = file.read()
    words = text.split()

word_counts = Counter(words)

output = [{'word':word, 'count': count} for word, count in word_counts.items()]
print(output)
