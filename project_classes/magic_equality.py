class Book:
    def __init__(self, title,author,price) -> None:
        self.title = title
        self.author = author
        self.price = price
    

    def __eq__(self, value) -> bool:
        if not isinstance(value, Book):
            raise ValueError("Cannot compare book to a non book")
        return(self.title == value.title and 
        self.author == value.author and
        self.price == value.price)
    
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare book to a non book")
        return(self.price >= value.price)
    
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare book to a non book")
        return(self.price < value.price)




"""
magic method __eq__ cheks for equality between two objects
magic method __ge__ establishes relationship  >=with another object
magic method __lt__ establishes relationship  < with another object


"""





b1 = Book("Brave New World", "Leo Tolsyoy",  39.95)
b2 = Book("War and Peace", "JS Salinger", 29.95)
b3 = Book("War and Peace", "JS Salinger", 29.95)
b4 = Book("To kill a mocking bird", "Harper LEE", 24.95)

# print(b2 == b3)
# print(b2==b4)
# print(b1==42)

print(b2 >= b1)

