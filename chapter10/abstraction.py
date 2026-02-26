#Abstraction is the process of hiding the implementation details and showing only the functionality to the user. It allows us to focus on what an object does instead of how it does it.    
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)   
rectangle = Rectangle(5, 3)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
