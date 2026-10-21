# task: Create day-05/sum_digits.py.  -sum the digits of a number using a while loop

# Write a program that asks the user for a positive integer and calculates the sum of its digits using a while loop.


number = int(input("Enter the positive integer: "))

total = 0

while number > 0:

    digit = number % 10 
    total += digit
    number = number // 10

     

print(f"Sum of digits: {total}")
     
