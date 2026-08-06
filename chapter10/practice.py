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