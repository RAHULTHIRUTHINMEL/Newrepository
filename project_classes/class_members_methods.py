class Book:
    #class variable
    Book_Types = ("Hardcover", "Paperback", "Ebook")  #classattribute

    __booklist = None



    @classmethod
    def getbooktypes(cls):
        return cls.Book_Types

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist


 

    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype) -> None:
        self.title = title
        if (not booktype in Book.Book_Types):
            raise ValueError(f"{booktype} is not a valifd book type")
        else:
            self.booktype = booktype

    #to access class attribute
print("Book types: ", Book.getbooktypes())


b1 = Book("Title 1", "Hardcover")
b2 = Book("Title 2", "Paperback")

#use the static method to acces the singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)