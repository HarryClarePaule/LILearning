# using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK" )

    # TODO: double-underscore properties are hidden from other classes

    __booklist = None

    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist    

    # instance methods receiev a specific object insatnce as an argument
    # and operate on data specific to that object instance

    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title,booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

# TODO: access the class method

print("Book types: ", Book.getbooktypes())

# TODO: Create some book instances:
b1 = Book('Python for Beginners','HARDCOVER')
b2 = Book('American Psycho', 'EBOOK') # will return value error
b3 = Book('Book3', 'Comic') # will return value error

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
