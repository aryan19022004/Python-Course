# ============================================================
# 1️⃣ Basic Inheritance Example (Method Overriding)
# ============================================================

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"


# Child class Dog inherits from Animal
class Dog(Animal):
    # Method overriding
    def speak(self):
        return "Woof!"  


# Child class Cat inherits from Animal
class Cat(Animal):
    # Method overriding
    def speak(self):
        return "Meow!"  


# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling overridden methods
print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")


# ============================================================
# 2️⃣ Another Example of Inheritance (Vehicle Example)
# ============================================================

# Parent class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Engine started."


# Child class Car
class Car(Vehicle):
    # Overriding parent method
    def start_engine(self):
        return f"{self.make} {self.model} engine started with a roar!"  


# Child class Motorcycle
class Motorcycle(Vehicle):
    # Overriding parent method
    def start_engine(self):
        return f"{self.make} {self.model} engine started with a vroom!"


car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Harley-Davidson", "Street 750")

print(car.start_engine())
print(motorcycle.start_engine())


# ============================================================
# 3️⃣ Types of Inheritance in Python
# ============================================================


# ============================================================
# 3.1️⃣ Single Inheritance
# One child class inherits from one parent class
# ============================================================

class Parent:
    def parent_method(self):
        return "This is the parent method."

class Child(Parent):
    def child_method(self):
        return "This is the child method."

child = Child()

print(child.parent_method())  # Inherited from Parent
print(child.child_method())   # Child's own method



# ============================================================
# 3.2️⃣ Multiple Inheritance
# One child inherits from more than one parent class
# ============================================================

class Mother:
    def mother_method(self):
        return "This is the mother method."

class Father:
    def father_method(self):
        return "This is the father method."

class ChildMultiple(Mother, Father):
    def child_method(self):
        return "This is the child method."

child_multi = ChildMultiple()

print(child_multi.mother_method())  
print(child_multi.father_method())  
print(child_multi.child_method())   



# ============================================================
# 3.3️⃣ Multilevel Inheritance
# Grandparent → Parent → Child
# ============================================================

class Grandparent:
    def grandparent_method(self):
        return "This is the grandparent method."    

class ParentLevel(Grandparent):
    def parent_method(self):
        return "This is the parent method."

class ChildLevel(ParentLevel):
    def child_method(self):
        return "This is the child method."

child_level = ChildLevel()

print(child_level.grandparent_method())  
print(child_level.parent_method())       
print(child_level.child_method())  

# ============================================================
#using super() to run parent class method


class ParentSuper:
    def parent_method(self):
        return "This is the parent method." 
class ChildSuper(ParentSuper):
    def parent_method(self):
        parent_message = super().parent_method()  # Call the parent method
        return f"{parent_message} This is the child method overriding it."  
child_super = ChildSuper()
print(child_super.parent_method())




# ============================================================
# 3.4️⃣ Hierarchical Inheritance
# Multiple child classes inherit from one parent
# ============================================================

class ParentHier:
    def parent_method(self):
        return "This is the parent method."

class Child1(ParentHier):
    def child1_method(self):
        return "This is the child1 method."

class Child2(ParentHier):
    def child2_method(self):
        return "This is the child2 method."

child1 = Child1()
child2 = Child2()

print(child1.parent_method())  
print(child1.child1_method())  

print(child2.parent_method())  
print(child2.child2_method())  



# ============================================================
# 3.5️⃣ Hybrid Inheritance
# Combination of multiple + hierarchical inheritance
# ============================================================

class Base:
    def base_method(self):
        return "This is the base method."

class Derived1(Base):
    def derived1_method(self):
        return "This is the derived1 method."   

class Derived2(Base):
    def derived2_method(self):
        return "This is the derived2 method."

class Hybrid(Derived1, Derived2):
    def hybrid_method(self):
        return "This is the hybrid method."

hybrid = Hybrid()

print(hybrid.base_method())      
print(hybrid.derived1_method())  
print(hybrid.derived2_method())  
print(hybrid.hybrid_method())    

