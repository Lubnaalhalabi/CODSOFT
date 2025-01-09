from game_strategy import GameStrategy

class AlphaBeta(GameStrategy):
    """
    Perform an Alpha-Beta pruning search to evaluate a position.
    """
    def evaluate(self, position, depth, maximizing_player, alpha=float('-inf'), beta=float('inf')):
        try:
            # Base case: if depth is 0 or the game is over, evaluate the position
            if depth == 0 or self.game.is_game_over(position):
                return self.game.evaluate_position(position)
            
            # Maximizing player's turn
            if maximizing_player:
                max_eval = float('-inf')
                for child in self.game.get_children(position):
                    eval = self.evaluate(child, depth - 1, False, alpha, beta)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  
                return max_eval
            
            # Minimizing player's turn
            else:
                min_eval = float('inf')
                for child in self.game.get_children(position):
                    eval = self.evaluate(child, depth - 1, True, alpha, beta)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  
                return min_eval
        except Exception as e:
            print(f"Error in AlphaBeta evaluation: {e}")
            return 0