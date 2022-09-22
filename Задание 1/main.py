import random

t = input()
words = t.split()
adhoc = random.sample(words, len(words))
alphabetically = sorted(words, key=str.lower)
as_in_text = words
print(adhoc)
print(alphabetically)
print(as_in_text)

