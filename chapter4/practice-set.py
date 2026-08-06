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


#Only one element tuple
single_element_tuple = (5,)  #there is the comma after 5 because without the comma it will be considered as an integer and not a tuple. So to create a single element tuple we need to add a comma after the element. This is a common mistake that people make when creating single element tuples. They forget to add the comma and end up creating an integer instead of a tuple. So always remember to add a comma after the element when creating a single element tuple.   
print(single_element_tuple)
print(type(single_element_tuple))