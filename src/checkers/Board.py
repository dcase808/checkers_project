from .constants import BOARD_HEIGHT, BOARD_WIDTH, STATE_RED, STATE_BLACK
from .Pawn import Pawn

class Board:
    def __init__(self):
        self.pawns = []
        self.init_board()
        self.legal_moves = self.generate_legal_moves()
    
    def init_board(self):
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                if i < 3:
                    if i != 1 and i % 2 == 0 and j % 2 == 1: 
                        self.pawns.append(Pawn((i, j), STATE_BLACK))
                    elif i == 1 and j % 2 == 0:
                        self.pawns.append(Pawn((i, j), STATE_BLACK))
                elif i > 4:
                    if i == 6 and j % 2 == 1: 
                        self.pawns.append(Pawn((i, j), STATE_RED))
                    elif i != 6 and j % 2 == 0:
                        self.pawns.append(Pawn((i, j), STATE_RED))
    
    def generate_legal_moves(self):
        out = []
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    out.append((i, j))
        return out