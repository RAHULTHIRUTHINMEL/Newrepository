"""
from python 3.7 python introduced new feature called python data class to automate init 
and repr and eq magice methods


"""

from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float


b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# print(b1.author)
# print(b2.title)

print(b1)
print(b1==b3)



