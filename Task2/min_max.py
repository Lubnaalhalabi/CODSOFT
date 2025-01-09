from game_strategy import GameStrategy

class Minimax(GameStrategy):
    """
    Perform a Minimax search to evaluate a position.
    """
    def evaluate(self, position, depth, maximizing_player, alpha=None, beta=None):
        try:
            # Base case: if depth is 0 or the game is over, evaluate the position
            if depth == 0 or self.game.is_game_over(position):
                return self.game.evaluate_position(position)

            # Maximizing player's turn
            if maximizing_player:
                max_eval = float('-inf')
                for child in self.game.get_children(position):
                    eval = self.evaluate(child, depth - 1, False)
                    max_eval = max(max_eval, eval)
                return max_eval

            # Minimizing player's turn
            else:
                min_eval = float('inf')
                for child in self.game.get_children(position):
                    eval = self.evaluate(child, depth - 1, True)
                    min_eval = min(min_eval, eval)
                return min_eval
        except Exception as e:
            print(f"Error in Minimax evaluation: {e}")
            return 0 

