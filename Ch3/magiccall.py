# Using the __call__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
    
    # TODO: the __call__ method can be used to the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The catcher in the Rye", "JD Salinger", 29.95)

print(b1) # War and Peace by Leo Tolstoy, costs 39.95
b1("New Title", "New Author", 60.98) # update the attribute with the new call function
print(b1) # New Title by New Author, costs 60.98