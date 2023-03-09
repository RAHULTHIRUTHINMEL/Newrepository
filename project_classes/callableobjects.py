class Book:
    def __init__(self, title,author,pages,price) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} by {self.author} , costs {self.price}"
    
    def __call__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    

b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

print(b1)
b1("Anna Karinena", "Leo Tolstoy", 333, 89.9)
print(b1)