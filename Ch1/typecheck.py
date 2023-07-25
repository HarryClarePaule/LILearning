class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    # TODO: create insatnce methods
    def getprice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount


class Newspaper:
    def __init__(self, name):
        self.name = name


# TODO: Create some instances of the classes
b1 = Book("The catcher in the Rye","Author", 249, 24.99)
b2 = Book("The grapes of wrath","Author2",300,29.99)
n1 = Newspaper("The Washington post")
n2 = Newspaper("The NEw York Times")

# TODO: use type() to inspect the object type

# print(type(b1))
# print(type(n1))


# TODO: compare two types together
# print(type(b1) == type(b2))
# print(type(b2) == type(n1))


# TODO: use isinstance to compare a specific instance to a known type

print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))