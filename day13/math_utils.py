# ASSIGNMENT
# 1 math_utils.py — is_prime(n), factorial(n), fibonacci(n) and gcd(a, b), each with a docstring

# Task 1: is_prime(n)

def is_prime(n):
    """Check whether a number is prime."""
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(7))
print(is_prime(10))
print(is_prime(2))
print(is_prime(1))
print(is_prime(13))

# Task 2: factorial(n)

def factorial(n):
    """Calculate and return the factorial of a number."""

    result = 1

    if n == 0:
       return 1

    for i in range(1,n+1):

        result = result * i

    return result

print(factorial(5))  # 120
print(factorial(4))  # 24
print(factorial(0))  # 1
print(factorial(6))  # 720

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


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(7))



# Task 4: gcd(a, b)
# GCD (Greatest Common Divisor) is the largest number that divides two numbers without leaving a remainder.


def gcd(a, b):

    """Calculate the greatest common divisor of two numbers."""

    while b != 0:

      remainder = a % b
      a = b
      b = remainder

    return a


print(gcd(18, 12))
print(gcd(48, 18))
print(gcd(20, 15))