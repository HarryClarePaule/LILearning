# Using the __eq__, __ge__ and __lt__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method to check equality between two objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title == value.title and
        self.author == value.author and
        self.price == value.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price >= value.price
    
    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price < value.price



b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("to kill and mockingbird", "Harper Lee", 24.95)



# TODO: Check for equality
print(b1 == b3) # True
print(b1 == b2) #False
# print(b1 == 9) # ValueError

# TODO: check for greater and lesser value
print(b2 >= b1) # False
print(b2 < b1) # True

# TODO: Now we can sort them too
books = [b1, b2, b3, b4]
books.sort()
print([book.title for book in books])