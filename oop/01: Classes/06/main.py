class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.book = []

    def add_book(self, book):
        self.book.append(book)

    def remove_book(self, book):
        for b in self.book:
            if b.title or b.author == book.title or book.author:
                self.book.remove(b)

    def search_books(self, search_string):
        books = []

        for b in self.book:
            queries = b.title.lower().split() + b.author.lower().split()

            for query in queries:
                if query.startswith(search_string.lower()):
                    books.append(b)

        return books
