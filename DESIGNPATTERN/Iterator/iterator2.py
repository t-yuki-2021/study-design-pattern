from collections.abc import Iterator, Iterable


class Book:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class BookShelf(Iterable):

    def __init__(self):
        self.__books = []

    def append_book(self, book: Book):
        self.__books.append(book)

    def get_book_at(self, index):
        return self.__books[index]

    def __iter__(self):
        return BookShelfIterator(self)


class BookShelfIterator(Iterator):

    def __init__(self, book_shelf: BookShelf):
        self.__book_shelf = book_shelf
        self.__index = 0

    def __next__(self):
        try:
            book = self.__book_shelf.get_book_at(self.__index)
            self.__index += 1
        except IndexError:
            raise StopIteration()
        return book

book_shelf = BookShelf()
book_shelf.append_book(Book('こころ1'))
book_shelf.append_book(Book('こころ2'))
book_shelf.append_book(Book('こころ3'))
book_shelf.append_book(Book('こころ4'))
book_shelf.append_book(Book('こころ5'))

for book in book_shelf:
    print(book.get_name())