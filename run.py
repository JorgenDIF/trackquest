
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


class Question:
    """
    A class to represent a question.
    """
    def __init__(self, category, points, text, answer):
        self.category = category
        self.points = points
        self.text = text
        self.answer = answer


class RunGame:
    """A class to represent the game.

    This class takes a list of questions as input
    and creates a list of Question objects from
    the input list. It also creates a list of cities
    from the input list, randomizes the order of the cities, and sorts the
    questions by points using a lambda function. I learned about lambda
    functions studying the following website:
    https://sparkbyexamples.com/python/sort-using-lambda-in-python/amp/

    The main idea is inspired by
    https://github.com/sampathbasa/quiz-app/tree/main.
    Changes have been made to the original code to fit this game.
    Some suggestions from my mentor have also been
    implemented to improve the code. """

    def clear(self):
        """Clears the screen based on the user's operating system."""
        # for Windows
        if os.name == "nt":
            os.system("cls")
        # for Mac and Linux (here, os.name is 'posix')
        else:
            os.system("clear")

    def delprint(self, text, delay_time=0.04):
        """
        Function to print text with a delay between each character.
        Credit to: https://replit.com/talk/learn/The-Slow-Print/44741
        """
        for character in text:
            sys.stdout.write(character)  # writes the character
            sys.stdout.flush()
            time.sleep(delay_time)  # this is the delay time between each
        print()  # make a new line

    def intro(self):
        """Prints the introduction to the game and asks the user
        for their name. Also a choice between first classhand or handcar.
        It´s just for fun and has no impact on the game.
        """
        self.clear()

        self.delprint(" Welcome to Track Quest!\n"
                      " Inspired by the Swedish TV-show 'På spåret,'\n"
                      " guess the city in 5 rounds\n"
                      " with points decreasing from 10 to 2.\n"
                      " One guess per destination;"
                      "a wrong answer gets zero points.\n"
                      " Type 'next' to move down a point level if unsure,\n"
                      " and save your guess to the next point level\n"
                      " Choose a username to begin.")

        while True:
            player_name = input(" Please enter your preferred username "
                                "max 10 letters: ")
            if player_name:
                if len(player_name) <= 10:
                    break
            print(" Please choose a username of max 10 letters.")
        # Print a blank line for formatting
        self.delprint(" Welcome " + player_name + "!")

        while True:
            self.delprint(" Choose if you want to sit in first class or\n"
                          " in the handcar. It makes no difference \n"
                          " to the game, but it's more fun to choose.")
            compartment = input(" Do you want to sit in first class\n"
                                " or the handcar? Choose one to continue: ")
            if compartment == "first class":
                self.delprint(" You have chosen first class")
                break
            if compartment == "handcar":
                self.delprint(" You have chosen the handcar")
                time.sleep(3)
                break
            self.delprint(" Please choose between first class or handcar")

    def __init__(self, question_list):
        self.question_list = question_list

        question_bank = []
        for question in self.question_list:
            question_category = question["category"]
            question_points = question["points"]
            question_text = question["text"]
            question_answer = question["answer"]
            new_question = Question(
                question_category, question_points, question_text,
                question_answer
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

        self.inner_question_bank = question_bank
        self.inner_cities = cities
        self.score = 0
        self.cities_visited = 0

    def run(self):
        """
        Runs the game.
        This method iterates over each city in`self.inner_cities`.
        For each city, it retrieves all questions associated with
        that city from `self.inner_question_bank`.  It then asks
        each question in order,accepting user input for the answer.

        If the user's answer is correct, they are awarded
        points (added to `self.score`)and the game moves on to the next city.
        If the user's answer is incorrect, they are not awarded any
        points and the game also moves on to the next city.
        If the user types 'next', the game skips to the next
        question within the same city.

        Note: This method uses the `delprint` function to print
        messages to the user.  It also uses the `time.sleep`
        function to pause execution of the game for a
        short period of time after certain actions.
    """
        for inner_city in self.inner_cities:
            # Get all questions for this city
            inner_city_questions = [
                q for q in self.inner_question_bank if q.category == inner_city
            ]

            # Iterate over each question in order
            for inner_question in inner_city_questions:
                # Ask the question and get the user's answer
                self.clear()
                self.delprint(" Where are we heading?")
                print(inner_question.text)
                user_answer = input(" Your answer or type next: ")

                # Check if the user's answer is correct
                if user_answer.lower() == inner_question.answer.lower():
                    self.delprint(" Your answer is.....")
                    time.sleep(2)
                    print("Correct!")
                    self.delprint(" You get " + str
                                  (inner_question.points) + " points!")
                    self.score += inner_question.points
                    self.delprint(" Your current score is: " + str(self.score))
                    self.delprint(" Prepare for the next destination!")
                    break
                elif user_answer.lower() == "next":
                    continue  # Go to the next question within the same city
                else:
                    self.delprint(" Your answer is.....")
                    time.sleep(2)
                    print(" Incorrect!")
                    self.delprint(" The correct answer was: " + str
                                  (inner_question.answer))
                    self.delprint(" You get 0 points!")
                    self.delprint(" Your current score is: " + str(self.score))
                    self.delprint(" Prepare for the next destination!")
                    break  # Move to the next city if the answer is incorrect

                # Increase the counter each time a city has been visited
            self.cities_visited += 1

            # Check if all cities have been visited
            if self.cities_visited == len(self.inner_cities):
                self.clear()
                print("You have visited all cities!")
                print("Your final score is: " + str(self.score))
                if self.score == 50:
                    self.delprint("Congratulations! You got a perfect score!"
                                  "  You  should be on the show!")
                elif self.score >= 30:
                    self.delprint("Congratulations! You got a good score!")
                elif self.score >= 20:
                    self.delprint("You got an ok score. Try again!")
                elif self.score <= 10:
                    self.delprint("Did you pay attention in your geography"
                                  " classes? Try again!")
                print("Do you want to play again?")
                user_input = input("Enter yes or no: ")
                if user_input == "yes":
                    self.restart()
                elif user_input == "no":
                    break  # End the game
                else:
                    raise ValueError("Please enter yes or no")

    def restart(self):
        """Method to restart the game."""
        self.score = 0
        self.cities_visited = 0
        self.run()


game = RunGame(questions)
game.intro()
game.run()
