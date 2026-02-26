#Object oriented Programming in Python
#Defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
#Creating an object of the class
person1 = Person("Alice", 30)
print(person1.greet())
print(Person.greet(person1))  # Calling method using class name and passing the object

#Creating another object
person2 = Person("Bob", 25) 
print(person2.greet())

#Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")

#Inheritance
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.employee_id = employee_id

    def work(self):
        return f"{self.name} is working with employee ID {self.employee_id}."   
employee1 = Employee("Charlie", 28, "E123")
print(employee1.greet())  # Inherited method