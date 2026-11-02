# Assignment
# Stretch: vowel_checker.py — find which vowels do and do not appear in a sentence.

sentence = "Python programming is fun"
vowels = {"a", "e", "i", "o", "u"}

characters = set(sentence.lower())

print(characters)

present_vowels = characters.intersection(vowels)
missing_vowels =  vowels - characters



print(present_vowels)
print(missing_vowels)
