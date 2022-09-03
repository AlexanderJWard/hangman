# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import random
from words import hangman_words


class Hangman:
    def __init__(self, player_name):
        self.player_name = player_name
        self.tries = 6
        self.guess_correct = False
        self.guessed_letters = []
        self.guessed_words = []

    def play_game(self):
        Hangman.hangman_state(self)
        Hangman.random_word(self)
        print(f"\nYou have {self.tries} attempts remaining\n")
        print(self.current_state[self.tries])
        Hangman.guess_validation(self)

    def random_word(self):
        self.word = random.choice(hangman_words).upper()
        self.word_length = "_" * len(self.word)
        print(self.word_length)

    def hangman_state(self):
        self.current_state = [
            """
            _______
            |/  |
            |   0
            |  /|\\
            |  / \\
            |
            """,
            """
            _______
            |/  |
            |   0
            |  /|\\
            |    \\
            |
            """,
            """
            _______
            |/  |
            |   0
            |  /|\\
            |
            |
            """,
            """
            _______
            |/  |
            |   0
            |   |\\
            |
            |
            """,
            """
            _______
            |/  |
            |   0
            |   |
            |
            |
            """,
            """
            _______
            |/  |
            |   0
            |  
            |  
            |
            """,
            """
            _______
            |/  |
            |   
            |  
            |  
            |
            """
        ]

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
                print(f"\n{e} Please enter a new guess\n")

    def guess_validation(self):
        while not self.guess_correct and self.tries > 0:
            Hangman.data_validation(self)
            if self.guess_type == "letter":
                if self.guess_input in self.guessed_letters:
                    print(f"\nYou already guessed the letter {self.guess_input}")
                    print(f"You have {self.tries} attempts remaining\n")
                    print(f"{self.word_length}\n")
                elif self.guess_input not in self.word:
                    self.tries -= 1
                    print(f"\n{self.guess_input} is NOT in the word")
                    print(f"You have {self.tries} attempts remaining\n")
                    print(self.current_state[self.tries])
                    self.guessed_letters.append(self.guess_input)
                    print(f"{self.word_length}\n")
                else:
                    print(f"\nWell done {self.guess_input} is in the word\n")
                    self.guessed_letters.append(self.guess_input)
                    self.list_word = list(self.word_length)
                    self.index = [i for i, letter in enumerate(self.word) if letter == self.guess_input]
                    for i in self.index:
                        self.list_word[i] = self.guess_input
                    self.word_length = "".join(self.list_word)
                    if "_" not in self.word_length:
                        self.guess_correct = True
                    print(f"{self.word_length}\n")
            elif self.guess_type == "word":
                if self.guess_input in self.guessed_words:
                    print(f"\nYou already guessed the word {self.guess_input}")
                    print(f"You have {self.tries} attempts remaining\n")
                    print(f"{self.word_length}\n")
                elif self.guess_input != self.word:
                    self.tries -= 1
                    print(f"\n{self.guess_input} is NOT the word")
                    print(f"You have {self.tries} attempts remaining\n")
                    self.guessed_words.append(self.guess_input)
                    print(f"{self.word_length}\n")
                else:
                    print(f"\nWell done {self.guess_input} is the correct word!")
                    self.guess_correct = True
        if self.guess_correct:
            print("WIN")
            print(f"Congratulations {self.player_name} you guessed the correct word {self.word}\n")
            self.play_again = input("Play again? (Y / N): ").upper()
            if self.play_again == "Y":
                Hangman(self.player_name).play_game()
            elif self.play_again == "N":
                print(f"\nGood bye {self.player_name}. Try again next time.")
                exit()
            else:
                raise TypeError(f"You entered {self.play_again}. Please enter either Y or N")
        else:
            print("LOSE")
            print(f"The correct word was {self.word}.\nBetter luck next time!\n")
            self.play_again = input("Play again? (Y / N): ").upper()
            if self.play_again == "Y":
                Hangman(self.player_name).play_game()
            elif self.play_again == "N":
                print(f"\nGood bye {self.player_name}. Try again next time.\n")
                exit()
            else:
                raise TypeError(f"You entered {self.play_again}. Please enter either Y or N")

def main():
    print("Hangman\n")
    player_name = input("Please enter your name: ").upper()
    print(f"\nWelcome {player_name}!")
    Hangman(player_name).play_game()


main()
