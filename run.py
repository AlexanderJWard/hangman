# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import random
from words import hangman_words


class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.tries = 5
        self.guess_correct = False
        self.guessed_letters = []
        self.guessed_words = []

    def random_word(self):
        self.word = random.choice(hangman_words).upper()
        self.word_length = "_ " * len(self.word)

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
                    if len(self.guess_input) == 1:
                        self.guess_type = "letter"
                    else:
                        self.guess_type = "word"
            except TypeError as e:
                print(f"{e} Please enter a new guess")

    def play_game(self):
        Game.random_word(self)
        print(self.word)
        print(self.word_length)
        Game.guess_validation(self)
        print("Data Type Correct...")
        print(self.guess_input)
        print(self.guess_type)
    
    def guess_validation(self):
        while not self.guess_correct and self.tries > 0:
            Game.data_validation(self)
            print(self.tries)
            if self.guess_type == "letter":
                if self.guess_input in self.guessed_letters:
                    print(f"You already guessed the letter {self.guess_input}")
                elif self.guess_input not in self.word:
                    print(f"{self.guess_input} is NOT in the word")
                    self.guessed_letters.append(self.guess_input)
                    self.tries -= 1
                else:
                    print(f"Well done {self.guess_input} is in the word")
                    self.guessed_letters.append(self.guess_input)
        if self.guess_correct:
            print("WIN")
        else:
            print("LOSE")

def main():
    print("Hangman\n")
    player_name = input("Please enter your name: ")
    print(f"\nWelcome {player_name}!")
    Game(player_name).play_game()


main()
