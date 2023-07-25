# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: use the __repr__ method to return an obj representation
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The catcher in the Rye", "JD Salinger", 29.95)


# Testing
print(b1) # War and Peace by Leo Tolstoy, costs 39.95
print(str(b1)) # War and Peace by Leo Tolstoy, costs 39.95
print(b2) # The catcher in the Rye by JD Salinger, costs 29.95
print(repr(b2)) # title=The catcher in the Rye, author=JD Salinger, price=29.95