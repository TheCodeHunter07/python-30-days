# ASSIGNMENT
# 3 recursion.py — recursive factorial, sum of a list, and string reversal


# recursive factorial

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))  
print(factorial(4))  
print(factorial(3))  

# sum of a list

def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + recursive_sum(numbers[1:])


print(recursive_sum([5, 10, 15]))

# string reversal

def reverse_string(word):

    if len(word) == 0:
        return ""

    return word[-1] +  reverse_string(word[:-1])

print(reverse_string("java"))