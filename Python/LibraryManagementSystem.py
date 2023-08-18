class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print("Book borrowed.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print("Book returned.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


# Using the classes
my_book = Book("Harry Potter", "J.K. Rowling", 400)
my_library = Library()
my_library.add_book(my_book)
my_book.borrow()
my_book.return_book()
