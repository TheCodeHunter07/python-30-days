name = input("Enter your full name: ")

parts = name.split()

initials = ""
for part in parts:
    initials += part[0].upper()

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())
print("Reversed:", name[::-1])
print("Initials:", initials)