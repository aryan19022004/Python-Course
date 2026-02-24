a = 1   # This is the inter variable a, which is assigned the value 1
b = 1.5 # This is the float variable b, which is assigned the value 1.5
c = "Hello" # This is the string variable c, which is assigned the value "Hello"
d = True # This is the boolean variable d, which is assigned the value True
e = None # This is the None variable e, which is assigned the value None
A = 2 # This is the inter variable A, which is assigned the value 2
print(a,A) # This will print the values of a and A, which are 1 and 2 respectively

f = A == a # This is the boolean variable f, which is assigned the value of the expression A == a, which is False
print(f) # This will print the value of f, which is False

#Logical operators
g = (A == a) and (b > 1) # This is the boolean variable g, which is assigned the value of the expression (A == a) and (b > 1), which is False
h = (A == a) or (b > 1) # This is the boolean variable h, which is assigned the value of the expression (A == a) or (b > 1), which is True
print(g,h) # This will print the values of g and h, which are False and True respectively

#Truth table for and operator
print("A\tB\tA and B")
print("False\tFalse\t", False and False)
print("False\tTrue\t", False and True)
print("True\tFalse\t", True and False)
print("True\tTrue\t", True and True)

#Truth table for or operator
print("A\tB\tA or B")
print("False\tFalse\t", False or False)
print("False\tTrue\t", False or True)
print("True\tFalse\t", True or False)
print("True\tTrue\t", True or True)