correct_username = "admin"
correct_password = "python@123"

username = input("Enter the username: ")
password = input("Enter the password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password!")