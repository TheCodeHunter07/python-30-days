

import json
from book import Book
from member import Member

class Library:

    def __init__(self):

        self.books = []
        self.members = []

    def __str__(self):

        return f"Library: {len(self.books)} Books, {len(self.members)} Members"

    def __repr__(self):

        return f"Library(books={self.books}, members={self.members})"

    def add_book(self, book):

        found = False

        # Check whether the book ID already exists
        for existing_book in self.books:

            if existing_book.book_id == book.book_id:
                found = True
                break

        # Add book if it is not already registered
        if found == True:

            print("Book with this ID already exists!")

        else:

            self.books.append(book)

            print("Book added successfully!")
            
    def remove_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:

                if book.is_borrowed:
                    print("Cannot remove a borrowed book!")
                    return

                for member in self.members:

                    if book in member.borrowed_books:
                        print("Cannot remove a borrowed book!")
                        return

                self.books.remove(book)
                print("Book removed successfully!")
                return

        print("Book not found!")


    def register_member(self, member):

        found = False

        for existing_member in self.members:

            if existing_member.member_id == member.member_id:

                found = True
                break

        if found == True:

            print("Member with this ID already exists!")

        else:

            self.members.append(member)

            print("Member registered successfully!")


    def borrow_book(self, book_id, member_id):

        book_found = False
        member_found = False

        # Find the book
        for book in self.books:

            if book.book_id == book_id:
                book_found = True
                selected_book = book
                break

        # Find the member
        for member in self.members:

            if member.member_id == member_id:
                member_found = True
                selected_member = member
                break

        # Check whether book exists
        if book_found == False:
            print("Book not found!")
            return

        # Check whether member exists
        if member_found == False:
            print("Member not found!")
            return

        # Check whether book is already borrowed
        if selected_book.is_borrowed == True:
            print("Book is already borrowed!")
            return

        # Check borrowing limit
        if len(selected_member.borrowed_books) >= 3:
            print("Borrowing limit reached!")
            return

        # Complete borrowing
        selected_book.is_borrowed = True

        selected_member.borrow_book(selected_book)

        print("Borrowing completed successfully!")


    def return_book(self, book_id, member_id):

        book_found = False
        member_found = False

        # Find the book
        for book in self.books:

            if book.book_id == book_id:
                book_found = True
                selected_book = book
                break

        # Find the member
        for member in self.members:

            if member.member_id == member_id:
                member_found = True
                selected_member = member
                break

        # Check whether book exists
        if book_found == False:
            print("Book not found!")
            return

        # Check whether member exists
        if member_found == False:
            print("Member not found!")
            return

        # Check whether the book is borrowed by this member
        if selected_book not in selected_member.borrowed_books:
            print("This member has not borrowed this book!")
            return

        # Complete return
        selected_book.is_borrowed = False

        selected_member.return_book(selected_book)

        print("Return completed successfully!")


    def search_book(self, search_value):

        found = False

        for book in self.books:

            if search_value.lower() in book.title.lower() or search_value.lower() in book.author.lower():

                print(book)
                found = True

        if found == False:

            print("No matching books found!")


    def list_borrowed_books(self):

        found = False

        for member in self.members:

            for book in member.borrowed_books:

                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Borrowed By:", member.name)
                print("Member ID:", member.member_id)
                print("-------------------------")

                found = True

        if found == False:

            print("No books are currently borrowed.")


    def to_dict(self):

        books_data = []
        members_data = []

        # Convert all books into dictionaries
        for book in self.books:
            books_data.append(book.to_dict())

        # Convert all members into dictionaries
        for member in self.members:
            members_data.append(member.to_dict())

        return {
            "books": books_data,
            "members": members_data
        }

    @classmethod
    def from_dict(cls, data):

        library = cls()

        # Reconstruct Book objects
        for book_data in data["books"]:

            book = Book.from_dict(book_data)

            library.books.append(book)

        # Reconstruct Member objects
        for member_data in data["members"]:

            member = Member.from_dict(member_data, library.books)

            library.members.append(member)

        return library


    def save_data(self):

        # Convert library objects into dictionaries
        library_data = self.to_dict()

        # Save dictionary data into JSON file
        with open("library.json", "w") as file:

            json.dump(library_data, file, indent=4)

        print("Library data saved successfully!")


    @classmethod
    def load_data(cls):

        try:

            with open("library.json", "r") as file:

                library_data = json.load(file)

            library = cls.from_dict(library_data)

            print("Library data loaded successfully!")

            return library

        except FileNotFoundError:

            print("Library data file not found!")

            return cls()