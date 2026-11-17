# ASSIGNMENT
# 1 average.py — a function that accepts any number of values and returns their average

def calculate_average(*args):

    if len(args) == 0:
        return 0

    average = sum(args) / len(args)

    return average
print(calculate_average(10, 20, 30, 40))  # 25.0
print(calculate_average(5, 15))           # 10.0
print(calculate_average(10, 20, 30))      # 20.0