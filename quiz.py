# Fun quiz to test your friends knowledge - focused on general trivia

# Import modules, libraries
import time 


# List of questions presented as tuples
questions = [
    ("What country has the highest life expectancy?\n", "Hong Kong"),
    ("How many bones do humans have in an ear?\n", "3"),
    ("What company was initially known as 'Blue Ribbon Sports'?\n", "Nike"),
    ("What is a group of pandas known as?\n", "Embarrassment")
]


# Keep score of user's points in the quiz 
score = 0


# Welcome users to the quiz 
print("Welcome! It's time to test your knowledge!")

# Check if user is ready to play by asking them to type Start
playing = input("Type 'Start' to begin your game.\n")

# Have a bit of fun and quit the program if user's input is not equal to Start
if playing != "Start":
    print("Hey, hey, hey, try again!")
    quit()

# Acknowledge succcessful start to the quiz
print("Time to begin your journey, Player.")

# Ask questions
for question in questions:
    answer = input(question[0])

    # Check if user-provided answer is correct
    if answer.lower() == question[1].lower(): 
        # Increase user's score count by 1
        score += 1
        # Acknowledge correct answer
        print(f"Oh yeahhh! Well done, Player! Your score is {score}.")
        time.sleep(3)
        print("### ### ###")
    else: 
        # Say that answer was incorrect 
        print(f"Oh nooo! That doesn't seem to be right. Your score is {score}.") 
        time.sleep(3)
        print("### ### ###")

# Print total score and thank user
print(f"Your total score is {score}.\nThanks for playing!")


