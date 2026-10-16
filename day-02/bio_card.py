
#Method 1: Using print() Statements and Multiple Arguments

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("================================")
print("          PROFILE CARD")
print("================================")

print("Name:", name)
print("Age:", age)
print("City:", city)

print("================================")


#Method 2: Using f-Strings

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("=" * 32)
print(f"{'PROFILE CARD':^32}")
print("=" * 32)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

print("=" * 32)
