import random
import time
import os

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


def clear():
    """
    Function to clear the terminal on windows, mac and
    linux for a better user experience.
    """
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
    score = 0
    for question in questions:
        print(question["question"][0]["text"])


game_start()


def show_question():
    pass


def game_instructions():
    pass
