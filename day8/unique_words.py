# ASSIGNMENT
# 3 unique_words.py — print the unique words of a paragraph in alphabetical order

paragraph = "Python is easy to learn. Python is powerful and Python is popular. Learning Python helps developers build useful applications."

unique_words = set(paragraph.split())

print(unique_words)

sorted_words = sorted(unique_words)

for word in sorted_words:
    print(word)