# **Ludo: From Empires to Epidemics**

## **Description**

This project recreates Ludo, a traditional South Asian game I grew up playing in Pakistan, in a digital format using Python and Pygame. It’s part of my broader "Window into Pakistan" project—an interactive platform for exploring Pakistani culture and politics. The game traces Ludo’s evolution from its origins as "Pachisi" in the Mughal Empire, through its rebranding under British colonialism, to its modern digital form. By blending gameplay with interactive storytelling, this project shows how a simple game can transcend time and cultures, using technology to reclaim and share cultural legacies

### **Key Features:**
- 2-4 players on a turn-by-turn basis and point-and-click moving tokens based on classic Ludo rules.
- Historical narrative! And three different board interfaces and three different sets of tokens that change as a narrative progresses--from ancient Pachisi, to Ludo after patent, to digital Ludo. The tokens' positioning is not affected by the change.
- Ability to handle game rules like first turn on a 6 dice, kicking another token off the board, etc.
- Animations including texts, zooming in, ship sailing, etc.
- Randomized dice movements.
- Various buttons, pop-ups, and "You Win!" win condition
---

## **Project Structure**
```
├── images/               # Images and animations in the game
├── LudoPachisi.py        # Main game
├── README.md             # This README file
├── requirements.txt      # Python dependencies
├── LudoWorksCited.txt    # Sources used!
└── OldLudo.py            # Old version of the game
```

---

## **Getting Started**

### **Prerequisites**

- Python 3.x
- Pygame library

Specifically, pygame 2.6.1!

### **Installing/Running in Virtual Environment**

If you want to run everything in a Python virtual environment (recommended), instructions are below. Otherwise, skip! First, download Python with your preferred method. Then...

1. Clone or download the repository by running this in terminal.
```bash
git clone https://github.com/alvs210/LudoGame
```
2. Create your environment by running this in the terminal:
```
python -m venv .venv_name
```
you might need to replace "python" with python3 or your specific python version

3. Run your virtual environment:
```
cd .venv_name/bin
source ./activate
```
You should see your virtual environment's name in parentheses at the beginning of your command prompt. Now, download pygame 
```
pip install pygame
```
4. And then run the downloaded game by navigating into "LudoGame-main" (the name of this folder) and then running
```
python LudoPachisi.py
```
A few seconds later, a window should pop up!! Enjoy!!

### **Installing/Running without Virtual Environment**

1. Clone or download the repository by running this in terminal.
```bash
git clone https://github.com/alvs210/LudoGame
```
2. Navigate to the project directory.
```bash
cd path-to-the-project-depending-on-where-you-saved-it
```
3. Install required dependencies (if you have not via virtual environment).
```bash
pip install python
pip install pygame
```
4. Run the game.
```bash
python LudoPachisi.py
```

## **How to Play**

### **Objective:**
Each player must move all four of their tokens from the start to the home column by completing a circuit around the board.

### **Game Rules:**
1. **Starting the Game:**
   - Each player selects a color. The tokens already begin in the starting position.
   - To move a token from the home base, the player must roll a 6.
  
2. **Rolling the Dice:**
   - Players take turns rolling the dice (via a button) and move their tokens by clicking on them.
   - Tokens move clockwise around the board.

3. **Movements:**
   - Landing on an opponent's token sends their token back to the start position.
   - You can only exit the starting position with a "6" rolled.
   - You must roll the exact number of places remaining to reach the home base (center) and earn a point.
  
4. **Winning:**
   - The first player to move all four tokens into the home base and thus earns 4 points wins the game.

---

## **Future Plans**
- Improve digital design!! Graphic designing needed
- Add more customization options for game rules and token designs.
- Add historically relevant changes (examples: cowrie shells were used isntead of dices earlier, and tokens moved counterclockwise instead of clockwise)
- Implement multiplayer functionality over a network.
- Expand historical contexts with additional time periods and interactive storytelling.

---

## **Acknowledgements**
- BIG Shotuout to my brother Tauseef Nadeem for using his anthropological brain to guide me through this project and to Joel Mire for his reassuring compsci statements. Also Hala Mohammed for being so incredibly supportive and letting me demo on her multiple times.
