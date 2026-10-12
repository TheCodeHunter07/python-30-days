# Stage 1 — CLI Quiz Game

## About the Project

The CLI Quiz Game is a command-line application built using Python. It asks users questions about Python fundamentals, checks their answers, and calculates their final score and percentage.

The game provides feedback based on the user's performance and allows them to play multiple rounds.

## Features

- Contains 10 questions about Python fundamentals.
- Checks answers without considering uppercase or lowercase differences.
- Displays whether each answer is correct or incorrect.
- Calculates the total score and percentage.
- Provides feedback based on the final percentage.
- Randomizes the question order in each round.
- Allows users to play again without restarting the program.
- Validates replay input and accepts `y` or `n`.

## Technologies Used

- Python 3
- Python `random` module

## Project Structure

```text
stage1-quiz-game/
├── quiz_game.py
└── README.md
```

## How to Run

### Prerequisites

Make sure Python 3 is installed on your system.

### Steps

1. Open a terminal.
2. Navigate to the `stage1-quiz-game` directory.
3. Run the following command:

```bash
python quiz_game.py
```

## Python Concepts Practiced

- Variables and data types
- Lists and dictionaries
- `for` loops and `while` loops
- Conditional statements (`if`, `elif`, `else`)
- User input using `input()`
- String methods such as `lower()`
- Arithmetic operations
- Score and percentage calculation
- The `random` module and `random.shuffle()`
- Loop control using `break`
- Boolean variables
- Input validation

## Scoring System

The game calculates the final percentage using the following formula:

```text
Percentage = (Correct Answers / Total Questions) × 100
```

Feedback is provided according to the final percentage:

- **80% or above:** Excellent work!
- **50% to below 80%:** Good effort! Keep practising.
- **Below 50%:** Keep learning and try again!

## Learning Outcomes

Through this project, I practised Python fundamentals by building an interactive command-line application.

The project helped me understand how to work with lists and dictionaries, use loops and conditional statements, accept and validate user input, calculate scores, randomize question order, and implement replay functionality.

## Future Improvements

- Add questions from multiple topics.
- Display the correct answer when a user answers incorrectly.
- Add a maximum number of attempts.
- Store scores from previous rounds.

---