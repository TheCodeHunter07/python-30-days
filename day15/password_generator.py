# ASSIGNMENT
# 3 password_generator.py — use random and string to generate strong passwords

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation


password_length = int(input("Enter password length: "))

password = ""


for i in range(password_length):
    random_character = random.choice(characters)
    password += random_character

print("Generated Password:", password)
