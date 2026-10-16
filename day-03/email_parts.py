# Task :  split an email address into username and domain

email = input("Enter your email: ")

parts = email.split("@")

username = parts[0]
domain = parts[1]

print(f"Email: {email}")
print(f"Username is: {username}")
print(f"Domain is: {domain}")

# ALternative approach using find()

email = input("Enter your email: ")

position = email.find("@")  #suppose the  position of @ is 5, because indexing starts at zero.

username = email[:position]  #This takes everything before index 5 menas position.

domain = email[position + 1:]  #This starts after @  menas when comsideimg index position =index 5 but fo doman we dont wan to include @ so we used postion +1 means 5+1 so it print from 6 toremainning characters  and takes the remaining characters.

print(f"Username: {username}")
print(f"Domain: {domain}")

