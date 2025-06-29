class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

my_book = Book("Friedrich Nietzsche", "Beyond Good and Evil")
print(my_book)