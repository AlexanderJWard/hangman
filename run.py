# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials


class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.tries = 5
        self.guess_correct = False
        self.guess_input = input("Enter a letter or word: ").upper()

    def guess_validation(self):
            try:
                if not self.guess_input.isalpha():
                    raise TypeError(
                    f"Your guess {self.guess_input} does not contain alphabet letters.")
            except TypeError as e:
                print(f"{e} Please enter a new guess")

    def player_guess(self):
        self.guess_input
        Game.guess_validation(self)


def main():
    print("Welcome")
    player_name = input("Please enter your name: ")
    Game(player_name).player_guess()


main()
