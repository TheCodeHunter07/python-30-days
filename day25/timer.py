# ASSIGNMENT
# 3 timer.py — a decorator that prints how long a function took

import time


def timer(function):

    def wrapper():

        start = time.time()

        function()

        end = time.time()

        total_time = end - start

        print("Time taken:", total_time, "seconds")

    return wrapper


@timer
def calculate():

    total = 0

    for number in range(10000):
        total = total + number

    print("Calculation completed!")


calculate()