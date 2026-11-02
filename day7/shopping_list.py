# Day 7 — Assignment 2: shopping_list.py-a menu to add, remove and view items until the user types quit

# Requirements

# Your program should repeatedly display a menu that allows the user to:

# Add an item.
# Remove an item.
# View the shopping list.
# Quit the program by typing quit.

shopping_list = []

while True:

    
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Quit")
    

    choice = int(input("Enter the choice: "))

    if choice == 1:
       item = input("Enter the item to add: ")
       shopping_list.append(item)

    elif choice == 2:
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
              print("This item does not exist")
    
    elif choice == 3:
        print(f"shopping list: {shopping_list}")

    elif choice == 4:
        print("Exiting shopping list...")
        break
    else:
        print("This choice does not exist choose choices between 1-4")
        


         