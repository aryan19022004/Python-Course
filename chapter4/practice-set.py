#Write a program to store 7 fruits name entered by the user in a list and print them.
'''

fruits = []
for i in range(7):
    fruit = input("Enter the name of a fruit: ")
    fruits.append(fruit)
print("Fruits entered:", fruits)

'''

#Write a program to store marks of 6 students in a list and print them in sorted manner.

'''marks = []
for i in range(6):
    mark = float(input("Enter the marks of student {}: ".format(i+1))) # We can use {} for string formatting as  long as we use .format() method to replace the placeholders with actual values.without makin string a f-string we can use {} and .format() method to insert values into the string.
    marks.append(mark)  
marks.sort()
print("Marks in sorted order:", marks)'''

#Write a program to sum the all elements in a list of numbers.
numbers = [1,2,3,4,5]
total = sum(numbers)
print("Sum of all elements in the list:", total)