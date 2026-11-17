# ASSIGNMENT
# 3 Refactor your Day 5 number-guessing game into functions

import random

def generate_number():

    random_number = random.randint(1, 100)
    return random_number

def check_guess(guess, random_number):

    if guess > random_number:
        return "high"

    elif guess < random_number:
        return "low"

    else:
        return "correct"

def play_game():
    random_number = generate_number()

    attempt = 0
    total_attempts = 3

    while attempt < total_attempts:

        number = int(input("Guess the number between 1 and 100: "))
        attempt += 1

        result = check_guess(number, random_number)

        return result

    if result == "high":
       print("Too high!")

    elif result == "low":
        print("Too low!")

    elif result == "correct":
        print("Success!")
  
    else:
        print("Not found")
    
        