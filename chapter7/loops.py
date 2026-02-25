#Loops In Python
#Loops are used to execute a block of code repeatedly until a certain condition is met. In Python, we have two types of loops: for loops and while loops.
#Example of for loop    
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)    
#Example of while loop
count = 0   
while count < 5:
    print("Count:", count)
    count += 1

for i in range(9):
    print(i)

#For loop with else statement
for i in range(5):
    print(i)
else:
    print("Loop is finished.")  

#Using pass statement in loops
for i in range(5):  
    if i == 2:
        pass  # This will do nothing and the loop will continue
    print(i)