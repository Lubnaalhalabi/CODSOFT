# Tic Tac Toe with Minimax and Alpha-Beta Pruning Strategies
This project implements a Tic Tac Toe game with two artificial intelligence (AI) strategies:
- Minimax: A brute-force AI strategy that evaluates all possible game states to determine the optimal move.
- Alpha-Beta Pruning: An optimized version of Minimax that eliminates unnecessary evaluations, reducing the computation time.
The user plays as (`X`) against the computer (`O`). The game is developed using Python and the Tkinter library for the graphical user interface (GUI).

# Key Features
1. Game Strategies
   - Minimax: Explores all possible moves to find the best one.
   - Alpha-Beta Pruning: Optimizes Minimax by pruning unnecessary branches of the search tree.
2. User Interface
   - A simple and interactive GUI built with Tkinter.
   - Buttons for selecting the AI strategy (Minimax or Alpha-Beta).
   - Reset button to restart the game.
3. Game Flow
   - Players take turns making moves.
   - The game announces the winner at the end.

# File Structure
- game_strategy.py: Defines the abstract base class GameStrategy for AI strategies.
- alpha_beta.py: Implements the AlphaBeta strategy, a subclass of GameStrategy.
- min_max.py: Implements the Minimax strategy, a subclass of GameStrategy.
- tic_tac_toe_ui.py: Defines the TicTacToeApp class, which handles the GUI and game logic.
- main.py: Contains the main function to run the application. It allows users to select a strategy and start the game.

# How to Run the Application
1. Clone the repository.
2. Navigate to the project directory.
3. Run the main script: python main.py.
4. Select a Strategy: Choose either Minimax or Alpha-Beta from the strategy selection window.
5. Play the Game:
   - Make your moves by clicking on the grid buttons.
   - The game will announce the result after each round.

# How the AI Works
1. Minimax Algorithm
   - Explores all possible game states recursively.
   - Maximizing player (`O`) tries to maximize the score, while minimizing player (`X`) tries to minimize it.
2. Alpha-Beta Pruning
   - Adds two parameters: `alpha` (best already explored option for the maximizer) and `beta` (best already explored option for the minimizer).
   - Prunes branches where further exploration cannot affect the outcome, improving efficiency.

# TicTacToeApp
Manages the game logic and GUI.
- player_move: Handles the player's move.
- comp_move: Handles the computer's move using the selected strategy.
- check_game_over: Checks if the game has ended.
- reset_game: Resets the game state.

