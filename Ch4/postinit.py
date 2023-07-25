# Using the post_init function in data classes

from dataclasses import dataclass


@dataclass
class Book:
    title : str # typehints required for dataclass wrapper to work but no longer required to use the __init__() function or self.
    author : str
    pages : int
    price : float

# TODO: the __post_init__ function lets us customise additional properties after the object has been initialised via built-in __init__
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


# create some book instances
b1 = Book("War and Peace", "Leo Tolstoy",1225, 39.95)
b2 = Book("The catcher in the Rye", "JD Salinger",400, 29.95)

# TODO: ues the description attribute
print(b1.description) # War and Peace by Leo Tolstoy, 1225 pages
print(b2.description) # The catcher in the Rye by JD Salinger, 400 pages