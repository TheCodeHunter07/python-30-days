# Task: show a full name in upper, lower and title case, reversed, and as initials


name = input("Enter your full name: ")

parts = name.split()


print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"Title Case: {name.title()}")
print(f"Reverse: {name[-1::-1]}")
print(f"Initials: {parts[0][0] + " " + parts[1][0]}")



