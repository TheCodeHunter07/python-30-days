# Stretch: Use filter and lambda to extract all palindromes from a list of words.

words = ["madam", "python", "level", "hello", "radar", "world"]

result = filter(lambda word: word == word[::-1] , words)

print(list(result))