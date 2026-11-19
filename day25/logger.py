# ASSIGNMENT
# 4 logger.py — a decorator that logs every call and its arguments

def logger(function):

    def wrapper(*args, **kwargs):

        print("Function called:", function.__name__)
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)

        result = function(*args, **kwargs)

        return result

    return wrapper


@logger
def greet(name):
    print(f"Hello, {name}!")


@logger
def add(a, b):
    print("Sum:", a + b)


@logger
def welcome():
    print("Welcome!")


greet("Sumit")
add(10, 20)
welcome()