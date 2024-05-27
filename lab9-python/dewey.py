from hashtable import HashTable

class BookInfo:
    def __init__(self, decimal: str, book_name: str, author: str):
        self.decimal = decimal
        self.book_name = book_name
        self.author = author

class Library:
    def __init__(self, book_lst: list[BookInfo]):
        self.lookup_table = HashTable()
        for book in book_lst:
            self.lookup_table[book.decimal] = book.book_name

    """
    TODO: implement find_book to return the name of a book with a given Dewey decimal key decimal_key.
    If a book cannot be found, then print "Book with decimal key {key} not found" (replacing {key}
    with the value of the input decimal_key).
    """
    def find_book(self, decimal_key: str) -> str:
        ...

    """
    TODO: implement checkout_book to return the name of a book with a given Dewey decimal key decimal_key.
    Also check out the book - this should remove the book from the lookup table.
    If a book cannot be found, then print "Book with decimal key {key} not found" (replacing {key}
    with the value of the input decimal_key).
    """
    def checkout_book(self, decimal_key: str) -> str:
        ...

if __name__ == "__main__":
    # Dewey decimal technically shouldn't apply to fiction books, so this isn't an entirely accurate example...
    # I hope you like the books though =)
    lib = Library([
        BookInfo("800.375", "Lalka", "Bolesław Prus"),
        BookInfo("812.99", "Ferdydurke", "Witold Gombrowicz"),
        BookInfo("875.231", "Blood of Elves", "Andrzej Sapkowski"),
        BookInfo("377.4", "Inny świat", "Gustaw Herling-Grudziński"),
        BookInfo("312.01", "Kaminie na szaniec", "Henryk Sienkiewicz")
        ])
    print(lib.find_book("875.231"))
    print(lib.find_book("377.4"))
    print(lib.find_book("800"))
    print(lib.checkout_book("812.99"))
    print(lib.checkout_book("812.30"))