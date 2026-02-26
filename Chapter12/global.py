#global keyword is used to declare a variable as global, allowing it to be accessed and modified across different scopes within the program. When a variable is declared as global, it can be accessed and modified from any part of the program, including inside functions. This is useful when you want to maintain a single instance of a variable that can be shared and updated across multiple functions or modules.
#Example 1: Using global variable
counter = 0  # Global variable
def increment():
    global counter  # Declare counter as global to modify it
    counter += 1
    print(f"Counter inside function: {counter}")

increment()  # Output: Counter inside function: 1
print(f"Counter outside function: {counter}")  # Output: Counter outside function: