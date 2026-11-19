


class Book:

    def __init__(self,book_id,title,author,is_borrowed=False):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):

        if self.is_borrowed == True:
            status = "Borrowed"
        else:
            status = "Available"

        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"

    def __repr__(self):

        return f"Book(book_id='{self.book_id}', title='{self.title}', author='{self.author}', is_borrowed={self.is_borrowed})"

    def to_dict(self):

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["is_borrowed"]
        )



