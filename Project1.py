# Project1.py
# Author: Justin Agosto


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game

# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
# the return value should be a boolean (True or False) for whether the user was correct

# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).
print("Welcome to the quiz game!")
print("Here are the rules:")
print("You will be asked a series of questions.")
print("You will be given 4 options for each question.")
print("You will type in the letter of the answer you think is correct.")
print("If you get the answer correct, you will get 1 point.")
print("If you get the answer incorrect, you will get 0 points.")
print("Good luck!")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Mars", "B. Jupiter", "C. Saturn", "D. Earth"],
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Claude Monet"],
        "answer": "A"
    },
    {
        "question": "Who is the current president?",
        "options": ["A. Joe Biden", "B. Donald Trump", "C. George Washington", "D. Abraham Lincoln"],
        "answer": "A"
    },
    {
        "question": "What is a 1 cent coin made of?",
        "options": ["A. Iron", "B. Steel", "C. Copper", "D. Aluminum"],
        "answer": "C"
    }
]

score = 0


for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)

    user_answer = input("Enter your answer (A, B, C or D): ")

    
    if user_answer.upper() == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print()  

print("Quiz complete!")
print("Your score: {}/{}".format(score, len(questions)))
