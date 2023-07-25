#Using data classes to represent data objects

from dataclasses import dataclass


@dataclass
class Book:
    title : str # typehints required for dataclass wrapper to work but no longer required to use the __init__() function or self.
    author : str
    pages : int
    price : float

    def bookinfo(self):
        return f"{self.title} by {self.author}, {self.pages} Pages"


# create some book instances
b1 = Book("War and Peace", "Leo Tolstoy",1225, 39.95)
b2 = Book("The catcher in the Rye", "JD Salinger",400, 29.95)

# access fields
print(b1.title) # War and Peace
print(b2.author) # JD Salinger

# TODO: print the book itself - dataclasses implement __repr__
print(b1) # Book(title='War and Peace', author='Leo Tolstoy', pages=1225, price=39.95)

# TODO: comparing two dataclasses - they implement __eq__
print(b1 == b2) # False

# TODO: change some fields
b1.title = "A new title"
b1.author = "A new author"
b1.pages = 900
print(b1.bookinfo()) # A new title by A new author, 900 Pages