#Use of warlus operator
#The walrus operator (:=) allows you to assign a value to a variable as part of an expression. It is often used in situations where you want to both compute a value and use it in a condition or loop.
#Example 1: Using walrus operator in a while loop
#Without walrus operator
n = 0
while n < 5:
    print(n)
    n += 1
#With walrus operator
n = 0
while (n := n + 1) < 5:
    print(n)

#Example 2: Using walrus operator in an if statement
#Without walrus operator
value = input("Enter a value: ")
if value:
    print(f"You entered: {value}")
#With walrus operator
if (value := input("Enter a value: ")):
    print(f"You entered: {value}")

