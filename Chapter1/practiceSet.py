import os
'''
# Specify the directory path
directory_path = "."  # Current directory, change this to any path

try:
    # List all items in the directory
    items = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':\n")
    
    for item in items:
        item_path = os.path.join(directory_path, item)
        # Check if it's a file or directory
        if os.path.isdir(item_path):
            print(f"[DIR]  {item}")
        else:
            print(f"[FILE] {item}")
            
except FileNotFoundError:
    print(f"Directory '{directory_path}' not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")

'''
    #Question 3 

import pyttsx3
pyttsx3.speak("I will speak this text")
