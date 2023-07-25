# TODO: create a basic class
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
    


# TODO: create some book instances

b1= Book("War and Peace","Leo Tolstoy", 1225, 39.95)
b2 = Book("The catcher in the rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
#print(b1.getprice(), b1.price)

# TODO: try setting discount
# print(b2.getprice())
# b2.setdiscount(0.25)
# print(b2.getprice())

# TODO: test printing secret atttributes
print(b2.__secret) # this will throw an error
print(b2._Book__secret) # this will subvert the secret attribute and print it
