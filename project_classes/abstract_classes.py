from  abc import ABC, abstractmethod
"""
the base class GraphicShape is here just a idea and while instantiating ,the properties of base class  arenot used, 
we use abc module for that

from linkedin learning

"""




class GraphicShape(ABC):
    def __init__(self) -> None:
        super().__init__()


    @abstractmethod
    def calcArea(self):
        pass 



class Circle(GraphicShape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def calcArea(self):
        return 3.14 * self.radius ** 2

    



class Square(GraphicShape):
    def __init__(self, side) -> None:
        self.side = side

    def calcArea(self):
        return self.side * self.side


#g = GraphicShape()

c = Circle(10)
print(c.calcArea())

s = Square(12)
print(s.calcArea())
