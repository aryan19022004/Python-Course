#Tuples in python are similar to lists, but they are immutable, meaning that once a tuple is created, its elements cannot be changed. Tuples are defined using parentheses () instead of square brackets [].    
#Creating a tuple
my_tuple = (1, 2, 3, 'hello', True)
print(my_tuple)
print(type(my_tuple))

#accessing elements in a tuple
print(my_tuple[0])  # Output: 1

#Tuples can also contain other tuples
nested_tuple = (1, 2, (3, 4), 'hello')
print(nested_tuple)
print(nested_tuple[2])  # Output: (3, 4)

#Only one element tuple
single_element_tuple = (5,)
print(single_element_tuple)
print(type(single_element_tuple))

#Methods in tuples
#Tuples have only two built-in methods: count() and index()
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))  # Output: 2
print(my_tuple.index(2))  # Output: 1 (first occurrence of 2)