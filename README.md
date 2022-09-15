# Hangman

![image](https://user-images.githubusercontent.com/102811792/190385034-cdda6095-c2c0-4f1b-b0f1-e78621e2d52b.png)

## Author
Alexander Ward

## Project Overview
Hangman is a classic game that's instantly recognizable and the rules are easy enough for players of all ages to play and enjoy. The goal of the game is to uncover the hidden word by guessing letters or words to reveal new information. If a guessed letter is in the word then it's position in the word is revealed. However, if a letter is incorrect a part is added to the hangman image. Once the person is fully added to the image it's game over!

https://alexward-hangman.herokuapp.com/

## Table of Contents
Generate after readme is complete for UX and below

## How To Play/Use
![full-play](https://user-images.githubusercontent.com/102811792/190483375-787ef008-9610-42da-993e-2521cd5b25e9.gif)

- The player starts by entering a valid name using alphabet characters no longer than 10 long.

![enter-name](https://user-images.githubusercontent.com/102811792/190483768-d42859b8-78c4-47ee-bd53-889efbdce4ef.gif)

- After entering their name the player can now choose between starting the game, viewing the leaderboard or exiting the game. Here is what happens when the player looks at the leaderboard. The leaderboard shows the top 5 players who have the highest wins.

![view_leaderboard](https://user-images.githubusercontent.com/102811792/190484395-dd56a25d-9bd0-46cb-921d-2f412e7becca.gif)

- When starting the game a random word is chosen from the words.py file and displayed as underscores. The current hangman image is displayed, at the start of the game there are no body parts added to the image. The lives are also displayed, when these run out the game is over.

![start-game](https://user-images.githubusercontent.com/102811792/190484490-bcc99ab0-0942-42d7-aca9-238dd1a42580.gif)

- The player can now enter guesses, letters or words, to replace the underscores with correct letters or even guess the entire word.

![guess-correct](https://user-images.githubusercontent.com/102811792/190484972-0b420b99-3e9f-4fec-8513-ebb09ce98af9.gif)
![guess-word](https://user-images.githubusercontent.com/102811792/190485183-e38608fd-20ec-4d44-8a72-1985861ee610.gif)

- If the player guesses all the correct letters or enters the correct word the game is over and the player has won. The games won score will increase by 1.

![you-win](https://user-images.githubusercontent.com/102811792/190486034-dcd8f35e-5f79-4d82-8f31-42ceee9adab3.gif)

- However, if the player does not guess the correct letters or word in 6 attempts the game is over and the player has lose. The games lost score will increase by 1.

![you-lost](https://user-images.githubusercontent.com/102811792/190486770-98a3c842-63c5-4ac0-a49e-d5ededdb53a0.gif)

- A play again message is shown where the player can choose Y to loop back to the menu selection or choose N to exit the game.

![play-again-yes](https://user-images.githubusercontent.com/102811792/190486971-3a134ea9-2b46-48c4-8ba5-6f5d12c76c75.gif)
![play-again-no](https://user-images.githubusercontent.com/102811792/190486987-163300cf-3625-45e0-b91c-163430691679.gif)

- The player's score is saved so even if they exit the game and return at a later date they can continue climbing the leaderboard.

## Features

### Implemented Features

__Player Name__
- The player is prompted to enter a name of their choice, this connects the game with the player and gives them some creative control rather than just being player1 or player2 for example.

![image](https://user-images.githubusercontent.com/102811792/190489116-b6ec6faa-2a0f-44c1-8bf7-2c030c6fe52b.png)

- The name itself has some validation it must pass unless errors are raised. The first being that the inputted text must be alphabet characters and can't include numbers or special characters. Additionally, the name must be 10 characters or lower or an error is raised. When the errors for either of these outcomes happens a message is printed and the input for player name is prompted again.

![enter-name-non-alphabet](https://user-images.githubusercontent.com/102811792/190489934-2a6d09f2-656e-4d63-b14e-e2f55c24e96e.gif)
![enter-name-too-long](https://user-images.githubusercontent.com/102811792/190489944-0cdcf8cc-bf04-4498-a788-9124c601a3bf.gif)

__Menu__
- Options on the menu can be chosen by entering 1, 2, or 3. There is validation and if any characters inputted are not the 1, 2 or 3 an error is raised and the player is asked to choose again.

![image](https://user-images.githubusercontent.com/102811792/190493507-562cc7dc-0d88-4124-baef-a89481b8db5f.png)

![start-game-wrong](https://user-images.githubusercontent.com/102811792/190493540-c76bb65b-6e62-4668-bcd2-53c0a1c2e774.gif)

__Play Hangman__
- Choosing this option starts the game and randomly selects a word from words.py and shows it hidden so only the length is visible. The current hangman state image is shown alongside the players lives.

![start-game](https://user-images.githubusercontent.com/102811792/190493892-b2e9a825-fa3b-4fce-878a-674a5f83f67f.gif)

__Leaderboard__
- This can be accessed after choosing a player name and displays the top 5 players who have the most wins of all time. This is achieved by connecting a Google Sheet API with the python code.

![image](https://user-images.githubusercontent.com/102811792/190490923-1607140b-fd17-4108-acf7-72c87c884242.png)

__Exit Game__
- The game can be exited at multiple points and displays a personal message including the player name.

![image](https://user-images.githubusercontent.com/102811792/190491252-0ac317d5-02d9-41c9-8ce0-bb20ae561a00.png)
![image](https://user-images.githubusercontent.com/102811792/190491330-e53439bb-a548-45d3-b389-3825ca73bb52.png)

__Guess Input__
- A guess is made by the player which can either be correct, wrong or already guessed. Either a single letter can be entered or an entire word.

![guess-correct](https://user-images.githubusercontent.com/102811792/190492234-269744c7-0708-420b-b19c-f508f135807a.gif)
![guess-wrong](https://user-images.githubusercontent.com/102811792/190492255-03db14d5-8e55-41b9-b482-fa6874d1ea08.gif)
![guess-already](https://user-images.githubusercontent.com/102811792/190492275-d114708c-984e-4c54-bf72-825b6c3adfeb.gif)

- Here is a word being entered instead of a letter.

![guess-word](https://user-images.githubusercontent.com/102811792/190492980-f183e902-30ce-43e8-a160-01463fcd104d.gif)

- Guesses also have validation which end with errors being raised. If the guess contains any NON alphabet characters a message is displayed and the player is prompted to enter their guess again.

![guess-non-alphabet](https://user-images.githubusercontent.com/102811792/190492544-f4ecae1c-1a93-4b6f-aa00-81ed0a719e9e.gif)

- If the guess contains any leading or trailing whitespace this'll be stripped and their answer will be accepted as long as it meets the above validation.
![guess-space-strip](https://user-images.githubusercontent.com/102811792/190492716-18669396-d18d-4cc9-9d3d-b6bd964666db.gif)


__Guessed Letters & Words__
- Any guesses the player has already entered will be displayed if an incorrect guess is made or the player enters one of the guesses already entered previously.

![image](https://user-images.githubusercontent.com/102811792/190491803-540778f2-b861-458c-9451-ad2849a863f1.png)
![image](https://user-images.githubusercontent.com/102811792/190491937-d23cbab2-c38d-42bd-8f5c-ff5ca960a6c8.png)

__Winning and Losing__
- After the player either discovers the answer or runs out of lives depends if they see the you win or you lose screen. The correct answer is revealed either way and the players wins or loses will be incremented based on their outcome. A message is printed showing the players overall wins and loses.

![image](https://user-images.githubusercontent.com/102811792/190494480-b265d8a8-c216-4bce-ba72-c6d21c21255c.png)
![image](https://user-images.githubusercontent.com/102811792/190494676-73fe168a-b792-4dd4-a3e0-f1a0052dc3df.png)

__Play Again__
- When the player reaches the end of the game they will be asked to play again. If they enter Y the game loops and takes them back to the menu. If N is chosen then the game ends and shows the exit game message. This input also has validation and if anything other then Y or N is entered an error is raised and the input is asked for again.

![image](https://user-images.githubusercontent.com/102811792/190495091-db81a820-806d-461f-82b3-4ec045199204.png)

![play-again-yes](https://user-images.githubusercontent.com/102811792/190495951-9d0e0c4c-7dbf-4910-bd5b-fb79204831a0.gif)
![play-again-no](https://user-images.githubusercontent.com/102811792/190495969-985501f9-0b06-4fa6-b13d-7d38503ffe14.gif)
![play-again-wrong](https://user-images.githubusercontent.com/102811792/190495918-6670fa5c-5e2e-4cb3-a969-b76a5dac1827.gif)

### Future Features

- Difficulty setting for both harder more obscure words and also varying amount of lives to make it harder or easier.

## Design Documents

__Flow Chart__
-This flow chart shows the basic rules and choices made as the game is played.
![Hangman-FlowChart](https://user-images.githubusercontent.com/102811792/190488034-5bf1e6af-45e5-48a0-b563-776c4f98edb1.png)

## Data Model/ Classes

### Class Hangman

Parameters
----------
player_name : str
The name inputted by the player used to play and score in the game.

Attributes
----------
lives : int
The amount of attempts before the player reaches the fail state of the game.

guessed_letters : list, str
An empty list that will store the players already guessed letters.

guessed_words : list, str
An empty list that will store the players already guessed words.

wins : int
Keeps track of how many wins the player has

loses : int
Keeps track of how many loses the player has

#### Methods

- __init__
- update_player
- menu_options
- start_game
- hangman_state
- random_word
- player_guess
- update_leaderboard
- view_leaderboard
- play_again
- print_lives
- print_already_guessed
- guess_correct
- guess_wrong
- already_guessed
- letter_guess
- word_guess
- win_game
- lose_game
- main

## Libraries used

__natsort__
- This is used to naturally sort the leader board as originally it was sorted like 9, 8, 44, 3, 12, 1. Natsort changes this to sort them like 44, 12, 9, 8, 3, 1.

__random__
- Random library is used to pick a random word from the words.py hangman_words list.

__colorama__
- Used to color text through the Python code.

__gspread & google.oauth__
- Connect to Google Sheets API to amend and update the worksheet.

List out the python libraries you purposefully used in your project and why. You can look at your requirements.txt file and go back to https://pypi.org/ to rediscover the purpose of a library if needed.

A bulleted list is a good presentation for this information.

## Testing



### Validation Testing

__run.py__
![image](https://user-images.githubusercontent.com/102811792/190501397-513931ed-b41f-45b9-9ceb-5b947a875e7f.png)

__words.py__
![image](https://user-images.githubusercontent.com/102811792/190502292-e0f7e6e0-6c48-4b8e-8377-4e1c98453f0d.png)

### Manual Testing



### Defect Tracking



### Defects of Note



### Outstanding Defects



### Commenting Code



## Deployment

### Requirements



### Gitpod



### Heroku


#### Fork the repository


#### New Project



#### Settings


#### Deploy



## Credits

### Content


### Media


### Acknowledgments

Google Sheets integration from Love Sandwiches

