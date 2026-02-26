l = [1,2,4,5,7]

for index, value in enumerate(l):
    print(f"Index: {index}, Value: {value}")    

#List comprehension with enumerate
squared = [value**2 for index, value in enumerate(l)]
print(squared) 