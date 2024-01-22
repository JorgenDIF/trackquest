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
            try:
                player_name = input(" Please enter your preferred username "
                                    "max 10 letters: ")
                if not player_name:
                    raise ValueError(" Username can't be empty")
                if len(player_name) > 10:
                    raise ValueError(" Username can't be longer"
                                     "than 10 letters")
                self.player_name = player_name
                break
            except ValueError as e:
                print(e)
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
        self.player_name = None

        self.question_bank = []
        for question in self.question_list:
            question_category = question["category"]
            question_points = question["points"]
            question_text = question["text"]
            question_answer = question["answer"]
            new_question = Question(
                question_category, question_points, question_text,
                question_answer
            )
            self.question_bank.append(new_question)

            # Randomize the order of the cities

        cities = list(set(q.category for q in self.question_bank))
        random.shuffle(cities)

        # Limit the number of cities to 5 per game
        cities = cities[:5]

        # Existing code
        for city in cities:
            city_questions = [
                q for q in self.question_bank if q.category == city]
            city_questions.sort(key=lambda q: q.points, reverse=True)
            self.question_bank = [
                q for q in self.question_bank
                if q.category != city
                ] + city_questions
        self.inner_question_bank = self.question_bank
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
            for inner_question in inner_city_questions:
                # Show the current score
                self.delprint("Your current score is: " + str(self.score))
                time.sleep(2)
                # Ask the question and get the user's answer
                self.clear()
                self.delprint("Where are we heading?")
                print(inner_question.text)
                while True:
                    try:
                        user_answer = input(" Your answer or type next: ")
                        if not user_answer:
                            raise ValueError(" Please " + self.player_name +
                                             ", enter an answer or type next")
                        break  # If the input is valid, break out of the loop
                    except ValueError as e:
                        print(e)
                # Check if the user's answer is correct
                if user_answer.lower() == inner_question.answer.lower():
                    self.delprint(" Your answer is.....")
                    time.sleep(2)
                    print(" Correct!")
                    self.delprint("You get " + str
                                  (inner_question.points) + " points!")
                    self.score += inner_question.points
                    self.delprint(" Your current score is: " + str(self.score))
                    self.delprint(" Prepare for the next destination!")

                    break
                else:
                    self.delprint(" Your answer is.....")
                    time.sleep(2)
                    print(" Incorrect!")
                    self.delprint(" The correct answer was: " + str
                                  (inner_question.answer))
                    self.delprint(" You get 0 points!")
                    self.delprint(" Prepare for the next destination!")
                    break  # Move to the next city if the answer is incorrect

            # Increase the counter each time a city is visited
            self.cities_visited += 1

            # Check if all cities have been visited
            if self.cities_visited == len(self.inner_cities):
                self.clear()
                print(" You have visited all cities!")
                print(" Your final score is: " + str(self.score))
                if self.score == 50:
                    self.delprint(" Congratulations!" + str(self.player_name) +
                                  " You got a perfect score!"
                                  "  You  should be on the show!")
                elif self.score >= 30:
                    self.delprint(" Congratulations!" + str(self.player_name) +
                                  " You got a good score!")
                elif self.score >= 20:
                    self.delprint(" You got an ok score."
                                  + str(self.player_name) +
                                  " Try again!")
                elif self.score >= 10:
                    self.delprint(" Did you pay attention in your geography"
                                  " classes?" + str(self.player_name) +
                                  " Try again!")
                print(" Please enter yes or no")
                user_input = input(" Do you want to play again?"
                                   " yes/no: ").lower()
                while user_input not in ["yes", "no"]:
                    print(" Invalid input. Please enter yes or no")
                    user_input = input(" Do you want to play again?"
                                       "yes/no: ").lower()

                if user_input == "yes":
                    self.restart()
                elif user_input == "no":
                    self.clear()
            self.delprint(" Thank you for playing! Hope to see you again"
                          " soon! If you want to try a Swedish version of"
                          " the game, please visit: "
                          " Pasparetbloggen to try it out!"
                          " and you can play the real game!")
            return  # End the game

    def restart(self):
        """Method to restart the game."""
        self.score = 0
        self.cities_visited = 0
        self.run()


game = RunGame(questions)
game.intro()
game.run()
