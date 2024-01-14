import random
import time
import os


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


questions = [
   { 
    "city": "1",
    "questions": [
        {"points": 10, "text": "This city is the capital of Sweden", "answer": "Stockholm"},
        {"points": 8, "text": "This city is the home of DIF", "answer": "Stockholm"}
    ]
   }
]
print(questions)


def game_instructions():
    pass


def game_start():
    score = 0
    for question in questions:
        print(question["1 ,10 points"])
        answer = input("Answer: ")
        if answer == question["answer"]:
            score += 10
            print("Correct! Your score is now " + str(score))
        else:
            print("Wrong! Your score is still " + str(score))


def show_question():
    pass
