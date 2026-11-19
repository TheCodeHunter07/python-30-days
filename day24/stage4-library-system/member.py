class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Books: {len(self.borrowed_books)}"

    def __repr__(self):
        return f"Member(member_id='{self.member_id}', name='{self.name}', borrowed_books={self.borrowed_books})"

    def borrow_book(self, book):

        if book in self.borrowed_books:
            print("This book is already borrowed by this member!")

        elif len(self.borrowed_books) >= 3:
            print("Borrowing limit reached! You can borrow only 3 books.")

        else:
            self.borrowed_books.append(book)

    def return_book(self, book):

        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

        else:
            print("This book is not borrowed by this member.")

    def to_dict(self):

        borrowed_book_ids = []

        for book in self.borrowed_books:
            borrowed_book_ids.append(book.book_id)

        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": borrowed_book_ids
        }

    @classmethod
    def from_dict(cls, data, books):

        member = cls(data["member_id"], data["name"])

        for book_id in data["borrowed_books"]:

            for book in books:

                if book.book_id == book_id:
                    member.borrowed_books.append(book)
                    break

        return member