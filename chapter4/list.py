#Lists in Python
# A list is a collection of items which is ordered and changeable. In Python, lists are written with square brackets [].
#Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list) # Output: [1, 2, 3, 4, 5]
#Accessing items in a list
print(my_list[0]) # Output: 1


#List can contain different types of data
my_list = [1, "Hello", 3.14, True]
print(my_list) # Output: [1, 'Hello', 3.14, True]
#List can also contain other lists
my_list = [1, [2, 3], 4]
print(my_list) # Output: [1, [2, 3], 4]
#List methods
my_list.append(6)
print(my_list) # Output: [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0)
print(my_list) # Output: [0, 1, 2, 3, 4, 5, 6]
my_list.insert(3, 2.5)
print(my_list) # Output: [0, 1, 2, 2.5, 3, 4, 5, 6]
my_list.remove(2.5)
print(my_list) # Output: [0, 1, 2, 3, 4, 5, 6]
my_list.pop()   
print(my_list) # Output: [0, 1, 2, 3, 4, 5]
my_list.pop(0)
print(my_list) # Output: [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list) # Output: [5, 4, 3, 2, 1]

my_list[0] = 10
print(my_list) # Output: [10, 4, 3, 2, 1]
my_list.clear()
print(my_list) # Output: []

#If we are performing any method on list then it doest not create another list it just modifies the existing list. So it is not necessary to assign the result of the method to a new variable. For example, if we want to reverse a list then we can simply call the reverse method on the list and it will reverse the list in place. We do not need to assign the result of the reverse method to a new variable.
