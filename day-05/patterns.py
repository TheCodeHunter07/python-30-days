# Day 5 — Stretch Assignment: patterns.py  — nested loops for a pyramid, an inverted pyramid and a number triangle.


# According to Day 5 plan, this file should print three patterns:

# A pyramid
# An inverted pyramid
# A number triangle

# Task 1: Pyramid pattern

for i in range(1, 5):

    for j in range(1, 5 - i):
        print(" ", end="")

    for k in range(1, 2 * i):
        print("*", end="")

    print()


print("\n")  # Space between patterns

 # Task 2:Inverted Pyramid

for i in range(1, 5):

    for j in range(1, i):
        print(" ", end="")

    for k in range(1, 10 - 2 * i):
        print("*", end="")

    print()

print("\n")  # Space between patterns

  # Task 3: Number Triangle

for i in range(1, 5):

    for j in range(1, i + 1):
        print(j, end="")

    print()