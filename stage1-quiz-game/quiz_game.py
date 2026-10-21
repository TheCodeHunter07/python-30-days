# DAY 6
# STAGE PROJECT · Quiz Game
# Build a command-line quiz game.
# REQUIREMENTS
# • At least 10 questions on any topic you like
# • Ask each question, check the answer and keep score
# • Answers are case-insensitive (Python equals python)
# • Show the final score and percentage
# • Print a message based on the score, e.g. "Excellent" or "Keep practising"
# • Ask "Play again? (y/n)" at the end
# Submit: stage1-quiz-game/ with a README

print("=" * 32)
print("   WELCOME TO QUIZ GAME   ")
print("=" * 32)

print("Test your Python knowledge!")
print("Let's begin!")

quiz = {
    "What keyword is used to define a function in Python?": "def",
    "Which data type stores True or False?": "bool",
    "Which loop repeats while a condition is true?": "while",
    "What data type stores whole numbers?": "int",
    "What data type stores text?": "str",
    "Which function accepts user input?": "input",
    "Which keyword checks a condition?": "if",
    "Which operator checks equality?": "==",
    "Which function generates a sequence of numbers?": "range",
    "Which keyword terminates a loop?": "break"
}

choice = "y"

while choice == "y":

    score = 0

    for question in quiz:

        print(question)
        answer = input("Enter the answer: ")

        if answer.lower() == quiz[question].lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")

    print(f"\nYour final score: {score}/{len(quiz)}")

    percentage = (score / len(quiz)) * 100

    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent work!")

    elif percentage >= 50:
        print("Good effort! Keep practising.")

    else:
        print("Keep learning and try again!")

    while True:
        choice = input("\nPlay again? (y/n): ").lower()

        if choice == "y":
            break

        elif choice == "n":
            break

        else:
            print("Please enter y or n.")

print("\nThanks for playing!")




