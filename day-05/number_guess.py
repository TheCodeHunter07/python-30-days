
# Task:  — guess a random number (import random) with too-high / too-low hints; count the attempts


import random

random_number = random.randint(1, 100)

attempt = 0
total_attempts = 3
guessed_correctly = False

while attempt < total_attempts:

    number = int(input("Guess the number between 1 and 100: "))
    attempt += 1

    if number > random_number:
        print("Too high!")

    elif number < random_number:
        print("Too low!")

    else:
        guessed_correctly = True
        print(f"Correct! You guessed the number in {attempt} attempts.")
        break

if not guessed_correctly:
    print(f"Game over! The correct number was {random_number}.")


 





 

