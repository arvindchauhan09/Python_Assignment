#abstract class demonstrate
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * self.__side

sqr = Square(5)
print(sqr.area())


