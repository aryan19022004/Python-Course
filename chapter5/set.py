#Set in python
#A set is an unordered collection of unique elements. Sets are defined using curly braces {} or the built-in set() function. Sets are mutable, meaning that you can add or remove elements from a set after it has been created. However, since sets are unordered, they do not support indexing or slicing like lists or tuples.
#Creating a set 
my_set = {1, 2, 3, 'hello', True}
print(my_set)
print(type(my_set))
#Creating a set using the set() function
another_set = set([4, 5, 6, 'world', False])
print(another_set)
print(type(another_set))
#Sets automatically remove duplicate elements
duplicate_set = {1, 2, 2, 3, 3, 3}
print(duplicate_set)  # Output: {1, 2, 3}       
#Empty set
empty_set = set()
print(empty_set)
print(type(empty_set))

S1 = {1, 2, 3}
S2 = {3, 4, 5}
#Union of sets
union_set = S1.union(S2)
print("Union of S1 and S2:", union_set)  # Output: {1, 2, 3, 4, 5}
#Intersection of sets
intersection_set = S1.intersection(S2)
print("Intersection of S1 and S2:", intersection_set)  # Output: {3}
#Difference of sets
difference_set = S1.difference(S2)
print("Difference of S1 and S2 (S1 - S2):", difference_set)  # Output: {1, 2}
#Symmetric difference of sets
symmetric_difference_set = S1.symmetric_difference(S2)
print("Symmetric Difference of S1 and S2:", symmetric_difference_set)  # Output
# Output: {1, 2, 4, 5}

#Adding elements to a set
my_set.add(10)  
print(my_set)  # Output: {1, 2, 3, 'hello', True, 10}
#Removing elements from a set   
my_set.remove(2)
print(my_set)  # Output: {1, 3, 'hello', True, 10}      
#Note: If you try to remove an element that does not exist in the set using remove(), it will raise a KeyError. To avoid this, you can use the discard() method, which does not raise an error if the element is not found.
my_set.discard(5)  # This will not raise an error since 5 is not in the set
print(my_set)  # Output: {1, 3, 'hello', True, 10}

#Can we have 18 as a integer and also as an string simultaneously in a set?
my_set.add(18)  # Adding integer 18
my_set.add("18")  # Adding string "18"  
print(my_set)  # Output will include both 18 and "18" since they are different types