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


# Clears the screen based on the user's operating system.
def clear():
    # for Windows
    if os.name == "nt":
        os.system("cls")
    # for Mac and Linux (here, os.name is 'posix')
    else:
        os.system("clear")


def main():
    print("Welcome to Track Quest!")
    print("This game concept is from the swedish TV-show 'På spåret'")
    print("The goal is to guess the city from the clues given")
    print("The game will be played in 5 rounds.")
    print("The rounds goes from 10 points to 2 points.")
    print("Enter your name to continue")

    while True:
        player_name = input("Please enter your preferred username: ")
        if player_name:
            break
        print("Username can not be empty, please try again.")
    # Print a blank line for formatting
    print("Welcome " + player_name + "!")


main()


def game_start():
    clear()
    print("Where are we heading?") 
    for question in questions:
        print(question["question"][0]["text"])


game_start()


def show_question():
    pass


def game_instructions():
    pass
