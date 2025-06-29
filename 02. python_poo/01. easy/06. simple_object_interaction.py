class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

class Library:
    def __init__(self, books: list[Book] = None) -> None:
        self.books = [] if books is None else books

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"The book {book.title} has been added to the libary")

    def list_books(self) -> None:
        if not self.books:
            print("The library is currently empty.")
            return
        for book in self.books:
            print(f"The author of {book.title} is {book.author}")

my_book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
my_book2 = Book("Pride and Prejudice", "Jane Austen")
my_book3 = Book("1984", "George Orwell")

my_library = Library()
my_library.add_book(my_book1)
my_library.add_book(my_book2)
my_library.add_book(my_book3)

my_library.list_books()