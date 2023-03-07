



class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self) -> None:
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)
"""
python used method resolution order to look up class, here python looks in order they are defined from left to right,
thats why it prints class A.

"""


c = C()
c.showprops()
print(C.mro())