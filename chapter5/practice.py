a= {
    "name": "Aryan",
    "age": 25,
    "city": "New York",
    "country": "USA"
}

#print(a.keys())
#print(a.values())

#print(a.items())

b = a.copy() # here we are just copying the a to b 
c = a # here we are just assigning the reference of a to c

b["name"] = "Ayan"  # disctonaries are mutable so we can change the value of a key in the dictionary. Here we are changing the value of the key "name" in the dictionary b to "Ayan". This will not affect the dictionary a because we have created a copy of a and assigned it to b. So b is a new dictionary that has the same key-value pairs as a, but it is a different object in memory. Therefore, when we change the value of the key "name" in b, it does not affect the value of the key "name" in a. However, if we change the value of the key "name" in c, it will affect the value of the key "name" in a because c is just a reference to a and not a new object. So when we change the value of the key "name" in c, it changes the value of the key "name" in a as well because they are both referring to the same object in memory.
c["name"] = "Ayan"  # here we are changing the value of the
print(a) # Output: {'name': 'Aryan', 'age': 25, 'city': 'New York', 'country': 'USA'}
print(b) # Output: {'name': 'Ayan', 'age': 25, 'city': 'New York', 'country': 'USA'}

new_info = {"country": "India", "age": 26}
a.update(new_info) # here we are updating the dictionary a with the key-value pairs from

print(a) # Output: {'name': 'Ayan', 'age': 26, 'city': 'New York', 'country': 'India'}