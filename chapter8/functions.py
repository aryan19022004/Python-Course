#Functions in Python
#Functions are reusable blocks of code that perform a specific task. They help to break down complex problems into smaller, manageable pieces. In Python, we define a function using the def keyword.
#Example of a simple function
def greet(name):
    print("Hello, " + name + "!")   
greet("Alice")  # Output: Hello, Alice!
#Function with return statement
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8
#Function with default parameters
def greet(name="Guest"):
    print("Hello, " + name + "!")
greet()  # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!
#Function with variable number of arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total    
print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5))     # Output: 9

#Function with keyword arguments
def display_info(name, age):
    print("Name:", name)
    print("Age:", age)
display_info(age=30, name="Charlie")  # Output: Name: Charlie, Age: 30


#RECURSION iN PYTHON
#Recursion is a programming technique where a function calls itself in order to solve a problem. A recursive function typically has a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
#Example of a recursive function to calculate factorial 
def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case
print(factorial(5))  # Output: 120