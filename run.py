# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import random
from words import hangman_words
from natsort import natsorted, ns

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman hiscores')
WORKSHEET = SHEET.worksheet('hiscores')

class Hangman:
    def __init__(self, player_name):
        self.player_name = player_name
        self.tries = 6
        self.guessed_letters = []
        self.guessed_words = []
        self.wins = 0
        self.loses = 0

    def update_hiscores(self):
        hiscore_index = WORKSHEET.col_values(1).index(self.player_name)
        print(f"\nGames Won: {self.wins}")
        print(f"Games Lost: {self.loses}\n")
        WORKSHEET.update_cell(hiscore_index + 1, 2, self.wins)
        WORKSHEET.update_cell(hiscore_index + 1, 3, self.loses)

    def start_game(self):
        self.tries = 6
        self.guessed_letters = []
        self.guessed_words = []
        self.hangman_state()
        print(f"\nYou have {self.tries} attempts remaining\n")
        print(self.current_state[self.tries])
        self.random_word()
        self.data_validation()

    def view_hiscores(self):
        hiscore_data = WORKSHEET.get_all_values()
        sort = natsorted(hiscore_data[1:], key=lambda x: x[1], reverse=True)
        top_five = sort[0:5]
        print("\nTOP 5 Players\n")
        for player in top_five:
            print(
                f"{player[0]:10s}| {player[1]:3s} WON | {player[2]:3s} LOST |")
        self.menu_options()

    def menu(self):
        hiscores = [self.player_name, self.wins, self.loses]
        if self.player_name in WORKSHEET.col_values(1):
            hiscore_index = WORKSHEET.col_values(1).index(self.player_name)
            self.wins = int(WORKSHEET.col_values(2)[hiscore_index])
            self.loses = int(WORKSHEET.col_values(3)[hiscore_index])
            print(f"\nWelcome back {self.player_name}!")
            print(f"\nGames Won: {self.wins}")
            print(f"Games Lost: {self.loses}\n")
        else:
            WORKSHEET.append_row(hiscores)
            print(f"\nWelcome {self.player_name}. Good Luck!")
        self.menu_options()

    def menu_options(self):
        validation = False
        while not validation:
            try:
                print(f"\n1: Play Hangman")
                print(f"2: View Hiscores")
                print(f"3: Exit Game\n")
                menu_input = input("Please enter your selection: ").strip()
                if menu_input == "1":
                    validation = True
                    self.start_game()
                elif menu_input == "2":
                    validation = True
                    self.view_hiscores()
                elif menu_input == "3":
                    validation = True
                    print(
                        f"\nGood bye {self.player_name}. Please come back and try again!\n")
                    exit()
                else:
                    raise TypeError(
                        f"\nYou entered {menu_input}. Please enter either 1 or 2\n")
            except TypeError as e:
                print(f"{e}")

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
                        f"Your guess {self.guess_input} contains NON alphabet characters.")
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
                    self.menu_options()
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
            self.index = [i for i, letter in enumerate(
                self.word) if letter == self.guess_input]
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
        self.update_hiscores()
        self.play_again()

    def lose_game(self):
        print(f"\nYOU LOST! The correct word was {self.word}\n")
        print(self.current_state[self.tries])
        self.loses += 1
        self.update_hiscores()
        self.play_again()


def main():
    print("Welcome to Hangman!\n")
    validation = False
    while not validation:
        try:
            player_name = input("Please enter your name: ").upper().strip()
            if len(player_name) > 10:
                raise TypeError(
                    f"\nYour player name {player_name} is too long.\nPlease enter a name less than 10 characters.\n")
            elif not player_name.isalpha():
                raise TypeError(
                    f"\nYour player name {player_name} contains NON alphabet characters.\nPlease enter a name using only alphabet characters.\n")
            else:
                validation = True
        except TypeError as e:
            print(f"{e}")
    Hangman(player_name).menu()


main()
