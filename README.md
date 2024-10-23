# **Ludo: From Empires to Epidemics**

## **Description**

This project brings to life Ludo, a traditional South Asian game that I grew up playing in Pakistan, now recreated in a digital format using Python and Pygame. This project is part of my vision for a larger "Window into Pakistan," an interactive platform for exploring Pakistani culture, traditions, games, and stories through immersive digital storytelling. Through gameplay, I trace its historical transformation—from its origins as "Pachisi" in the Mughal Empire, to its rebranding as Ludo under British colonialism, and finally, to the modern digital version played worldwide today. By blending gameplay with interactive storytelling, this project highlights how a simple game can endure across centuries and cultures, while also reflecting on how technology can be a tool for reclaiming and sharing cultural legacies

### **Key Features:**
- **Historical Journey:** Each game section is tied to a specific moment in history, from 1750 in the Mughal Empire to 2020 during the COVID-19 pandemic.
- **Turn-based Gameplay:** Players take turns rolling dice and moving tokens, following the rules of Ludo, with intentional loopholes like skipping turns and re-rolling dices.
- **Digital Transformation:** The game evolves through time, eventually transitioning to a digital version, reflecting how Ludo has transformed over the centuries.
- **Interactive Storytelling:** Each phase of the game is accompanied by historical events that immerse the player in the era’s context.

---

## **Getting Started**

### **Prerequisites**

- Python 3.x
- Pygame library (To install, run `pip install pygame`)

### **Installation**

1. Clone or download the repository.
   ```bash
   git clone https://github.com/alvs210/LudoGame
   ```
2. Navigate to the project directory.
   ```bash
   cd path-to-the-project-depending-on-where-you-saved-it
   ```
3. Install required dependencies.
   ```bash
   pip install python
   pip install pygame
   ```
4. Run the game.
   ```bash
   python LudoPachisi.py
   ```
you need pygame==2.6.1 but that shouldn't need to be specified...

## **How to Play**

### **Objective:**
Each player must move all four of their tokens from the start to the home column by completing a circuit around the board.

### **Game Rules:**
1. **Starting the Game:**
   - Each player selects a color and places their tokens in the home base.
   - To move a token from the home base, the player must roll a 6.
  
2. **Rolling the Dice:**
   - Players take turns rolling the dice and move their tokens based on the roll.
   - Tokens move clockwise around the board.
   - Rolling a 6 allows for an additional roll.

3. **Landing on Opponents:**
   - Landing on an opponent's token sends their token back to the start position.
  
4. **Winning:**
   - The first player to move all four tokens into the home column wins the game.

### **Historical Context & Animations:**
- The game begins in **1750**, during the Mughal Empire, where you and your friends gather to play Pachisi.
- As the game progresses, different time periods are introduced, showing how the game evolves under British colonial rule and eventually into a digital version during the COVID-19 pandemic.

---

## **Project Structure**
```
├── assets/               # Images, animations, and assets for the game
├── LudoPachisi.py             # Main game logic
├── README.md             # This README file
├── requirements.txt      # Python dependencies
└── workscited.txt      # Sources used!
```

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
