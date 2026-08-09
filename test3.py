class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You returned '{self.title}'.")
        else:
            print(f"'{self.title}' is already in the library.")

    def check_availability(self):
        if self.available:
            print(f"'{self.title}' is available.")
        else:
            print(f"'{self.title}' is currently borrowed.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("\nBooks in the library:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"- {book.title} by {book.author} [{status}]")


book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Things Fall Apart", "Chinua Achebe")
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.show_books()
book1.borrow()
book1.check_availability()
book1.return_book()
book1.check_availability()
library.show_books()