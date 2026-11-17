# Stretch: password_strength.py — rate a password as weak, medium or strong and explain why.

# print(has_uppercase) 
# print(has_lowercase)
# print(has_digit)


def check_password(password):
    """Check password requirements and return feedback."""

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    feedback = []

    for character in password:

        if character.isupper():
            has_uppercase = True

        elif character.islower():
            has_lowercase = True

        elif character.isdigit():
            has_digit = True

        elif not character.isalnum():
            has_special = True

    has_minimum_length = len(password) >= 8

    if not has_uppercase:
        feedback.append("Missing uppercase letter.")

    if not has_lowercase:
        feedback.append("Missing lowercase letter.")

    if not has_digit:
        feedback.append("Missing digit.")

    if not has_special:
        feedback.append("Missing special character.")

    if not has_minimum_length:
        feedback.append("Password must contain at least 8 characters.")

    score = (
        int(has_uppercase)
        + int(has_lowercase)
        + int(has_digit)
        + int(has_special)
        + int(has_minimum_length)
    )

    return score, feedback


def calculate_strength(score):
    """Determine password strength based on score."""

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


def display_result(strength, feedback):
    """Display password strength and improvement suggestions."""

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Suggestions:")

        for suggestion in feedback:
            print("-", suggestion)

    else:
        print("Excellent! Your password meets all requirements.")


def main():
    """Run the password strength checker."""

    password = input("Enter your password: ")

    score, feedback = check_password(password)

    strength = calculate_strength(score)

    display_result(strength, feedback)


if __name__ == "__main__":
    main()

     
     