from copy import deepcopy
from checkers.constants import STATE_RED, STATE_BLACK

class Minimax:
    def __init__(self, depth, board):
        self.original_board = board
        self.board = deepcopy(board)
        self.depth = depth
        self.maximizing_player = STATE_RED
        self.best_move = None

    def __evaluate(self, board):
        return board.score_black - board.score_red
    
    def run(self):
        self.minimax(self.board, self.depth, -9999, 9999, True)
        for pawn in self.original_board.pawns.copy():
            if pawn.get_position() == self.best_move[0]:
                self.original_board.move_pawn(pawn, self.best_move[1])
                self.original_board.switch_who_to_move()

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0:
            return self.__evaluate(board)
        
        if maximizing_player:
            max_eval = -9999
            for pawn in board.black_pawns:
                for move in pawn.get_available_moves():
                    temp_board = deepcopy(board)
                    temp_move = (pawn.get_position(), move)
                    temp_board.move_pawn(pawn, move)
                    eval = self.minimax(temp_board, depth - 1, alpha, beta, False)
                    if eval > max_eval and depth == self.depth:
                        self.best_move = temp_move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = 9999
            for pawn in board.red_pawns:
                for move in pawn.get_available_moves():
                    temp_board = deepcopy(board)
                    temp_board.move_pawn(pawn, move)
                    eval = self.minimax(temp_board, depth - 1, alpha, beta, True)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval
