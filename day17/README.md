# Day 17 – Error Handling

## 📚 Topics Covered

- Exception handling using `try` and `except`.
- Understanding `else` and `finally` blocks.
- Common Python exceptions:
  - `ValueError`
  - `ZeroDivisionError`
  - `FileNotFoundError`
  - `KeyError`
- Catching specific exceptions instead of using a bare `except`.
- Raising exceptions using `raise`.
- Creating custom exception classes.

## 📝 Assignments

### 1. Safe Calculator – safe_calculator.py

Created a calculator that handles invalid user input and mathematical errors.

Features:
- Performs basic arithmetic operations.
- Handles invalid input.
- Prevents division by zero.
- Displays meaningful error messages instead of crashing.

### 2. Safe File Reader – safe_file_reader.py

Created a program that asks the user for a filename and reads its contents.

Features:
- Accepts a filename from the user.
- Reads file contents safely.
- Handles `FileNotFoundError` when a file does not exist.

### 3. Age Validator – age_validator.py

Created a custom exception named `InvalidAgeError`.

Features:
- Validates user age.
- Raises an exception for ages below 0.
- Raises an exception for ages above 120.
- Accepts valid ages between 0 and 120.

### 4. Stretch Assignment – Student Records Manager

Improved the Student Records Manager by adding error handling.

Features:
- Handles invalid user input.
- Prevents unexpected application crashes.
- Uses appropriate exception handling.
- Provides meaningful error messages.

## 🎯 Learning Outcomes

- Learned how to handle runtime errors using exception handling.
- Understood the importance of catching specific exceptions.
- Practiced raising built-in and custom exceptions.
- Improved application reliability through proper error handling.
- Learned how to handle invalid input and missing files gracefully.