# Python Programming Assignment 02
# Instructions: Implement Python programs to accomplish the following tasks
# Hint: When asking the user for input in your Python program, use the input() method. This method allows you to prompt the user for information and capture their response.
# Add two numbers
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.

input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))

print(f"The sum of the two numbers is: {input1 + input2}")



# Agreement Boot
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
# What's your favorite animal? cow
# My favorite animal is also cow!

user_favorite = input("What's your favorite animal? ")

print(f"My favorite animal is also {user_favorite}!")   


# Fahrenheit to Celsius Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!
# The equation you should use for converting from Fahrenheit to Celsius is the following:
# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
# (Note. The .0 after the 5 and 9 matters in the line above!!!)
# Here's a sample run of the program (user input is in bold italics):
# Enter temperature in Fahrenheit: 76
# Temperature: 76.0F = 24.444444444444443C

input1 = float(input("Enter temperature in Fahrenheit: "))

print(f"Temperature: {input1}F = {(input1 - 32) * 5.0 / 9.0}C") 


# riangle Perimeters Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
# Here's a sample run of the program (user input is in bold italics):
# What is the length of side 1? 3
# What is the length of side 2? 4
# What is the length of side 3? 5.5
# The perimeter of the triangle is 12.5

input1 = float(input("What is the length of side 1? "))
input2 = float(input("What is the length of side 2? "))
input3 = float(input("What is the length of side 3? "))

print(f"The perimeter of the triangle is {input1 + input2 + input3}")   


# Square Number Ask the user for a number and print its square (the product of the number times itself).
# Here's a sample run of the program (user input is in bold italics):
# Type a number to see its square: 4
# 4.0 squared is 16.0

input1 = float(input("Type a number to see its square: "))

print(f"{input1} squared is {input1 * input1}")


# Delete a number Consider a list named numbers with the elements [1, 2, 3, 4, 5]. Use list method to delete the number 3?

# Creating a list You have two lists:

# list1 with elements [1, 2, 3]
# list2 with elements [4, 5, 6].
# Create a program using list method to add the elements of list2 to list1.
# Pop method You have a list named items with the elements [10, 20, 30, 40]. If you use the pop method without any arguments, what will the list look like and what value will be removed?
# Index Method You have a list called colors with the elements ['red', 'blue', 'green', 'yellow']. If you use the index method to find the position of 'green', what will the index be?

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)  # This will remove the number 3 from the list
print(numbers)  # Output will be [1, 2, 4, 5]


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # This will add all elements of list2 to list1
print(list1)  # Output will be [1, 2, 3, 4, 5, 6]


items = [10, 20, 30, 40]
removed_value = items.pop()  # Removes the last item, which is 40
print(items)  # Output will be [10, 20, 30]
print(removed_value)  # Output will be 40


colors = ['red', 'blue', 'green', 'yellow']
index_of_green = colors.index('green')  # This will return the index of 'green'
print(index_of_green)  # Output will be 2



# Challenge Questions
# Get last element Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
# Get a List Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1
# Enter a value: 2
# Enter a value: 3
# Enter a value:
# Here's the list: ['1', '2', '3']

def get_last_element(lst):
    # Print the last element of the list
    print(lst[-1])

# Check if the input is a valid list
def get_last_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")
    # Check if the list is empty
    if len(lst) == 0:
        raise ValueError("List is empty")
    # Print the last element of the list
    print(lst[-1])

# Example usage
sample_list = [1, 2, 3, 4, 5]
get_last_element(sample_list)  # Output will be 5


