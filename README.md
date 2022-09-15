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

-The player starts by entering a valid name using alphabet characters no longer than 10 long.

![enter-name](https://user-images.githubusercontent.com/102811792/190483768-d42859b8-78c4-47ee-bd53-889efbdce4ef.gif)

-After entering their name the player can now choose between starting the game, viewing the leaderboard or exiting the game. Here is what happens when the player looks at the leaderboard. The leaderboard shows the top 5 players who have the highest wins.

![view_leaderboard](https://user-images.githubusercontent.com/102811792/190484395-dd56a25d-9bd0-46cb-921d-2f412e7becca.gif)

-When starting the game a random word is chosen from the words.py file and displayed as underscores. The current hangman image is displayed, at the start of the game there are no body parts added to the image. The lives are also displayed, when these run out the game is over.

![start-game](https://user-images.githubusercontent.com/102811792/190484490-bcc99ab0-0942-42d7-aca9-238dd1a42580.gif)

-The player can now enter guesses, letters or words, to replace the underscores with correct letters or even guess the entire word.

![guess-correct](https://user-images.githubusercontent.com/102811792/190484972-0b420b99-3e9f-4fec-8513-ebb09ce98af9.gif)
![guess-word](https://user-images.githubusercontent.com/102811792/190485183-e38608fd-20ec-4d44-8a72-1985861ee610.gif)

-If the player guesses all the correct letters or enters the correct word the game is over and the player has won. The games won score will increase by 1.

![you-win](https://user-images.githubusercontent.com/102811792/190486034-dcd8f35e-5f79-4d82-8f31-42ceee9adab3.gif)

-However, if the player does not guess the correct letters or word in 6 attempts the game is over and the player has lose. The games lost score will increase by 1.

![you-lost](https://user-images.githubusercontent.com/102811792/190486770-98a3c842-63c5-4ac0-a49e-d5ededdb53a0.gif)

-A play again message is shown where the player can choose Y to loop back to the menu selection or choose N to exit the game.

![play-again-yes](https://user-images.githubusercontent.com/102811792/190486971-3a134ea9-2b46-48c4-8ba5-6f5d12c76c75.gif)
![play-again-no](https://user-images.githubusercontent.com/102811792/190486987-163300cf-3625-45e0-b91c-163430691679.gif)

-The player's score is saved so even if they exit the game and return at a later date they can continue climbing the leaderboard.

## Features

### Implemented Features


### Future Features


## Design Documents


## Data Model/ Classes


### Class X
To better group the game as an object, I wrote a class representing its properties and had method functions to update those properties: 

**Properties**
- property 1: is a {string} it represents {something} 
- property 2: is a {string} it represents {something} 

**Methods**
- **\_\_init\_\_**: Initialize method, it starts the class off with default parameters as if a user just started to play a game.
- **\_\_str\_\_**: Returns a string representation of the class/object

## Libraries used

-natsort
-random
-

List out the python libraries you purposefully used in your project and why. You can look at your requirements.txt file and go back to https://pypi.org/ to rediscover the purpose of a library if needed.

A bulleted list is a good presentation for this information.

## Testing



### Validation Testing


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

