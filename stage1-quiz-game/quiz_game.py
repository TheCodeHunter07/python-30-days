import random

questions = [
    {
        "question": "Which keyword defines a function in Python?",
        "answer": "def"
    },
    {
        "question": "Which data type is immutable?",
        "answer": "tuple"
    },
    {
        "question": "Which keyword is used to create a loop that continues while a condition is true?",
        "answer": "while"
    },
    {
        "question": "Which function is used to display output in Python?",
        "answer": "print"
    },
    {
        "question": "Which function is used to accept input from the user?",
        "answer": "input"
    },
    {
        "question": "Which operator returns the remainder of a division?",
        "answer": "%"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "answer": "dictionary"
    },
    {
        "question": "Which keyword is used to exit a loop immediately?",
        "answer": "break"
    },
    {
        "question": "Which list method adds an item to the end of a list?",
        "answer": "append"
    },
    {
        "question": "Which keyword is used to check another condition after an if statement?",
        "answer": "elif"
    }
]

running = True

while running:
    score = 0
    random.shuffle(questions)

    for question in questions:

        print(question["question"])

        answer = input("Enter the answer: ")

        if question["answer"].lower() == answer.lower():
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect answer!")

    print(f"Total score is out of {len(questions)}: {score}")

    percentage = score * 100 / len(questions)

    print(f"Percentage: {percentage}")

    if percentage >= 80:
        print("Excellent work!")
    elif percentage >= 50:
        print("Good effort! Keep practising.")
    else:
        print("Keep learning and try again!")

    while True:
        play_again = input("Play again? (y/n): ").lower()

        if play_again == "y":
            break

        elif play_again == "n":
            running = False
            break

        else:
            print("Please enter y or n.")