#Conditional statements are used to perform different actions based on different conditions. In Python, we use if, elif, and else statements to create conditional statements.
#Example of if statement
age = 18
if age >= 18:
    print("You are an adult.")
#Example of if-else statement
age = 16    
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")   
#Example of if-elif-else statement
age = 25    
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")