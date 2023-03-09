from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float


    #the postinit func lets us customise additional property
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"





b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)


print(b1.description)
print(b2.description)