"""
User se number leke check karo even ya odd

3 numbers me se largest find karo

Leap year check karo

Number positive, negative ya zero check karo

Simple calculator banao (add, sub, mul, div)

Factorial of a number (loop se)

Factorial using recursion

Fibonacci series print karo n terms tak

Prime number check karo

1 se 100 tak sab prime print karo

Number reverse karo

Palindrome number check karo

Armstrong number check karo

Sum of digits find karo

Count digits in number

Multiplication table print karo

Pattern print karo (star triangle)

Number guessing game banao

Random password generator

Sum of first n natural numbers

"""

#1. Even Odd Check
"""
number = int(input("Enter a number"))

if(number % 2 == 0):
    print("Even")
else:
    print("Odd")

"""

#2. Largest of 3 numbers

'''

num1 = int(input("Enter you first number"))
num2 = int(input("Enter you second number"))
num3 = int(input("Enter you third number"))
largest = 0
if(num1 >num2 and num1>num3 ):
    largest = num1
elif(num2>num1 and num2>num3):
    largest = num2
else:
    largest = num3
print(f"The largest number is {largest}")

'''

#3. Leap Year Check

'''
year = int(input("Enter The year"))
if(year%4 == 0 and year%100!=0) or (year%400 == 0):
    print("This is the leap year")
else:
    print("This is not the leap year")
    
'''

#4. Positive, Negative or Zero Check

'''
num = int(input("Enter the number"))

if(num>0):
    print("the number is the positive")
elif(num<0):
    print("The number is the negative")
else:
    print("the number is 0")

'''

#5. Simple Calculator
'''
num1 = int(input("enter first number"));
num2 = int(input("enter the second number"))

print("enter 1 for addition\nenter 2 for difference\nenter 3 for multiplication.\n")
o = int(input("Enter operation"))

def calculator(num1,num2,oper):
    if(oper == 1):
        return num1 + num2
    elif(oper == 2):
        return num1 - num2
    elif(oper == 3):
        return num1*num2
    else:
        return "Invalid operation"

result = calculator(num1,num2,o);

print(result)

'''
#6. Factorial of a number using loop

'''
def factorial(num):
    factorial = 1
    while num>0:
        factorial = factorial*num
        num = num-1
    
    return factorial

int a = int(input("Enter the number"))
print(f"factorial of {a} is {factorial(a)}")
    
'''

#7. Factorial using recursion
'''
def factorial(num):
    
    if(num == 0 or num ==1):
        return 1
    else:
        return num*factorial(num-1)

print(factorial(5))
'''

#8. Fibonacci series print karo n terms tak
'''
def fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1
n = int(input("Enter the number of terms"))
fibonacci(n)

'''

#9. Prime number check karo

'''
def prime(n):
    if n <= 1:
        print("Not a prime number")
        return
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("This is not a prime number")
            break
    else:
        print("This is a prime number")

num = int(input("Enter the number: "))
prime(num)
'''

#10. 1 se 100 tak sab prime print karo
'''
def prime():
    primes = []
    
    for i in range(2, 100):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    
    return primes

print(prime())
'''

#11. Number reverse karo
'''
def reverse(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev
num = int(input("Enter the number: "))
print(f"The reverse of {num} is {reverse(num)}")



#12. Palindrome number check karo
def palindrome(num):
    return num == reverse(num)
num = int(input("Enter the number: "))
if palindrome(num):
    print(f"{num} is a palindrome number")
else:    print(f"{num} is not a palindrome number")

'''

#13. Armstrong number check karo
'''
def Armstrong(n):
    original = n
    result = 0
    while n >0:
         a =  n%10
         result = result + a**3
         n = n//10
    if(result == original):
        print("This is the armstrong number")
    else:
        print("This is not the Arm strong number")
        
Armstrong(153)
      
'''

#14. Sum of digits find karo
'''
def SumOfDigits(n):
    sum = 0
    while n>0:
        digit = n%10
        sum = sum + digit
        n = n//10
    return sum

print(SumOfDigits(567))
'''
#15. Count digits in number

'''
def NoOfDigits(n):
    count = 0
    while n >0:
        count = count+1
        n = n//10
    return count
print(NoOfDigits(1567))
'''
#16. Multiplication table print karo
'''
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}\n")
    else:
        print("Done")
table(6)
'''

#17. Pattern print karo (star triangle)
'''def pattern(n):
    for i in range(1, n+1):
        print("* " * i)
pattern(5)

'''

#18. Number guessing game banao
'''
import random

secret_number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess > secret_number:
        print("Too High ")
    elif guess < secret_number:
        print("Too Low ")
    else:
        print("Congratulations  You guessed it right!")
        break
'''
#19. Random password generator
'''import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password_length = int(input("Enter the desired password length: "))
print(f"Generated Password: {generate_password(password_length)}")

'''
#20. Sum of first n natural numbers

'''
def sum(n):
    result = 0
    for i in range(1,n+1):
        result = result + i
    return result

print(f"The sum of the first {5} natural numbers is {sum(5)}")

'''


