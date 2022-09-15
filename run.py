import gspread
from google.oauth2.service_account import Credentials
import random
from words import hangman_words
from natsort import natsorted
from colorama import Fore, Back, Style

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
    """
    Hangman is a text based game where the player has to guess the correct
    word by inputting letters to reveal correctly guessed ones. Once the
    player reveals all the correct letters in the word or the player guesses
    the word itself the game has been won. The player only has a set amount
    of lives to win the game before they lose, their already guessed letters
    and words are displayed to help the user. The player name, wins and loses
    are recorded on a Google Sheet and the top 5 players can be viewed before
    playing the game.
    """

    def __init__(self, player_name):
        """
        Parameters
        ----------
        player_name : str
            The name inputted by the player used to play and score in the game.

        Attributes
        ----------
        lives : int
            The amount of attempts before the player reaches the fail state
            of the game.
        guessed_letters : list, str
            An empty list that will store the players already guessed letters.
        guessed_words : list, str
            An empty list that will store the players already guessed words.
        wins : int
            Keeps track of how many wins the player has
        loses : int
            Keeps track of how many loses the player has
        """
        self.player_name = player_name
        self.lives = 6
        self.guessed_letters = []
        self.guessed_words = []
        self.wins = 0
        self.loses = 0

    def update_player(self):
        """
        update_player checks if the player's name is already in the
        leaderboard. If the name exists the wins and loses are retrieved
        from the Google Sheet so the player can continue their account.
        The exisiting player is welcomed back and their wins and loses
        are displayed.

        However if the player's name does not exist the player is welcomed
        and their name, wins and loses are added to the Google Sheet,
        note that the players wins and loses will both be 0.

        Finally, menu_options will be called and the player makes their choice.
        """
        leaderboard = [self.player_name, self.wins, self.loses]
        if self.player_name in WORKSHEET.col_values(1):
            hiscore_index = WORKSHEET.col_values(1).index(self.player_name)
            self.wins = int(WORKSHEET.col_values(2)[hiscore_index])
            self.loses = int(WORKSHEET.col_values(3)[hiscore_index])
            print(f"\nWelcome back {self.player_name}!")
            print(Fore.GREEN + f"\nGames Won: {self.wins}")
            print(Fore.RED + f"Games Lost: {self.loses}\n" + Fore.RESET)
        else:
            WORKSHEET.append_row(leaderboard)
            print(f"\nWelcome {self.player_name}. Good Luck!")
        self.menu_options()

    def menu_options(self):
        """
        menu_options give the player a choice between the following:
        1. Play Hangman which calls start_game.
        2. View Leaderboard which calls view_leaderboard to view to top 5
        players sorted by wins.
        3. Exit Game which will display a goodbye message and stop the
        Python code.

        Raises
        ------
        TypeError
            If the input is not equal to 1, 2 or 3.
        """
        validation = False
        while not validation:
            try:
                print("\n1: Play Hangman")
                print("2: View Leaderboard")
                print("3: Exit Game\n")
                menu_input = input("Please enter your selection: ").strip()
                if menu_input == "1":
                    validation = True
                    self.start_game()
                elif menu_input == "2":
                    validation = True
                    self.view_leaderboard()
                elif menu_input == "3":
                    validation = True
                    print(
                        f"\nGood bye {self.player_name}. Please come back and try again!\n")  # noqa
                    exit()
                else:
                    raise TypeError(
                        f"\nYou entered {menu_input}. Please enter 1, 2 or 3\n")  # noqa
            except TypeError as e:
                print(f"{e}")

    def start_game(self):
        """
        start_game sets the lives to 6 and empties the guessed_letter and
        guessed_words lists.

        hangman_state is then called and the players current amount of lives
        is printed followed by an image of the current hangman state determined
        by the index of current_state.

        random_word is called to choose a word from the words.py file and hide
        the letters with underscores.

        player_guess is called to ask the player to input their guess of
        either a letter or word.
        """
        self.lives = 6
        self.guessed_letters = []
        self.guessed_words = []
        self.hangman_state()
        self.print_lives()
        print(self.current_state[self.lives])
        self.random_word()
        self.player_guess()

    def hangman_state(self):
        """
        hangman_state contains all the hangman image states which are
        displayed when the player guesses the wrong letter or word.
        The player's current lives relate to the index of the current_state,
        lives start at 6 meaning the 7th image is displayed first. When the
        player has 0 lives left the 1st image in the list is displayed.
        """
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

    def random_word(self):
        """
        random_word uses the imported random library to choose a word from the
        hangman_words list inside the words.py file, this word is then
        capitalized.

        The length of this word is then determined and the same amount of
        underscores as the length is saved in a variable called word.length.
        This is then printed to the player.
        """
        self.word = random.choice(hangman_words).upper()
        self.word_length = "_" * len(self.word)
        print(f"{self.word_length}\n")

    def player_guess(self):
        """
        player_guess asks the player to input a letter or word guess, this is
        then converted into uppercase and stripped of leading and trailing
        whitespace.

        If the length of the guess is equal to exactly 1 then letter_guess is
        called, if the guess is longer than 1 then word_guess is called.

        Raises
        ------
        TypeError
            If the input contains any NON alphabet characters.
        """
        validation = False
        while not validation:
            try:
                self.guess_input = input(
                    "Enter a letter or word: ").upper().strip()
                if not self.guess_input.isalpha():
                    raise TypeError(
                        f"Your guess {self.guess_input} contains NON alphabet characters.")  # noqa
                else:
                    validation = True
                    if len(self.guess_input) == 1:
                        self.letter_guess()
                    else:
                        self.word_guess()
            except TypeError as e:
                print(f"\n{e} Please enter a new guess\n")

    def update_leaderboard(self):
        """
        update_leaderboard prints to the player how many wins and loses they
        have before updating the related scores for that player in the Google
        Sheet leaderboard. This allows the player to close the game and when
        they return at a later date their wins and loses can be retrieved
        from the leaderboard.
        """
        hiscore_index = WORKSHEET.col_values(1).index(self.player_name)
        print(Fore.GREEN + f"\nGames Won: {self.wins}")
        print(Fore.RED + f"Games Lost: {self.loses}\n" + Fore.RESET)
        WORKSHEET.update_cell(hiscore_index + 1, 2, self.wins)
        WORKSHEET.update_cell(hiscore_index + 1, 3, self.loses)

    def view_leaderboard(self):
        """
        view_leaderboard gets all data values from the Google Sheet and sorts
        them in order of wins using an imported library called natsort. The
        order is reversed so high numbers appear at the top and the column
        names are removed from the selection. This data is then sorted into a
        list of the top 5 and printed in a for loop. menu_options is then
        called to return back to the menu.
        """
        hiscore_data = WORKSHEET.get_all_values()
        sort = natsorted(hiscore_data[1:], key=lambda x: x[1], reverse=True)
        top_five = sort[0:5]
        print("+---------------+-------+--------+")
        print("|  " + Fore.YELLOW + "RANK & NAME" + Fore.RESET + "  |  " + Fore.YELLOW + "WON" + Fore.RESET + "  |  " + Fore.YELLOW + "LOST" + Fore.RESET + "  |")  # noqa
        print("+---------------+-------+--------+")
        for player in top_five:
            print(
                "| " + Fore.YELLOW + f"{top_five.index(player) + 1}:" + Fore.RESET + f" {player[0]:10s} | " + Fore.GREEN + f" {player[1]:4s}" + Fore.RESET + " | " + Fore.RED + f" {player[2]:5s}" + Fore.RESET + " |" )  # noqa
            print("+---------------+-------+--------+")
        self.menu_options()

    def play_again(self):
        """
        play_again asks the player to enter either Y to play again or N to exit
        the code. If Y is entered menu_options is called and the game can be
        started again. If N is entered the game ends and a message is displayed
        to the player.

        Raises
        ------
        TypeError
            If the input does not contain a Y or N.
        """
        validation = False
        while not validation:
            try:
                play_again = input("Play again? ( Y / N ): ").upper().strip()
                if play_again == "Y":
                    validation = True
                    self.menu_options()
                elif play_again == "N":
                    validation = True
                    print(
                        f"\nGood bye {self.player_name}. Please come back and try again!\n")  # noqa
                    exit()
                else:
                    raise TypeError(
                        f"\nYou entered {play_again}. Please enter either Y or N\n")  # noqa
            except TypeError as e:
                print(f"{e}")

    def print_lives(self):
        """
        print_lives checks if lives are above 1 and if true then lives
        remaining is printed. If false then life remaining is printed instead.
        """
        if self.lives > 1:
            print(Fore.RED + f"{self.lives}" + Fore.RESET + " lives remaining")
        else:
            print(Fore.RED + f"{self.lives}" + Fore.RESET + " life remaining")

    def print_already_guessed(self):
        """
        print_already_guessed loops through guessed_letters and guessed_words
        and prints them neatly for the player to view.
        """
        if self.guessed_letters:
            print("Your guessed letters:\n")
            print("|", end=" ")
            for letter in self.guessed_letters:
                print(Fore.YELLOW + letter + Fore.RESET + " |", end=" ")
            print("\n") 
        if self.guessed_words:
            print("Your guessed words:\n")
            for word in self.guessed_words:
                print("| " + Fore.YELLOW + word + Fore.RESET + " |\n")
        
    def guess_correct(self):
        """
        guess_correct checks if there are any underscores remaining in
        word_length and if not win_game is called. If there are underscores
        then a message is printed letting the player know the guess was
        correct. The updated word is displayed and player_guess is called
        so the player can make another guess.
        """
        if "_" not in self.word_length:
            self.win_game()
        else:
            print(f"\nYour guess " + Fore.YELLOW + f"{self.guess_input}" + Fore.RESET + " is " + Fore.GREEN + "CORRECT" + Fore.RESET + ".\n")  # noqa
            print(self.current_state[self.lives])
            print(f"{self.word_length}\n")
            self.player_guess()

    def guess_wrong(self):
        """
        guess_wrong decreases the lives by 1. If the lives are above 0 a
        message is shown informing the player their guess was wrong, it
        also prints their guessed letters and words followed by how many
        attempts they have left. The current state is printed and then the
        player_guess is called for the player to guess again.

        If the lives are not greater than 0 then lose_game is called.
        """
        self.lives -= 1
        if self.lives > 0:
            print(f"\nYour guess " + Fore.YELLOW + f"{self.guess_input}" + Fore.RESET + " is " + Fore.RED + "WRONG" + Fore.RESET + ".\n")  # noqa
            self.print_already_guessed()
            self.print_lives()
            print(self.current_state[self.lives])
            print(f"{self.word_length}\n")
            self.player_guess()
        else:
            self.lose_game()
        
    def already_guessed(self):
        """
        already_guessed prints the guess alongside other already guessed
        letters and words. player_guess is then called for the player to
        guess again.
        """
        print(f"\nYou already guessed " + Fore.YELLOW + f"{self.guess_input}\n" + Fore.RESET)  # noqa
        self.print_already_guessed()
        self.print_lives()
        print(self.current_state[self.lives])
        print(f"{self.word_length}\n")
        self.player_guess()

    def letter_guess(self):
        """
        letter_guess checks if the guess is already in the guessed_letters
        list and if true then already_guessed is called. It then checks if
        the guess is in the final word and if not then it appends the guess
        to the guessed_letters list before calling guess_wrong.

        If the letter is in the final word it first appends to guessed_letters
        and then enumerates through the word and replaces the relevant index of
        the word_length underscores with the guessed letter. Finally,
        guess_correct is called.
        """
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
        """
        word_guess checks if the word is already in guessed_words list and
        if true then already_guessed is called. If the guess is not the word
        then it's appended to guessed_words and guess_wrong is called.
        If the word is correct then win_game is called.
        """
        if self.guess_input in self.guessed_words:
            self.already_guessed()
        elif self.guess_input != self.word:
            self.guessed_words.append(self.guess_input)
            self.guess_wrong()
        else:
            self.win_game()

    def win_game(self):
        """
        win_game prints text to the player informing them of the win as well
        as showing them the correct word. Wins is incremented by 1 and
        update_leaderboard is called before play_again is called.
        """
        print(Fore.GREEN + """
 __     ______  _    _  __          ______  _   _   _
 \ \   / / __ \| |  | | \ \        / / __ \| \ | | | |
  \ \_/ / |  | | |  | |  \ \  /\  / / |  | |  \| | | |
   \   /| |  | | |  | |   \ \/  \/ /| |  | | . ` | | |
    | | | |__| | |__| |    \  /\  / | |__| | |\  | |_|
    |_|  \____/ \____/      \/  \/   \____/|_| \_| (_)


            """ + Fore.RESET)
        print("\nThe correct word was " + Fore.GREEN + f"{self.word}" + Fore.RESET)  # noqa
        self.wins += 1
        self.update_leaderboard()
        self.play_again()

    def lose_game(self):
        """
        lose_game prints text to the player informing them of the loss as well
        as showing them the correct word. The final current state is printed
        and Loses is incremented by 1. update_leaderboard is called before
        play_again is called.
        """
        print(Fore.RED + """
 __     ______  _    _   _      ____   _____ _______   _
 \ \   / / __ \| |  | | | |    / __ \ / ____|__   __| | |
  \ \_/ / |  | | |  | | | |   | |  | | (___    | |    | |
   \   /| |  | | |  | | | |   | |  | |\___ \   | |    | |
    | | | |__| | |__| | | |___| |__| |____) |  | |    |_|
    |_|  \____/ \____/  |______\____/|_____/   |_|    (_)


        """ + Fore.RESET)
        print(self.current_state[self.lives])
        print("\nThe correct word was " + Fore.GREEN + f"{self.word}" + Fore.RESET)  # noqa
        self.loses += 1
        self.update_leaderboard()
        self.play_again()


def main():
    """
    main function prints the name of the game. It then asks the player to
    input their name. The Hangman class is called and passed the player name
    before calling the update_player function.

    Raises
    ------
    TypeError
        If the input contains NON alphabet characters
    ValueError
        If the input is greater than 10 in length
    """
    print("""
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/\n
    """)
    validation = False
    while not validation:
        try:
            player_name = input("Please enter your player name: ").upper().strip()  # noqa
            if len(player_name) > 10:
                raise ValueError(
                    f"\nYour player name {player_name} is too long.\nPlease enter a name less than 10 characters.\n")  # noqa
            elif not player_name.isalpha():
                raise TypeError(
                    f"\nYour player name {player_name} contains NON alphabet characters.\nPlease enter a name using only alphabet characters.\n")  # noqa
            else:
                validation = True
        except (ValueError, TypeError) as e:
            print(f"{e}")
    Hangman(player_name).update_player()


main()
