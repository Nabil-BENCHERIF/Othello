
# Othello Game – Python Implementation

This is a Python implementation of the classic board game **Othello** (also known as Reversi). The game includes different types of players such as human, random, and AI-based strategies including Minimax.

## 🎮 Features

- Complete Othello game logic
- Command-line interface
- Multiple player strategies:
  - Human player
  - Random moves
  - One-step lookahead
  - Minimax algorithm

## 🗂️ Project Structure

```

nabil-bencherif-othello/
├── README.md              # Project description
├── game.py                # Game loop and player interactions
├── LICENSE.txt            # MIT License
├── main.py                # Main entry point
├── Noeud.py               # Tree node logic (used in AI algorithms)
├── othello.py             # Core Othello game logic and rules
└── Joueurs/               # Player modules
├── **init**.py
├── joueur\_aleatoire.py   # Random strategy
├── joueur\_horizon\_1.py   # One-move horizon AI
├── joueur\_humain.py      # Human player interface
└── joueur\_minimax.py     # Minimax AI

````

## ▶️ How to Run

1. Make sure you have **Python 3** installed.
2. Clone this repository or download the source.
3. Run the game from the root directory:

```bash
python3 main.py
````

You will be prompted to choose the players and start the game in the terminal.

## 🤖 Player Strategies

* **Human**: Input your move via the console.
* **Random**: Chooses a legal move at random.
* **Horizon 1**: Selects the move that maximizes immediate gain.
* **Minimax**: Uses the Minimax algorithm for deeper strategic play.

## 📝 License

This project is released under the [MIT License](LICENSE.txt). Feel free to use, modify, and distribute it.

## 📌 TODO / Ideas for Improvement

* Add GUI using `tkinter` or `pygame`
* Implement alpha-beta pruning for Minimax
* Add training-based AI (e.g. reinforcement learning)
* Save/load game state

---

Enjoy playing and hacking Othello in Python! 😄




