# Ludo Game

Ludo is a classic South Asian game that I played growing up in Pakistan! This Python-based game allows you to play Ludo with others on your laptop/computer :) 

# Features

- 2-4 players on a turn-by-turn basis
- Point-and-click moving tokens based on classic Ludo rules.
- Graphical interface with an embedded Ludo board image.
- Ability to handle game rules like first turn on a 6 dice, kicking another token off the board, etc.
- A dice roll button & "You Win!" win condition

# Demo



# Installation

Clone or download this repository. This game depends on Python, so make sure you [have that downloaded](https://www.python.org/downloads/)!
Install the Pygame library by running:
```
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install pygamw
```
(Note: We aren't downloading pygame to the global environment. We're using a virtual environment. Installing system-wide packages is usually risky!)
For issues during installation, check [here](https://www.pygame.org/wiki/GettingStarted).

# How to Play Game

Running the game varies based on your device! See [here](https://artofproblemsolving.com/wiki/index.php/How_to_run_Pygame_Programs) for more instructions.

On a Mac, open your terminal.  (Command+Space, then type terminal in the search box and press enter). Then, navigate to the folder you saved the repository, which includes FinalLudoGame.py file and the LudoGame.jpeg file. Then, run the following in the terminal:

```
python3  FinalLudo.py
```
Note: the LudoGame.jpeg image *must* be in the same folder, or this won't work! It'll give you the error :)

# Rules of the Game

1. The turns go in the order of yellow, green, red, blue.
2. Each player gets to roll the dice once. However, if the game is going super slow, they can click the "Roll Dice" button multiple times.
3. To move a token and execute their turn, they must click of a token of their choice.
4. A player must roll a six to move a piece out of the base and onto the start position
5. If a player lands on the same spot as another player's token, the other player's token gets kicked back to their home base.
6. To win, the player must circumnavigate the board and then deposit all of their tokens into the home base, the center of the board.
More detailed instructions [here](https://www.ymimports.com/pages/how-to-play-ludo)!

# Future Improvements

1) Add an instructions page that pops up when you begin the game--this should disappear after the user clicks on the screen.
2) Slow down tokens' movements.
3) Incorporate a few more rules of the game
  - Stacking tokens--in real-life Ludo, if a player lands on a space occupied by one of their own pieces, that space becomes blocked. A blocked space cannot be passed or landed on by      an opponent’s piece.
  - If a player rolls a six, they get an extra turn.
    
# Dependencies

Python 3.x or Python 2.x
Pygame

# Notes
