#File input and output
#Open a file for writing
file = open("example.txt", "w")
#Write some text to the file
file.write("Hello, this is a sample file.\n")
file.write("This file is used to demonstrate file I/O in Python.\n")
#Close the file
file.close()

#Open the file for reading
file = open("example.txt", "r")
#Read the contents of the file
content = file.read()
print("File Content:")
print(content)
#Close the file
file.close()

file = open("example.txt", "a")
file.write("This line is appended to the file.\n")
file.close()
print("Updated File Content:")
file = open("example.txt", "r") 
print(file.read())
file.close()

#Using with statement for better file handling
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content using with statement:")
    print(content)
