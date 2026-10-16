# # Task: check user input against a hard-coded username and password

# Requirements:

# Set the correct username to "admin".
# Set the correct password to "python123".
# Ask the user for their username and password.
# If both match, print "Login successful".
# Otherwise, print "Invalid username or password".


data = {
    "username": "admin",
    "password": "python123"
}

username = input("Enter the username: ")
password = input("Enter the password: ")

if username == data["username"] and password == data["password"]:
    print("Login successful")
else:
    print("Invalid username or password")