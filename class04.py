#stored variable name
#created an empty list
#asking user for their name

name = input("Enter your name: ")  

#created an empty list
#asked user for their favorite number
favorite_number = [] 


#used a for loop to ask for 3 numbers
#appended the numbers to the list
#printed out the list
for i in range(1,4):
    number = int(input("Enter your favorite number {i}:"))
    favorite_number.append(number)
print(f"Hello {name} lets explore your favorite numbers {favorite_number}.")


#even, odd info 
#created a list
#used a for loop and if statement to check if the number is even or odd and used a tuple 
#appended the number and even or odd to the list

even_odd_info = []
for number in favorite_number:
    if number % 2 == 0:
        even_odd_info.append((number, "even"))
    else:even_odd_info.append((numbers, "odd"))


#squared numbers
#created a for loop and squared the numbers in the list
#printed out the list with the squared numbers using f string
print("Here are numbers and their equares:")
for number in favorite_number:
    print(f"{number} squared is{number **2}")


#Calculate the Sum of the Numbers
#created a function
#printed out the total sum of the numbers
total_sum = sum(favorite_number)
print(f"The sum of your favorite numbers is {total_sum} Great choice {name}!")


#Check if the Sum is a Prime Number
#created a function 
#used a for loop to check if the sum is a prime number
#used a if statement with f string to print out if the sum is a prime number

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i ==0:
            return True
if is_prime(total_sum):
    print(f"WOW! The sum {total_sum} is a prime number. ")
else:
    print(f"The sum {total_sum} is not a prime number.")

