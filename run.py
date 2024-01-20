"""
This is the main file for the game Track Quest.
The game is based on the swedish TV-show "På spåret".
The goal is to guess the city from the clues given.
The game is built with inspiration from the youtube tutorial

"""

# Importing modules
import random
import time
import os
import sys

# Global variables
score = 0

questions = [
    {
        "city": "1",
        "question": [
            {
                "points": 10,
                "text": "10 points: This city is the capital of Sweden",
                "answer": "Stockholm",
            },
            {
                "points": 8,
                "text": "This city is the home of DIF",
                "answer": "Stockholm",
            },
        ],
    }
]


"""
 Function to print text with a delay between each character. 
 Credit to: https://replit.com/talk/learn/The-Slow-Print/44741
 """


def delprint(text, delay_time=0.1):
    # Delayed printing function
    for character in text:
        sys.stdout.write(character)  # writes the character
        sys.stdout.flush()
        time.sleep(delay_time)  # this is the delay time between each
    print()  # make a new line


# Clears the screen based on the user's operating system.
def clear():
    # for Windows
    if os.name == "nt":
        os.system("cls")
    # for Mac and Linux (here, os.name is 'posix')
    else:
        os.system("clear")


def main():
    delprint("Welcome to Track Quest!")
    delprint("This game concept is from the swedish TV-show 'På spåret'")
    delprint("The goal is to guess the city from the clues given")
    delprint("The game will be played in 5 rounds.")
    delprint("The rounds goes from 10 points to 2 points.")
    delprint("You will get only one guess per destination!")
    delprint("Remeber that a wrong answer will give you zero points!")
    delprint("Enter your name to continue")

    while True:
        player_name = input("Please enter your preferred username: ")
        if player_name:
            break
        print("Username can not be empty, please try again.")
    # Print a blank line for formatting
    delprint("Welcome " + player_name + "!")

    while True:
        compartment = input("Do you want to sit in first class " "or the handcar?")
        if compartment == "first class":
            delprint("You have chosen first class")
            break
        elif compartment == "handcar":
            delprint("You have chosen the handcar")
            time.sleep(3)
            break
        else:
            delprint("Please choose between first class or handcar")


main()


def game_start():
    clear()

    delprint("Where are we heading?")
    for question in questions:
        delprint(question["question"][0]["text"])


game_start()


def show_question():
    pass


def game_instructions():
    pass
