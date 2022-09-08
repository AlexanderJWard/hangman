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
        self.guessed_letters = []
        self.guessed_words = []
        self.wins = 0
        self.loses = 0

    def play_game(self):
        self.tries = 6
        self.guessed_letters = []
        self.guessed_words = []
        self.hangman_state()
        print(f"\nYou have {self.tries} attempts remaining\n")
        print(self.current_state[self.tries])
        self.random_word()
        self.data_validation()

    def random_word(self):
        self.word = random.choice(hangman_words).upper()
        self.word_length = "_" * len(self.word)
        print(f"{self.word_length}\n")

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
        validation = False
        while not validation:
            try:
                self.guess_input = input(
                    "Enter a letter or word: ").upper().strip()
                if not self.guess_input.isalpha():
                    raise TypeError(
                        f"Your guess {self.guess_input} does not contain alphabet letters.")
                else:
                    validation = True
                    if len(self.guess_input) == 1:
                        self.letter_guess()
                    else:
                        self.word_guess()
            except TypeError as e:
                print(f"\n{e} Please enter a new guess\n")

    def play_again(self):
        validation = False
        while not validation:
            try:
                play_again = input("Play again? (Y / N): ").upper().strip()
                if play_again == "Y":
                    validation = True
                    self.play_game()
                elif play_again == "N":
                    validation = True
                    print(
                        f"\nGood bye {self.player_name}. Please come back and try again!\n")
                    exit()
                else:
                    raise TypeError(
                        f"\nYou entered {play_again}. Please enter either Y or N\n")
            except TypeError as e:
                print(f"{e}")

    def guess_correct(self):
        if "_" not in self.word_length:
            self.win_game()
        else:
            print(f"\nYour guess {self.guess_input} is CORRECT.\n")
            print(self.current_state[self.tries])
            print(f"{self.word_length}\n")
            self.data_validation()

    def guess_wrong(self):
        self.tries -= 1
        if self.tries > 0:
            print(f"\nYour guess {self.guess_input} is WRONG.\n")
            print(f"Your guessed letters: {self.guessed_letters}")
            print(f"Your guessed words: {self.guessed_words}\n")
            print(f"You have {self.tries} attempts remaining")
            print(self.current_state[self.tries])
            print(f"{self.word_length}\n")
            self.data_validation()
        else:
            self.lose_game()

    def already_guessed(self):
        print(f"\nYou already guessed {self.guess_input}\n")
        print(f"Your guessed letters: {self.guessed_letters}")
        print(f"Your guessed words: {self.guessed_words}\n")
        print(f"\nYou have {self.tries} attempts remaining")
        print(self.current_state[self.tries])
        print(f"{self.word_length}\n")
        self.data_validation()

    def letter_guess(self):
        if self.guess_input in self.guessed_letters:
            self.already_guessed()
        elif self.guess_input not in self.word:
            self.guessed_letters.append(self.guess_input)
            self.guess_wrong()
        else:
            self.guessed_letters.append(self.guess_input)
            self.list_word = list(self.word_length)
            self.index = [i for i, letter in enumerate(self.word) if letter == self.guess_input]
            for i in self.index:
                self.list_word[i] = self.guess_input
            self.word_length = "".join(self.list_word)
            self.guess_correct()

    def word_guess(self):
        if self.guess_input in self.guessed_words:
            self.already_guessed()
        elif self.guess_input != self.word:
            self.guessed_words.append(self.guess_input)
            self.guess_wrong()
        else:
            self.win_game()

    def win_game(self):
        print("""

               \\0/
                |
               / \\
            """)
        print(f"\nYOU WON! The correct word was {self.word}\n")
        self.wins += 1
        print(f"\nGames Won: {self.wins}")
        print(f"Games Lost: {self.loses}\n")
        self.play_again()

    def lose_game(self):
        print(f"\nYOU LOST! The correct word was {self.word}\n")
        self.loses += 1
        print(f"\nGames Won: {self.wins}")
        print(f"Games Lost: {self.loses}\n")
        self.play_again()

def main():
    print("Welcome to Hangman!\n")
    player_name = input("Please enter your name: ").upper().strip
    print(f"\nWelcome {player_name}!")
    Hangman(player_name).play_game()


main()
