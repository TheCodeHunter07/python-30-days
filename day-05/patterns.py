# Pattern 1: Pyramid

print("Pattern 1: Pyramid")

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()


# Pattern 2: Inverted Pyramid

print("\nPattern 2: Inverted Pyramid")

for i in range(1, 6):
    for j in range(i - 1):
        print(" ", end="")

    for k in range(9 - 2 * (i - 1)):
        print("*", end="")

    print()


# Pattern 3: Number Triangle

print("\nPattern 3: Number Triangle")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")

    print()