#class method is a method that is bound to the class and not the instance of the class. It can modify a class state that applies across all instances of the class, rather than just a single instance. Class methods are defined using the @classmethod decorator and take cls as the first parameter instead of self.     
class MyClass:
    class_variable = "I am a class variable"

    @classmethod
    def class_method(cls):
        return f"This is a class method. {cls.class_variable}"
    
# Calling the class method using the class name
print(MyClass.class_method())
# Calling the class method using an instance of the class
my_instance = MyClass()
print(my_instance.class_method())


#property decorator is used to define a method as a property. It allows us to access the method like an attribute, without needing to call it as a function. This is useful for creating read-only attributes or for adding logic when getting or setting an attribute.
class Circle:   
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * (self._radius ** 2)
circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area}")
circle.radius = 10
print(f"Updated Radius: {circle.radius}")
print(f"Updated Area: {circle.area}")
