"""
This is the main file for the game Track Quest.
The game is based on the swedish TV-show "På spåret".
The goal is to guess the city from the clues given.
The game is built with inspiration from the youtube tutorial

"""

# Importing modules
import os
import sys
import time
import random
from question_data import questions



# Global variables
score = 0


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


# Main function. Short introduction to the game and asks for username.


def main():
    delprint(" Welcome to Track Quest!")
    delprint(" This game concept is from the swedish TV-show 'På spåret'")
    delprint(" The goal is to guess the city from the clues given")
    delprint(" The game will be played in 5 rounds.")
    delprint(" The rounds goes from 10 points to 2 points.")
    delprint(" You will get only one guess per destination!")
    delprint(" Remeber that a wrong answer will give you zero points!")
    delprint(" Enter your name to continue")

    while True:
        player_name = input(" Please enter your preferred username: ")
        if player_name:
            break
        print(" Username can not be empty, please try again.")
    # Print a blank line for formatting
    delprint(" Welcome " + player_name + "!")

    while True:
        compartment = input(" Do you want to sit in first class "
                            "or the handcar?")
        if compartment == "first class":
            delprint(" You have chosen first class")
            break
        elif compartment == "handcar":
            delprint(" You have chosen the handcar")
            time.sleep(3)
            break
        else:
            delprint(" Please choose between first class or handcar")


# Class for the questions

class Question:
    def __init__(self, category, points, text, answer):
        self.category = category
        self.points = points
        self.text = text
        self.answer = answer

        """
        A questions bank is created from the questions in the" "
        question_data.py file.
        The questions are sorted by category and points.
        Its inspired by Evan Mawyers quiz:
        https://medium.com/@Evan.mawyer/creating-a-quiz-using-python-oop-object-oriented-programming-3675a0ae687

        """


for i, question in enumerate(questions):
    if "points" not in question:
        print(f"Question {i} does not have a 'points' key: {question}")


question_bank = []
for question in questions:
    question_category = question["category"]
    question_points = question["points"]
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(
        question_category, question_points, question_text, question_answer
    )
    question_bank.append(new_question)

    # Randomize the order of the cities

cities = list(set(q.category for q in question_bank))
random.shuffle(cities)

# Limit the number of cities to 5 per game
cities = cities[:5]

for city in cities:
    city_questions = [q for q in question_bank if q.category == city]
    city_questions.sort(key=lambda q: q.points, reverse=True)


class Run_game:
    def __init__(self, question_bank, cities):
        self.question_bank = question_bank
        self.cities = cities
        self.score = 0

    def run(self):
        for city in self.cities:
            # Get all questions for this city
            city_questions = [
                q for q in self.question_bank if q.category == city]

            # Iterate over each question in order
            for question in city_questions:
                # Ask the question and get the user's answer
                delprint(question.text)
                user_answer = input(" Your answer: ")

                # Check if the user's answer is correct
                if user_answer.lower() == question.answer.lower():
                    delprint("Your answer is.....")
                    time.sleep(2)
                    print("Correct!")
                    delprint("You get " + str(question.points) + " points!")
                    delprint("Prepare for the next destination!")
                    self.score += question.points
                    break
                elif user_answer.lower() == "next":
                    continue  # Go to the next question within the same city
                elif user_answer.lower() != question.answer.lower():
                    delprint("Your answer is.....")
                    time.sleep(2)
                    print("Incorrect!")
                    delprint("The correct answer was: " + str(question.answer))
                    delprint("You get 0 points!")
                    delprint("Prepare for the next destination!")
                    break  # Move to the next city if the answer is incorrect

            else:
                # Continue to the next city if all questions have been asked
                continue
                # Break the city loop if a ques was answered correct/incorrect



game = Run_game(question_bank, cities)
game.run()
