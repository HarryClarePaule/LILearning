# implemting default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No author"
    pages: int = 0
    price: float = field(default_factory=price_func)
    # price: float = field(default=10.0)


# b1 = Book()
# print(f" b1: {b1}") # Book(title='No title', author='No author', pages=0, price=0.0)

b2 = Book("War and Peace", "Leo Tolstoy",1225)
b3 = Book("The catcher in the Rye", "JD Salinger",400)

print(b2) # Book(title='The catcher in the Rye', author='JD Salinger', pages=400, price=10.0) / Book(title='War and Peace', author='Leo Tolstoy', pages=1225, price=32.0)
print(b3) # Book(title='The catcher in the Rye', author='JD Salinger', pages=400, price=10.0) / Book(title='The catcher in the Rye', author='JD Salinger', pages=400, price=21.0)