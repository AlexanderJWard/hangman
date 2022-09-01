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

    def data_validation(self):
        self.validation = False
        while not self.validation:
            try:
                self.guess_input = input("Enter a letter or word: ").upper()
                if not self.guess_input.isalpha():
                    raise TypeError(
                        f"Your guess {self.guess_input} does not contain alphabet letters.")
                else:
                    self.validation = True
            except TypeError as e:
                print(f"{e} Please enter a new guess")

    def player_guess(self):
        Game.data_validation(self)
        print("Data Type Correct...")
        print(self.guess_input)


def main():
    print("Hangman\n")
    player_name = input("Please enter your name: ")
    print(f"\nWelcome {player_name}!")
    Game(player_name).player_guess()


main()
