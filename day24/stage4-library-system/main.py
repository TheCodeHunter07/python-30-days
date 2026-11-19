from book import Book
from member import Member
from library import Library

import os

print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())


# Create Library object
library = Library.load_data()


while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")

    print("1. Add Book")
    print("2. Remove Book")
    print("3. Register Member")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Search Book")
    print("7. List Borrowed Books")
    print("8. Display All Books")
    print("9. Display All Members")
    print("10. Save Library Data")
    print("11. Exit")

    choice = input("\nEnter your choice: ")


    # Option 1: Add Book
    if choice == "1":

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)

        library.add_book(book)


    # Option 2: Remove Book
    elif choice == "2":

        book_id = input("Enter Book ID to remove: ")

        library.remove_book(book_id)


    # Option 3: Register Member
    elif choice == "3":

        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")

        member = Member(member_id, name)

        library.register_member(member)


    # Option 4: Borrow Book
    elif choice == "4":

        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        library.borrow_book(book_id, member_id)


    # Option 5: Return Book
    elif choice == "5":

        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        library.return_book(book_id, member_id)


    # Option 6: Search Book
    elif choice == "6":

        search_value = input("Enter Book Title or Author: ")

        library.search_book(search_value)


    # Option 7: List Borrowed Books
    elif choice == "7":

        library.list_borrowed_books()


    # Option 8: Display All Books
    elif choice == "8":

        if len(library.books) == 0:

            print("No books available in the library.")

        else:

            for book in library.books:
                print(book)


    # Option 9: Display All Members
    elif choice == "9":

        if len(library.members) == 0:

            print("No members registered.")

        else:

            for member in library.members:
                print(member)


    # Option 10: Save Library Data
    elif choice == "10":

        library.save_data()


    # Option 11: Exit
    elif choice == "11":

        print("Thank you for using the Library Management System!")

        break


    # Invalid Choice
    else:

        print("Invalid choice! Please select a number between 1 and 11.")