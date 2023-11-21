# HW2.py
# Author: Justin Agosto


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:
age = int(input('Please enter a persons age.'))
# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."
if age < 13: print('The person is a child.')

if age >= 13 and age < 20: print('The person is a teenager.')

if age >=20: print ('The person is an adult.')


# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345
n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:
l = [int(input('Enter a number: ')) for i in range(10)]
print(max(l))
print(min(l))
print(sum(l)/len(l))
# The highest number.
# The lowest number.
# The average of all the numbers.

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    text = text.lower()

    for char in text:
        if char in vowels:
            count += 1

    return count

user_input = input("Enter text: ")
vowel_count = count_vowels(user_input)
print("Number of vowels:", vowel_count)