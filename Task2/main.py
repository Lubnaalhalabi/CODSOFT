import tkinter as tk  
from min_max import Minimax 
from alpha_beta import AlphaBeta 
from tic_tac_toe_ui import TicTacToeApp  
from tkinter import messagebox  

def main():
    """
    Main function to run the application. 
    It displays a choice window to select the game strategy 
    (Minimax or AlphaBeta) and then launches the TicTacToe app.
    """
    try:
        # Create the root Tkinter window (hidden initially)
        root = tk.Tk()
        # Hide the root window to display only the choice window first
        root.withdraw()  

        # Create a secondary window for selecting the strategy
        choice_window = tk.Toplevel(root)
        choice_window.title("Choose Strategy")  

        def select_strategy(strategy):
            """
            Function to handle the strategy selection.
            Closes the choice window and initializes the TicTacToe app with the selected strategy.
            
            Args:
            - strategy (int): 1 for Minimax, 2 for AlphaBeta
            """
            # Choose the appropriate strategy class based on the user's selection
            strategy_class = Minimax if strategy == 1 else AlphaBeta
            choice_window.destroy()  
            root.deiconify()  
            app = TicTacToeApp(root, strategy_class) 

        # Add a label to the choice window
        tk.Label(choice_window, text="Choose a strategy:", font=("Arial", 14)).pack(pady=10)

        # Add buttons for selecting the Minimax strategy
        tk.Button(choice_window, text="Minimax", font=("Arial", 14), 
                  command=lambda: select_strategy(1)).pack(pady=5)

        # Add buttons for selecting the AlphaBeta strategy
        tk.Button(choice_window, text="AlphaBeta", font=("Arial", 14), 
                  command=lambda: select_strategy(2)).pack(pady=5)

        # Start the Tkinter event loop
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()  
