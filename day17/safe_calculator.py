# ASSIGNMENT
# 1 safe_calculator.py — a calculator that never crashes on bad input or division by zero


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


while True:

    print("\n--- CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Choose the operation: "))


        if choice == 5:
            print("Calculator closed.")
            break

        num1 = int(input("Enter the first number: "))

        num2 = int(input("Enter the second number: "))


        if choice == 1:
            result = addition(num1, num2)

        elif choice == 2:
            result = subtraction(num1, num2)

        elif choice == 3:
            result = multiplication(num1, num2)

        elif choice == 4:
            result = division(num1, num2)

        else:
            print("Invalid operation!")
            continue

    except ZeroDivisionError:
           print("Cannot divide by zero!")

    except ValueError:
        print("Please enter valid numbers!")

    else:
        print("Result:", result)
        
    finally:
        print("Calculator execution completed.")


        

                 


  

