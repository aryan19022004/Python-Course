#Exception handling in Python allows you to manage errors gracefully without crashing your program. You can use try-except blocks to catch and handle exceptions. Here's an example:
try:
    # This will raise a ZeroDivisionError
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
#You can also catch multiple exceptions:
try:
    # This will raise a ValueError
    number = int("abc")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
#You can also use a generic exception handler to catch any type of exception:
try:
    # This will raise an exception
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
#You can also use the else block to execute code if no exceptions were raised, and the finally block to execute code regardless of whether an exception was raised or not:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"The result is: {result}")
finally:
    print("This will always be executed.")

