# task: Create day-05/tables.py. -  print the multiplication table of any number


number = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{number} x {i} = {number*i}")