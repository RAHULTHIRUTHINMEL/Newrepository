class Book:
    def __init__(self, title,author,pages,price) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} by {self.author} , costs {self.price}"
    
    def __repr__(self) -> str:
        return f" title = {self.title},author = {self.author},price = {self.price}"



b1 = Book("Brave New World", "Leo Tolsyoy", 1125 , 39.95)
b2 = Book("War and Peace", "JS Salinger", 234, 29.95)


print(b1)
print(b2)
print(b2.__repr__())