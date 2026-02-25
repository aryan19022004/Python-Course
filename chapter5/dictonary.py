#Dictonary in Python
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are defined using curly braces {} and key-value pairs are separated by commas.   
#Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

#Empty dictionary
empty_dict = {}
print(empty_dict)
print(type(my_dict))

#methods in dictionary
#1. keys() - returns a view object that displays a list of all the keys in the dictionary.
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
#2. values() - returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values())  # Output: dict_values(['Alice', 30, 'New York'])
#3. items() - returns a view object that displays a list of dictionary's key-value tuple pairs.     
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
#4. get() - returns the value for the specified key if the key is in the dictionary, otherwise it returns None (or a default value if provided).
print(my_dict.get("name"))  # Output: Alice 
print(my_dict.get("country", "Not Found"))  # Output: Not Found (since 'country' key does not exist)
#5. update() - updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs.
new_info = {"country": "USA", "age": 31}
my_dict.update(new_info)
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}