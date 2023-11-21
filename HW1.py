# HW1.py
# Author: Justin agosto

# Question 1:
# Print Hello World like we did in class
print("Hello World")
# Question 2:
# Print the following:
# Your name
print("Justin Agosto")
# Your age
print("18")
# Your favorite color
print("purple")
# Your favorite animal
print("dog")
# Question 3:
# Create a variable called "myName" and set it equal to your name
myName= " Justin Agosto"
# Create a variable called "myAge" and set it equal to your age
myAge= " 17"
# Create a variable called "myColor" and set it equal to your favorite color
myColor= " pruple"
# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal= " dog"
# Print the following:
# Hello, my name is <myName>
print("Hello my name is" + myName)
# I am <myAge> years old
print("I am" + myAge)
# My favorite color is <myColor>
print("My favorite color is" + myColor)
# My favorite animal is <myAnimal>
print("My favorite animal is" + myAnimal)


# Question 4:
# Calculate the following and print the result:
# 2 + 2
print(2 + 2)
# 3 * 4
print(3 * 4)
# 5 - 6
print(5 - 6)
# 8 / 2
print(8 / 2)
# Question 5:
# Create a variable called "num1" and set it equal to 2
num1= 2
# Create a variable called "num2" and set it equal to 3
num2= 3
# Create a variable called "num3" and set it equal to 4
num3= 4
# Create a variable called "num4" and set it equal to 5
num4= 5
# Calculate the following and print the result:
# num1 + num2
print(num1 + num2)
# num3 * num4
print(num3 * num4)
# num4 - num1
print(num4 - num1)
# num2 / num1
print(num2 / num1)
# Question 6: Write a program that asks the user for their name and then prints the following:
name = input("Enter Name: ")
# Hello, <name>. Please enter three numbers.
print("Hello " + name)

# The program should then ask the user for three numbers (floats) and print the following:
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

# 1. The sum of the three numbers is <sum>
sum = a + b + c
print("The sum of the three numbers is", sum)

# 2. The product of the three numbers is <product>
product = a * b * c
print("The product of the three numbers is", product)

# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3
rounded_sum = round(a) + round(b) + round(c)
average = rounded_sum / 3
print("The average of the three numbers is", average)
# 4. The average of the three numbers is <average>

# Question 7: Ask the user for an input of a symbol (in the example its *)     
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.
input_symbol = input("Enter a symbol: ")
n = 9
for a1 in range(1, (n+1)//2 + 1): #from row 1 to 5
    for a2 in range((n+1)//2 - a1):
        print(" ", end = "")
    for a3 in range((a1*2)-1):
        print("*", end = "")
    print()

for a1 in range((n+1)//2 + 1, n + 1): #from row 6 to 9
    for a2 in range(a1 - (n+1)//2):
        print(" ", end = "")
    for a3 in range((n+1 - a1)*2 - 1):
        print("*", end = "")
    print()
#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
