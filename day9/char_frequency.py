# ASSIGNMENT
# 2 char_frequency.py — count how often each character appears in a string

frequency ={}

text = input("Enter the Text: ")

for char in text:
    if char not in frequency:
       frequency[char] = 1

    else:
      frequency[char] = frequency[char] + 1
        
   
print(frequency)