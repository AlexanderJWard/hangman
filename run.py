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
        self.correct_word = False
        self.guessed_letters = []
        self.guessed_words = []
        self.wins = 0
        self.loses = 0

    def play_game(self):
        self.hangman_state()
        self.random_word()
        self.tries = 6
        self.correct_word = False
        self.guessed_letters = []
        self.guessed_words = []
        print(f"\nYou have {self.tries} attempts remaining\n")
        print(self.current_state[self.tries])
        self.guess_validation()

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
                        self.guess_type = "word"
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
        print(f"\nWell done! Your guess {self.guess_input} is correct\n")

    def guess_wrong(self):
        print("a")

    def already_guessed(self):
        print(f"\nYou already guessed {self.guess_input}\n")
        print(f"Your guessed letters: {self.guessed_letters}")
        print(f"Your guessed words: {self.guessed_words}")
        print(f"\nYou have {self.tries} attempts remaining\n")
        print(f"{self.word_length}\n")
        self.data_validation()

    def letter_guess(self):
        while not self.correct_word and self.tries > 0:
            if self.guess_input in self.guessed_letters:
                self.already_guessed()
            elif self.guess_input not in self.word:
                self.guessed_letters.append(self.guess_input)
                self.guess_wrong()
            else:
                self.guessed_letters.append(self.guess_input)
                self.guess_correct()
                self.list_word = list(self.word_length)
                self.index = [i for i, letter in enumerate(
                    self.word) if letter == self.guess_input]
                for i in self.index:
                    self.list_word[i] = self.guess_input
                self.word_length = "".join(self.list_word)
                if "_" not in self.word_length:
                    self.correct_word = True
        if self.correct_word:
            self.win_game()
        else:
            self.lose_game()

    def word_guess(self):
        print("a")

    def win_game(self):
        print("win")

    def lose_game(self):
        print("lose")

    def guess_validation(self):
        while not self.correct_word and self.tries > 0:
            self.data_validation()
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
                    print(f"{self.word_length}\n")
                    self.guessed_letters.append(self.guess_input)
                else:
                    self.guess_correct
                    self.guessed_letters.append(self.guess_input)
                    self.list_word = list(self.word_length)
                    self.index = [i for i, letter in enumerate(
                        self.word) if letter == self.guess_input]
                    for i in self.index:
                        self.list_word[i] = self.guess_input
                    self.word_length = "".join(self.list_word)
                    if "_" not in self.word_length:
                        self.correct_word = True
                    print(f"{self.word_length}\n")
            elif self.guess_type == "word":
                if self.guess_input in self.guessed_words:
                    print(f"\nYou already guessed the word {self.guess_input}")
                    print(f"You have {self.tries} attempts remaining\n")
                    print(self.current_state[self.tries])
                    print(f"{self.word_length}\n")
                elif self.guess_input != self.word:
                    self.tries -= 1
                    print(f"\n{self.guess_input} is NOT the word")
                    print(f"You have {self.tries} attempts remaining\n")
                    print(f"{self.word_length}\n")
                    self.guessed_words.append(self.guess_input)
                else:
                    print(
                        f"\nWell done {self.guess_input} is the correct word!")
                    self.correct_word = True
        if self.correct_word:
            print("You WON!")
            print("""

               \\0/
                |
               / \\
            """)
            print(
                f"Congratulations {self.player_name}, you guessed the correct word {self.word}\n")
            self.play_again
        else:
            print("You LOST!")
            print(
                f"The correct word was {self.word}.\nBetter luck next time!\n")
            self.play_again()


def main():
    print("Hangman\n")
    player_name = input("Please enter your name: ").upper()
    print(f"\nWelcome {player_name}!")
    Hangman(player_name).play_game()


main()
