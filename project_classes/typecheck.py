"""

checking class types and instances
"""

class Book:
    def __init__(self, title) -> None:
        self.title = title





class Newspaper:
    def __init__(self, name) -> None:
        self.name = name



b1 = Book("The Catcher in the Eye")
b2 = Book("The Gapes of Wrath")
n1 = Newspaper("the Washington Post")
n2 = Newspaper("The New Yorktimes")


print(type(b1))
print(type(n1))

print(type(b1) == type(b2))
print(type(b1) == type(n2))

print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))

