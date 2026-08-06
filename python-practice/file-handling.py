'''
🔹 PART 6: File Handling Practice (10 Questions)

Write text into file

Read file and count words

Count lines in file

Count characters

Append data to file

Search specific word in file

Replace word in file

Copy content of one file to another

Store student data in file

Create login system using file
'''

# Write text into file
with open("example.txt","w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("This file is used to demonstrate file I/O in Python.\n")

    
with open("example.txt","r") as file:
    content = file.read()
print("File Content:")
print(content)

# Append data to file
with open("example.txt","a") as file:
    file.write("This is the lined added when practicing the Append mode.\n")
with open("example.txt","r") as file:
    content = file.read()
print("Updated File Content:")
print(content)


# Using with statement for better file handling
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content using with statement:")
    print(content)

# Count words in file
with open("example.txt","r") as file:
    content = file.read()
    words = content.split()
    print(f"Number of words in the file: {len(words)}")

# count characters in file
with open("example.txt", "r") as file:
    content = file.read()
    print("Total characters in file:", len(content))


#Count lines in file
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Total lines in file:", len(lines))

# Search specific word in file
search_word = "land"
with open("example.txt","r") as file:
    content = file.read()
    if(search_word in content):
        print(f"The {search_word} is available in the file")
    else:
        print(f"This word is not available in the file")

# Replace word in file
old_word = "sample"
new_word = "example"
with open("example.txt", "r") as file:
    content = file.read()
    updated_content = content.replace(old_word, new_word)
with open("example.txt", "w") as file:
    file.write(updated_content)
print("File content after replacing word:")
with open("example.txt", "r") as file:
    print(file.read())  

# Copy content of one file to another
with open("example.txt","r") as file:
    content = file.read()

with open("example2.txt","w") as file:
    file.write(content)
    
with open("example2.txt","r") as file:
    content2 = file.read()
    print(content2)

# Store student data in file
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A"},
]
with open("students.txt", "w") as file:
    for student in students:
        file.write(f"{student['name']}, {student['age']}, {student['grade']}\n")
print("Student data stored in students.txt")

#Storing Data in file using json
import json
with open("students.json", "w") as file:
    json.dump(students, file)
print("Student data stored in students.json")

#Reading the json data from the students.json file
with open("students.json", "r") as file:
    students_data = json.load(file)
print("Student data read from students.json:")
for student in students_data:
    print(student)


# Create login system using file
def register_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("User registered successfully.")

def login_user(username, password):
    with open("users.txt", "r") as file:
        users = file.readlines()
        for user in users:
            stored_username, stored_password = user.strip().split(",")
            if stored_username == username and stored_password == password:
                print("Login successful!")
                return True
    print("Invalid username or password.")
    return False
# Example usage
register_user("john_doe", "password123")
login_user("john_doe", "password123")
login_user("john_doe", "wrongpassword")




    
    
