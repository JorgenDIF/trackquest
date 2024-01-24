
"""
This is the main file for the game Track Quest.
The game is based on the swedish TV-show "På spåret".
The goal is to guess the city from the clues given.
The game is built with inspiration from the youtube tutorial

"""


# Importing modules
import os  # for clearing the screen
import sys  # for printing text with a delay
import time  # for printing text with a delay
import random  # for randomizing the order of the cities
import colorama  # for printing text in color
from colorama import Fore, Back, Style  # for printing text in color
from question_data import questions

colorama.init(autoreset=True)


class Question:
    """
    Args:
    category (str): The category or
    destination associated with the question.
    points (int): The point value assigned to the question.
    text (str): The text of the trivia question.
    answer (str): The correct answer to the trivia question.
    """
    def __init__(self, category, points, text, answer):
        self.category = category
        self.points = points
        self.text = text
        self.answer = answer


class RunGame:
    """
    A class to represent the game.

    Represent the trivia game inspired by 'På spåret.'
    This class orchestrates the trivia game, taking
    a list of questions as input
    and creating Question objects from the input list.
    It randomizes the order of
    the cities, sorts questions by points
    using a lambda function, and facilitates
    the gameplay.

    The main inspiration for the game comes from
    the 'På spåret' TV show, and some
    ideas were adapted from the following sources:
    - https://github.com/sampathbasa/quiz-app/tree/main
    - https://sparkbyexamples.com/python/sort-using-lambda-in-python/amp/

    Several modifications have been made to tailor the code
    for this specific game.
    Recommendations from my mentor have also been
    incorporated to enhance the code.
    """

    def clear(self):
        """Clears the screen based on the user's operating system."""
        # for Windows
        if os.name == "nt":
            os.system("cls")
        # for Mac and Linux (here, os.name is 'posix')
        else:
            os.system("clear")

    def delprint(self, text, delay_time=0.02):
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
        """
       Prints text with a delayed effect, introducing a time delay between
       each character for a gradual display.

        Parameters:
        - text (str): The text to be displayed with a delayed effect.
        - delay_time (float, optional): The duration of the delay between
        characters (default is 0.02 seconds).

        Credit: The implementation is inspired by
        https://replit.com/talk/learn/The-Slow-Print/44741.
        """
        self.clear()

        self.delprint("""
s   o o o o o o o . . .   ______________________________ _____=======_||____
   o      _____           ||                            | |                 |
 .][__n_n_|DD[  ====_____  |                            | |                 |
>(________|__|_[_________]_|____________________________|_|_________________|
_/oo OOOOO oo`  ooo   ooo  'o!o!o                  o!o!o` 'o!o         o!o`
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
        """)

        self.delprint("""
 _____                _        ____                 _
/__   \_ __ __ _  ___| | __   /___ \_   _  ___  ___| |_
  / /\/ '__/ _` |/ __| |/ /  //  / / | | |/ _ \/ __| __|
 / /  | | | (_| | (__|   <  / \_/ /| |_| |  __/\__ \ |_
 \/   |_|  \__,_|\___|_|\_\ \___,_\ \__,_|\___||___/\__|


        """)

        self.delprint(" Welcome to Track Quest!\n"
                      " Inspired by the Swedish TV-show 'På spåret,'\n"
                      " guess the city in 5 rounds\n"
                      " with points decreasing from 10 to 2.\n"
                      " One guess per destination;"
                      "a wrong answer gets zero points.\n"
                      " Type 'next' to move down a point level if unsure,\n"
                      " and save your guess to the next point level.\n"
                      " Just a reminder, if you press next on the last \n"
                      " point level, you will get zero points!!\n"
                      " Choose a username to begin.")

        while True:
            player_name = input(f"{Fore.LIGHTBLUE_EX}{Style.NORMAL} "
                                "Please enter your preferred username"
                                " max 10 letters: ")
            if player_name:
                if len(player_name) <= 10:
                    break
            print(f" {Back.RED}Please choose a username of max 10 letters.")
        # Print a blank line for formatting
        self.delprint(f" Welcome  {player_name} !!")

        while True:
            self.delprint(" Choose if you want to sit in First Class or\n"
                          " in the Handcar. It makes no difference \n"
                          " to the game, but it's more fun to choose.")
            compartment = input(f"{Fore.LIGHTBLUE_EX}{Style.NORMAL} "
                                "Type for '1' for First Class or '2' for "
                                " Handcar to make your choice: ")
            if compartment == "1":
                self.delprint(" You have chosen First class")
                break
            if compartment == "2":
                self.delprint(" You have chosen the Handcar")
                time.sleep(3)
                break
            print(f"{Back.RED} Please type  '1' First class"
                  "or '2' for Handcar.")

    def __init__(self, question_list):
        """
        Intializes a new instance of the RunGame class.

        This method takes a list of questions as input
        and creates Question objects from the input list.
        Each question is a dictionary with the following keys
        'category', 'points', 'text', and 'answer'.
        The also creates a list of unique cities from the
        question categories and randomizes the order of the cities.

        """
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
                user_answer = input(f"{Fore.LIGHTBLUE_EX}{Style.NORMAL}"
                                    " Your answer or type next: ")

                # Check if the user's answer is correct
                if user_answer.lower() == inner_question.answer.lower():
                    self.delprint(" Your answer is.....")
                    time.sleep(2)
                    print(f"{Style.BRIGHT}{Back.GREEN} Correct!")
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
                    print(f"{Style.BRIGHT}{Back.RED} Incorrect!")
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
                print(f"{Back.GREEN}{Style.BRIGHT} You have visited"
                      " all cities!")
                print(" Your final score is: " + str(self.score))
                if self.score == 50:
                    self.delprint(" Congratulations! You got a perfect score!"
                                  "  You should be on the show!")
                    print(f"{Fore.LIGHTGREEN_EX} You are a Star!")
                elif self.score >= 30:
                    self.delprint(" Congratulations! You got a good score!")
                    print(f" {Fore.LIGHTBLUE_EX} Still room for improvement!")
                elif self.score >= 20:
                    self.delprint(" You got an ok score. Try again!")
                    print(f" {Fore.LIGHTYELLOW_EX} You can do better!")
                elif self.score <= 10:
                    self.delprint(" Did you pay attention in your geography"
                                  " classes? Try again!")
                    print(f" {Fore.LIGHTRED_EX} I know you can do better!")
                print(" Do you want to play again?")
                user_input = input(" Enter yes or no: ")
                if user_input == "yes":
                    self.restart()
                elif user_input == "no":
                    print(f"{Fore.BLUE} Thanks for playing! Welcome"
                          " back anytime!")
                    break  # End the game
                else:
                    print(f"{Back.RED} Please enter yes or no")
                    user_input = input(" Enter yes or no: ")

    def restart(self):
        """
        Resets the game to its initial state and starts a new game.

        This method resets the score and cities_visited attributes.
        It then calls the run method to start a new game.
        """
        self.score = 0
        self.cities_visited = 0
        self.run()


game = RunGame(questions)
game.intro()
game.run()
