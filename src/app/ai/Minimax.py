from copy import deepcopy
from checkers.constants import STATE_RED, STATE_BLACK

class Minimax:
    def __init__(self, depth, board, maximizing_player):
        self.original_board = board
        self.board = deepcopy(board)
        self.depth = depth
        self.maximizing_player = maximizing_player
        self.best_move = (0, 0), (0, 0)

    def __evaluate(self, board):
        if self.maximizing_player == STATE_BLACK:
            return board.score_black - board.score_red
        else:
            return board.score_red - board.score_black
    
    def is_over(self, board):
        if board.who_to_move == STATE_RED and len(board.all_moves_red) == 0:
            return True
        elif board.who_to_move == STATE_BLACK and len(board.all_moves_black) == 0:
            return True
        elif len(board.red_pawns) == 0:
            return True
        elif len(board.black_pawns) == 0:
            return True
    
    def run(self):
        print(f'real eval: {self.minimax(self.board, self.depth, -9999, 9999, True)}')
        for pawn in self.original_board.pawns.copy():
            if pawn.get_position() == self.best_move[0]:
                self.original_board.move_pawn(pawn, self.best_move[1])
                self.original_board.switch_who_to_move()

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.is_over(board):
            return self.__evaluate(board)
        
        if maximizing_player:
            max_eval = -9999
            if self.maximizing_player == STATE_RED:
                for pawn in board.red_pawns:
                    for move in pawn.get_available_moves():
                        temp_board = deepcopy(board)
                        temp_move = (pawn.get_position(), move)
                        temp_board.move_pawn(pawn, move)
                        eval = self.minimax(temp_board, depth - 1, alpha, beta, False)
                        if eval > max_eval and depth == self.depth:
                            self.best_move = temp_move
                            print(self.best_move)
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
                return max_eval
            else:
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
            if self.maximizing_player == STATE_BLACK:
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
            else:
                for pawn in board.black_pawns:
                    for move in pawn.get_available_moves():
                        temp_board = deepcopy(board)
                        temp_board.move_pawn(pawn, move)
                        eval = self.minimax(temp_board, depth - 1, alpha, beta, True)
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
                return min_eval