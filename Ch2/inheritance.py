# Understanding class inheritance

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, price, author, pages):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __inti__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)



class Newspaper(Periodical):
    def __inti__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)



b1 = Book("Brave New World",29.0, "Author1", 311)
n1 = Newspaper("Newspaper1", "Harry", 2.0, "Daily")
m1 = Magazine("Mag1", "Steven", 5.0, "Monthly")


# Test
print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
