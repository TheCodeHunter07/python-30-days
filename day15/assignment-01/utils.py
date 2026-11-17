# ASSIGNMENT
# 1 Move your Day 13 functions into utils.py and import them from main.py

# Task 1: is_prime(n)

def is_prime(n):
    """Check whether a number is prime."""
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True



# Task 2: factorial(n)

def factorial(n):
    """Calculate and return the factorial of a number."""

    result = 1

    if n == 0:
       return 1

    for i in range(1,n+1):

        result = result * i

    return result



# Task 3: fibonacci(n)
# The Fibonacci sequence is a sequence where each number is the sum of the previous two numbers.

def fibonacci(n):
    """Generate the first n Fibonacci numbers."""

    a = 0
    b = 1
    sequence = []

    for i in range(n):
        sequence.append(a)

        a,b = b, a+b

    return sequence





# Task 4: gcd(a, b)
# GCD (Greatest Common Divisor) is the largest number that divides two numbers without leaving a remainder.


def gcd(a, b):

    """Calculate the greatest common divisor of two numbers."""

    while b != 0:

      remainder = a % b
      a = b
      b = remainder

    return a


