# ASSIGNMENT
# 2 even_squares.py — squares of even numbers from 1 to 50 in a single comprehension


even_squares = [numbers**2 for numbers in range(1,51) if numbers % 2 == 0]
print(even_squares)