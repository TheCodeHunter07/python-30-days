email = input("Enter email: ")

position = email.find("@")

username = email[:position]

domain = email[position + 1:]

print(email)
print("Username:", username)
print("Domain:", domain)