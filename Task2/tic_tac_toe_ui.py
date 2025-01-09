import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, master, strategy_class):
        # Initialize the game window and variables
        self.master = master
        self.master.title("Tic Tac Toe")

        # Initialize game variables
        self.board = {i: ' ' for i in range(1, 10)}
        self.player = 'X'
        self.bot = 'O'
        self.strategy = strategy_class(self)

        # Create UI components
        self.buttons = {}
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    master,
                    text=" ",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.player_move(row, col),
                )
                button.grid(row=i, column=j)
                self.buttons[(i, j)] = button

        # Reset button for restarting the game
        self.reset_button = tk.Button(
            master, text="Reset", font=("Arial", 14), command=self.reset_game
        )
        self.reset_button.grid(row=3, column=0, columnspan=3)
        
        # Status label to show whose turn it is
        self.status_label = tk.Label(master, text="Your Turn!", font=("Arial", 14))
        self.status_label.grid(row=4, column=0, columnspan=3)

    def board_to_grid(self, board_position):
        """
        Converts board position to grid coordinates
        """
        return divmod(board_position - 1, 3)

    def grid_to_board(self, row, col):
        """
        Converts grid coordinates to board position
        """    
        return row * 3 + col + 1

    def player_move(self, row, col):
        """
        Handles the player's move
        """
        try: 
            position = self.grid_to_board(row, col)
            if self.is_space_free(position):
                self.insert_letter(self.player, position)
                self.update_board()
                if self.check_game_over():
                    return
                self.status_label.config(text="Computer's Turn")
                self.master.after(100, self.comp_move)
            else:
                messagebox.showinfo("Invalid Move", "This space is already occupied!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during the player's move: {e}")

    def comp_move(self):
        """
        Handles the computer's move using the strategy class
        """
        try: 
            best_score = float('-inf')
            best_move = None
            for key in self.board.keys():
                if self.is_space_free(key):
                    self.board[key] = self.bot
                    score = self.strategy.evaluate(self.board, 0, False)
                    self.board[key] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = key

            if best_move:
                self.insert_letter(self.bot, best_move)
                self.update_board()
                if self.check_game_over():
                    return
                self.status_label.config(text="Your Turn!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during the computer's move: {e}")

    def update_board(self):
        """
        Updates the UI based on the current state of the board
        """
        try:
            for position, mark in self.board.items():
                row, col = self.board_to_grid(position)
                self.buttons[(row, col)].config(text=mark)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while updating the board: {e}")

    def is_space_free(self, position):
        """
        Check if a given position on the board is free.
        """
        return self.board[position] == ' '

    def insert_letter(self, letter, position):
        """
        Insert a player's or bot's letter into the specified position on the board.
        """
        self.board[position] = letter

    def check_which_mark_won(self, mark):
        """
        Check if the given mark has won the game.
        """
        try:

            win_patterns = [
                (1, 2, 3), (4, 5, 6), (7, 8, 9),  
                (1, 4, 7), (2, 5, 8), (3, 6, 9),  
                (1, 5, 9), (3, 5, 7)              
            ]
            return any(
                self.board[a] == self.board[b] == self.board[c] == mark
                for a, b, c in win_patterns
            )
        except Exception as e:
            print(f"Error in check_which_mark_won: {e}")
            return False

    def check_for_win(self):
        """
        Check if either player or bot has won the game.
        """
        try:
            return self.check_which_mark_won(self.player) or self.check_which_mark_won(self.bot)
        except Exception as e:
            print(f"Error in check_for_win: {e}")
            return False

    def is_game_over(self):
        """
        Check if the game is over (all spaces filled).
        """
        return all(space != ' ' for space in self.board.values())

    def check_game_over(self):
        """
        Checks if the game is over due to a win or draw
        """
        try:

            if self.check_for_win():
                winner = "Player" if self.check_which_mark_won(self.player) else "Computer"
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.disable_buttons()
                return True

            if self.is_game_over():
                messagebox.showinfo("Game Over", "Game Over!")
                self.disable_buttons()
                return True

            return False
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while checking if the game is over: {e}")
            return False

    def disable_buttons(self):
        """
        Disables all buttons after the game is over
        """
        try:

            for button in self.buttons.values():
                button.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while disabling the buttons: {e}")

    def reset_game(self):
        """
        Resets the game to the initial state
        """
        try:
            self.board = {i: ' ' for i in range(1, 10)}
            for button in self.buttons.values():
                button.config(text=" ", state=tk.NORMAL)
            self.status_label.config(text="Your Turn!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while resetting the game: {e}")

    def get_children(self, position):
        """
        Generate all possible next positions (children) based on the current board state.
        """
        try:
            children = []
            for key in self.board.keys():
                if self.is_space_free(key):
                    new_board = position.copy()  
                    new_board[key] = self.bot if self.board == position else self.player
                    children.append(new_board)
            return children
        except Exception as e:
            print(f"Error in get_children: {e}")
            return []

    def evaluate_position(self, position):
        """
        Evaluate the current board position.
        """
        try:
            if self.check_which_mark_won(self.bot):
                return 1
            elif self.check_which_mark_won(self.player):
                return -1
            else:
                return 0
        except Exception as e:
            print(f"Error in evaluate_position: {e}")
            return 0