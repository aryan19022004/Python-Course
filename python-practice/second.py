'''
String reverse karo

Palindrome string check karo

Count vowels in string

Count consonants

Count words in sentence

Remove spaces from string

Convert lowercase to uppercase without using built-in

Find frequency of each character

Replace specific word in string

Check anagram

Remove duplicate characters

First non-repeating character find karo

Capitalize first letter of every word

Count digits in string

Remove punctuation

Check substring present hai ya nahi

Most frequent character

Swap two strings without temp variable

Print ASCII value of each character

Check string contains only digits
'''

# String reverse
def reverse_string(s):
    return s[::-1]
a = "Hello World"
print(reverse_string(a))

# Palindrome check
def is_palindrome(s):
    return s == s[::-1]
b = "madam"
print(is_palindrome(b))

# Count vowels
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
c = "Hello World"
print(count_vowels(c))

# Count consonants
def count_consonants(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

print(count_consonants(c))

# Count words in sentence
def count_words(s):
    words = s.split()
    return len(words)
d = "Hello World, how are you?"
print(count_words(d))

# Remove spaces from string
def remove_spaces(s):
    return s.replace(" ", "")
e = "Hello World"
print(remove_spaces(e))

# Convert lowercase to uppercase without using built-in
def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result
f = "hello world"
print(to_uppercase(f))

# Find frequency of each character
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
g = "hello world"
print(char_frequency(g))

# Replace specific word in string
def replace_word(s, old, new):
    return s.replace(old, new)
h = "Hello World"
print(replace_word(h, "World", "Python"))

# Check anagram
def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())
i1 = "listen"
i2 = "silent"
print(are_anagrams(i1, i2))

# Remove duplicate characters
def remove_duplicates(s):
    result = ""
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result
j = "hello world"
print(remove_duplicates(j))

# First non-repeating character
def first_non_repeating(s):
    frequency = char_frequency(s)
    for char in s:
        if frequency[char] == 1:
            return char
    return None
k = "hello world"
print(first_non_repeating(k))

# Capitalize first letter of every word
def capitalize_words(s):
    words = s.split()

    capitalized = [word.capitalize() for word in words]
    return " ".join(capitalized)
l = "hello world"
print(capitalize_words(l))

# Count digits in string
def count_digits(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count
m = "Hello123"
print(count_digits(m))

# Remove punctuation
import string   
def remove_punctuation(s):
    return s.translate(str.maketrans("", "", string.punctuation))
n = "Hello, World!"
print(remove_punctuation(n))

# Check substring present hai ya nahi
def is_substring(s, substring):
    return substring in s
o = "Hello World"
print(is_substring(o, "World"))

# Most frequent character
def most_frequent_char(s):
    frequency = char_frequency(s)
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent
p = "hello world"
print(most_frequent_char(p))

# Swap two strings without temp variable
def swap_strings(s1, s2):
    s1 = s1 + s2
    s2 = s1[:len(s1) - len(s2)]
    s1 = s1[len(s2):]
    return s1, s2
q1 = "Hello"
q2 = "World"
print(swap_strings(q1, q2))

# Print ASCII value of each character
def ascii_values(s):
    return {char: ord(char) for char in s}
r = "Hello"
print(ascii_values(r))

# Check string contains only digits
def is_digits_only(s):
    return s.isdigit()
s1 = "12345"
s2 = "Hello123"
print(is_digits_only(s1))  # True
print(is_digits_only(s2))  # False

# String slicing
t = "Hello World"
print(t[0:5])  # Output: Hello
print(t[6:])   # Output: World
