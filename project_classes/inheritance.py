
class Publication:
    def __init__(self, title , price) -> None:
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        # self.title = title
        # self.price = price
        self.author = author
        self.pages = pages





class Magazine(Periodical):
    def __init__(self, title, publisher,price, period) -> None:
        super().__init__(title, price, period,publisher)
        # self.title = title
        # self.price = price
        # self.period = period
        # self.publisher = publisher


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period) -> None:
        super().__init__(title, price, period,publisher)   
        # self.title= title
        # self.price = price
        # self.period = period
        # self.publisher = publisher


b1 = Book("Brave World", "Aldoues Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "NYT Company", 6.0, "Daily")
m1 = Magazine("Scientific Amercian", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)