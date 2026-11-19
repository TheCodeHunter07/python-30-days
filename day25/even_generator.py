# ASSIGNMENT
# 1 even_generator.py — a generator that yields even numbers up to a limit


# Using if and modulo % 

def even_generator(limit):

    number = 1

    while number <= limit:

        if number % 2 == 0:
            yield number

        number = number + 1


for number in even_generator(10):
    print(number)



# Approach 2: Without if and modulo %


def even_generator(limit):

    number = 2

    while number <= limit:

        yield number

        number = number + 2


# Calling the generator
for number in even_generator(10):
    print(number)


