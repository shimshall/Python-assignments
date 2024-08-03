# Age Assignments Based on the Riddle

# Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.

anton_age = 21
beth_age = 6
chen_age = 20
drew_age = chen_age + anton_age
ethan_age = chen_age

print(f"Anton is {anton_age}")
print(f"Beth is {beth_age}")
print(f"Chen is {chen_age}")
print(f"Drew is {drew_age}")
print(f"Ethan is {ethan_age}")

# Formatted String Interpolation

# Task: Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables.
# name:str = "Alice"
# age:int = 30
# city:str = "New York"

name : str = "Alice"
age : int = 30
city : str = "New York"

print(f"{name} is {age} years old and lives in {city}.")

# String Manipulation

# Task: Given the string s, use string methods to:
# Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
# Convert to uppercase: change all characters in the string to uppercase.
# Convert to lowercase: change all characters in the string to lowercase.
# s:str = "hElLo WoRlD"
# Expected Output:
# Hello world
# HELLO WORLD
# hello world

s : str = "hElLo WoRlD"
print(s.capitalize())
print(s.upper())
print(s.lower())    

# Substring Search

# Task: Given the string s, use string methods to:
# Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.
# Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.
# s:str ="the quick brown fox jumps over the lazy dog"
# Expected Output:
# index of 'fox' is 16
# 'the' appears 2 times

s : str = "the quick brown fox jumps over the lazy dog"
print(s.find("fox"))
print(s.count("the"))

# String Replacement

# Task: Given the string s, use string methods to:
# Replace "Python" with "Java": substitute "Python" with "Java".
# s:str ="I love programming in Python"
# Expected Output:
# I love programming in Java

s : str = "I love programming in Python"
print(s.replace("Python", "Java"))  

# String Splitting and Joining

# Task: Given the string s, use string methods to:
# Split into a list: break the string into a list of substrings based on the delimiter ,.
# Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
# s:str ="apple,banana,cherry,dates"
# Expected Output:
# ["apple", "banana", "cherry", "dates"]
# apple banana cherry dates

s : str = "apple,banana,cherry,dates"
print(s.split(","))
print(" ".join(s.split(",")))

# String Stripping and Justifying

# Task: Given the string s, use string methods to:
# Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
# Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
# Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
# s:str ="   Python is fun!   "
# Expected Output:
# Python is fun!
# Python is fun!*****
# *****Python is fun!

s : str = "   Python is fun!   "
print(s.strip())
print(s.ljust(20, "*"))
print(s.rjust(20, "*"))

# Convert an integer to its binary representation

# Task: Given an integer num
# Obtain the binary representation of num
# num:int = 45
# Expected Output:
# Binary representation : 0b101101

num : int = 45
print(bin(num))


# Calculate Powers of Numbers.

# Task: Given two integers base and exponent
# Compute base raised to the power of exponent.
# base:int = 3
# exponent:int = 4
# Expected Output:
# Power result: 81

base : int = 3
exponent : int = 4
print(pow(base, exponent))

# Round floating-point numbers

# Task: Given a floating-point number value
# Round value to the nearest integer.
# Round value to two decimal places.
# value:float = 12.34567
# Expected Output:
# Rounded to nearest integer: 12
# Rounded to two decimal places: 12.35

value : float = 12.34567
print(round(value))
print(round(value, 2))


# Assignments_01_Complete.txt