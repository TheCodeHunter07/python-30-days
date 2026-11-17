# ASSIGNMENT
# 3 age_validator.py — raise a custom InvalidAgeError for ages below 0 or above 120


class InvalidAgeError(Exception):
    pass

try:

    age = int(input("\nEnter the age between 0 to 120: "))

    if age < 0 or age > 120:

       raise InvalidAgeError("\nInvalid age input Enter the age between 0-120")

except ValueError:
    print("\nEnter the valid integer input")

except InvalidAgeError as e:
    print(e)

else:
    print("\nValid age")

finally:
    print("\nAge Validation Execution completed")


