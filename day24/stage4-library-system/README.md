# Library Management System

A console-based Library Management System developed using Python and Object-Oriented Programming (OOP).

The application allows users to manage books, register members, borrow and return books, search for books, and store library data using JSON.

## Features

### 1. Book Management
- Add new books to the library.
- Remove books using Book ID.
- Prevent duplicate Book IDs.
- Prevent removal of borrowed books.
- Display all books with their availability status.

### 2. Member Management
- Register new library members.
- Prevent duplicate Member IDs.
- Display all registered members.
- Track books borrowed by each member.

### 3. Borrow and Return Books
- Borrow books using Book ID and Member ID.
- Prevent double-borrowing.
- Allow a maximum of 3 books per member.
- Return borrowed books.
- Automatically update book availability.

### 4. Book Search
- Search books by title.
- Search books by author.
- Support partial text matching.

### 5. Borrowed Books Tracking
- Display all currently borrowed books.
- Show the details of the member who borrowed each book.

### 6. JSON Data Persistence
- Save library data into a JSON file.
- Load previously saved library data.
- Restore books, members, and borrowing relationships when the application restarts.

## Technologies Used

- Python 3
- JSON
- Object-Oriented Programming (OOP)

## Project Structure

```text
stage4-library-system/
│
├── book.py
├── member.py
├── library.py
├── main.py
├── library.json
├── README.md
└── class-diagram.png