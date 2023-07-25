# Building an "Interface"

# Using Abstract base Classes to enforce class constraints
from abc import ABC, abstractmethod


class JSONify(ABC): # modifyiable class which serves a function as an interface, has a capabilty it knows how to provide
    @abstractmethod
    def toJSON(self):
        pass
    

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f"{{\"circle\" : {str(self.calcArea())} }}"


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side

c = Circle(10)
print(c.calcArea())
print(c.toJSON())

s = Square(5)
print(s.calcArea())