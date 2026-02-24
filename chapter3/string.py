# String slicing
name = "Aryan"
print(len(name))  # Output: 5
print(name[0])  # Output: A
print(name[1])  # Output: r
print(name[1:4])  # Output: rya
print(name[:3])  # Output: Ary

#Negative slicing
print(name[-1])  # Output: n
print(name[-2])  # Output: a
print(name[-3:-1])  # Output: ya
print(name[:])

#Slicing With Step
print(name[0:4:2])  # Output: Ayan

#String Methods
name = "aryan"
print(name.upper())  # Output: ARYAN
print(name.lower())  # Output: aryan
print(name.capitalize())  # Output: Aryan
print(name.title())  # Output: Aryan
print(name.strip())  # Output: aryan
print(name.replace("a", "o"))  # Output: oryon
print(name.split("a"))  # Output: ['ary', 'n']
print(name.find("a"))  # Output: 1
print(name.count("a"))  # Output: 2 
print(name.startswith("a"))  # Output: True
print(name.endswith("n"))  # Output: True