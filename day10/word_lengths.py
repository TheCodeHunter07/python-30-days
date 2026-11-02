# ASSIGNMENT
# Stretch: word_lengths.py — build a {word: length} dictionary for a sentence with a comprehension.

sentence = ("Python makes coding fun")

words = sentence.split()

word_lengths = {word: len(word) for word in words}

print(word_lengths)