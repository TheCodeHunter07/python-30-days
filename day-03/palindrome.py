# Task: check whether a word reads the same backwards.

# Task: Check whether a word is a palindrome



word = input("Enter a word: ")

reversed_word = word[::-1]

print(f"Original word: {word}")
print(f"Reversed word: {reversed_word}")
print(f"Is it a palindrome? : {word == reversed_word}")