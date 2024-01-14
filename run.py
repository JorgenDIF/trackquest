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


def delprint(text, delay_time): 
    for character in text:      
        sys.stdout.write(character) 
        sys.stdout.flush()
        time.sleep(delay_time)
    print("")

  
# Clears the screen based on the user's operating system.
def clear():
    # for Windows
    if os.name == "nt":
        os.system("cls")
    # for Mac and Linux (here, os.name is 'posix')
    else:
        os.system("clear")


def main():
    delprint("Welcome to Track Quest!", 0.1)
    delprint("This game concept is from the swedish TV-show 'På spåret'", 0.1)
    delprint("The goal is to guess the city from the clues given", 0.1)
    delprint("The game will be played in 5 rounds.", 0.1)
    delprint("The rounds goes from 10 points to 2 points.", 0.1)
    delprint("Enter your name to continue", 0.1)

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

    delprint("Where are we heading?", 0.1) 
    for question in questions:
        delprint(question["question"][0]["text"], 0.1)


game_start()


def show_question():
    pass


def game_instructions():
    pass
