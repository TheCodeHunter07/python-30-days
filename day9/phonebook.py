# ASSIGNMENT
# 1 phonebook.py — add, search, update and delete contacts through a menu

# phonebook.py — Add, search, update, and delete contacts through a menu

contacts = {}

while True:
    print("=" * 32)
    print("          PHONEBOOK")
    print("=" * 32)

    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    print("=" * 32)

    choice = input("Enter your choice (1-6): ")

    # Add Contact
    if choice == "1":
        print("--- Add Contact ---")

        name = input("Enter the name: ")
        number = input("Enter the contact number: ")

        contacts[name] = number

        print("Contact added successfully!")

    # Search Contact
    elif choice == "2":
        print("--- Search Contact ---")

        name = input("Enter the name to search: ")

        if name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]}")
        else:
            print("Contact not found!")

    # Update Contact
    elif choice == "3":
        print("--- Update Contact ---")

        name = input("Enter the name to update: ")

        if name in contacts:
            number = input("Enter the new phone number: ")

            contacts[name] = number

            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    # Delete Contact
    elif choice == "4":
        print("--- Delete Contact ---")

        name = input("Enter the name to delete: ")

        if name in contacts:
            del contacts[name]

            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # View All Contacts
    elif choice == "5":
        print("--- All Contacts ---")

        if contacts:
            for name, number in contacts.items():
                print(f"Name: {name} | Phone: {number}")
        else:
            print("Your phonebook is empty.")

    # Exit
    elif choice == "6":
        print("Exiting Phonebook...")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please select a valid option.")
 