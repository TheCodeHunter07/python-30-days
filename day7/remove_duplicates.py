# Assignment 3: remove_duplicates.py — remove duplicates while keeping the original order

numbers = [10, 20, 10, 30, 20, 40, 10, 50]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
       unique_numbers.append(number)

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)
