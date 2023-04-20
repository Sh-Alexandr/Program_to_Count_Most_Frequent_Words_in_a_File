from collections import Counter

words = []
with open("text.txt", "r", encoding="utf-8") as f:
    for line in f:
        words.extend(line.split())


counts = Counter(words)
top5 = counts.most_common(5)
print(top5)