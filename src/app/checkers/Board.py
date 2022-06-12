from copy import deepcopy
from .constants import BOARD_HEIGHT, BOARD_WIDTH, STATE_RED, STATE_BLACK
from .Pawn import Pawn

class Board:
    def __init__(self):
        self.pawns = []
        self.red_pawns = []
        self.black_pawns = []
        self.__init_board()
        self.legal_moves = []
        self.__generate_legal_moves()
        self.free_tiles = []
        self.all_moves_red = []
        self.all_moves_black = []
        self.__generate_free_tiles()
        self.__generate_available_moves()
        self.__generate_red_and_black_pawns()

        self.clicked = None
        self.who_to_move = STATE_RED
        self.score_red = 0
        self.score_black = 0
    
    def __init_board(self):
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
    
    def __generate_red_and_black_pawns(self):
        for pawn in self.pawns:
            if pawn.get_state() == STATE_RED:
                self.red_pawns.append(pawn)
            elif pawn.get_state() == STATE_BLACK:
                self.black_pawns.append(pawn)
    
    def __generate_legal_moves(self):
        out = []
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    out.append((i, j))
        self.legal_moves = out
    
    def __generate_available_moves(self):
        for pawn in self.pawns:
            pawn.clear_available_moves()
            y, x = pawn.get_position()
            if pawn.get_is_king():
                if (y - 1, x - 1) in self.free_tiles:
                    pawn.add_available_move((y - 1, x - 1))
                elif (y - 2, x - 2) in self.free_tiles:
                    for temp_pawn in self.pawns:
                        if temp_pawn.get_position() == (y - 1, x - 1) and temp_pawn.get_state() != pawn.get_state():       
                            pawn.add_available_move((y - 2, x - 2))
                if (y - 1, x + 1) in self.free_tiles:
                    pawn.add_available_move((y - 1, x + 1))
                elif (y - 2, x + 2) in self.free_tiles:
                    for temp_pawn in self.pawns:
                        if temp_pawn.get_position() == (y - 1, x + 1) and temp_pawn.get_state() != pawn.get_state():       
                            pawn.add_available_move((y - 2, x + 2))
                if (y + 1, x + 1) in self.free_tiles:
                    pawn.add_available_move((y + 1, x + 1))
                elif (y + 2, x + 2) in self.free_tiles:
                    for temp_pawn in self.pawns:
                        if temp_pawn.get_position() == (y + 1, x + 1) and temp_pawn.get_state() != pawn.get_state():       
                            pawn.add_available_move((y + 2, x + 2))
                if (y + 1, x - 1) in self.free_tiles:
                    pawn.add_available_move((y + 1, x - 1))
                elif (y + 2, x - 2) in self.free_tiles:
                    for temp_pawn in self.pawns:
                        if temp_pawn.get_position() == (y + 1, x - 1) and temp_pawn.get_state() != pawn.get_state():       
                            pawn.add_available_move((y + 2, x - 2))
            else:
                y, x = pawn.get_position()
                if pawn.get_state() == STATE_RED:
                    if (y - 1, x - 1) in self.free_tiles:
                        pawn.add_available_move((y - 1, x - 1))
                    elif (y - 2, x - 2) in self.free_tiles:
                        for temp_pawn in self.pawns:
                            if temp_pawn.get_position() == (y - 1, x - 1) and temp_pawn.get_state() != pawn.get_state():       
                                pawn.add_available_move((y - 2, x - 2))
                    if (y - 1, x + 1) in self.free_tiles:
                        pawn.add_available_move((y - 1, x + 1))
                    elif (y - 2, x + 2) in self.free_tiles:
                        for temp_pawn in self.pawns:
                            if temp_pawn.get_position() == (y - 1, x + 1) and temp_pawn.get_state() != pawn.get_state():       
                                pawn.add_available_move((y - 2, x + 2))
                if pawn.get_state() == STATE_BLACK:
                    if (y + 1, x + 1) in self.free_tiles:
                        pawn.add_available_move((y + 1, x + 1))
                    elif (y + 2, x + 2) in self.free_tiles:
                        for temp_pawn in self.pawns:
                            if temp_pawn.get_position() == (y + 1, x + 1) and temp_pawn.get_state() != pawn.get_state():       
                                pawn.add_available_move((y + 2, x + 2))
                    if (y + 1, x - 1) in self.free_tiles:
                        pawn.add_available_move((y + 1, x - 1))
                    elif (y + 2, x - 2) in self.free_tiles:
                        for temp_pawn in self.pawns:
                            if temp_pawn.get_position() == (y + 1, x - 1) and temp_pawn.get_state() != pawn.get_state():       
                                pawn.add_available_move((y + 2, x - 2))
        self.all_moves_red = []
        self.all_moves_black = []
        for pawn in self.pawns:
            if pawn.get_state() == STATE_RED:
                for move in pawn.get_available_moves():
                    self.all_moves_red.append(move)
            if pawn.get_state() == STATE_BLACK:
                for move in pawn.get_available_moves():
                    self.all_moves_black.append(move)
    
    def __generate_free_tiles(self):
        out = deepcopy(self.legal_moves)
        for pawn in self.pawns:
            try:
                out.remove(pawn.get_position())
            except:
                pass
        self.free_tiles = out

    def switch_who_to_move(self):
        if self.who_to_move == STATE_RED:
            self.who_to_move = STATE_BLACK
        elif self.who_to_move == STATE_BLACK:
            self.who_to_move = STATE_RED
    
    def click_pawn_event(self, position):
        x, y = position
        pos = (y // 100, x // 100)
        if self.clicked and pos in self.legal_moves and pos in self.free_tiles:
            if self.move_pawn(self.clicked, pos):
                self.switch_who_to_move()
            self.clicked.set_clicked(False)
            self.clicked = None
        elif not self.clicked:
            for pawn in self.pawns:
                if pawn.get_position() == pos and self.who_to_move == pawn.get_state():
                    pawn.set_clicked(True)
                    self.clicked = pawn
        else:
            self.clicked.set_clicked(False)
            self.clicked = None
        self.__generate_free_tiles()
        self.__generate_available_moves()

    def move_pawn(self, pawn, pos):
        self.__generate_free_tiles()
        self.__generate_available_moves()
        if pos in pawn.get_available_moves():
            if pawn.get_state() == STATE_BLACK and not pawn.get_is_king():
                new_y, new_x = pos
                y, x = pawn.get_position()
                if new_y == y + 1 and abs(new_x - x) == 1:
                    pawn.set_position(pos)
                    return True
                elif new_y == y + 2 and abs(new_x - x) == 2:
                    if new_x > x and (y + 1, x + 1) not in self.free_tiles:
                        self.__capture_pawn((y + 1, x + 1))
                        pawn.set_position(pos)
                        return True
                    elif new_x < x and (y + 1, x - 1) not in self.free_tiles:
                        self.__capture_pawn((y + 1, x - 1))
                        pawn.set_position(pos)
                        return True
            elif pawn.get_state() == STATE_RED and not pawn.get_is_king():
                new_y, new_x = pos
                y, x = pawn.get_position()
                if new_y == y - 1 and abs(new_x - x) == 1:
                    pawn.set_position(pos)
                    return True
                elif new_y == y - 2 and abs(new_x - x) == 2:
                    if new_x > x and (y - 1, x + 1) not in self.free_tiles:
                        self.__capture_pawn((y - 1, x + 1))
                        pawn.set_position(pos)
                        return True
                    elif new_x < x and (y - 1, x - 1) not in self.free_tiles:
                        self.__capture_pawn((y - 1, x - 1))
                        pawn.set_position(pos)
                        return True
            elif pawn.get_is_king():
                new_y, new_x = pos
                y, x = pawn.get_position()
                if abs(new_y - y) == 1 and abs(new_x - x) == 1:
                    pawn.set_position(pos)
                    return True
                elif (new_y == y + 2 and abs(new_x - x) == 2) or (new_y == y - 2 and abs(new_x - x) == 2):
                    if (new_y == y + 2 and new_x == x + 2) and (y + 1, x + 1) not in self.free_tiles:
                        self.__capture_pawn((y + 1, x + 1))
                        pawn.set_position(pos)
                        return True
                    elif (new_y == y + 2 and new_x == x - 2) and (y + 1, x - 1) not in self.free_tiles:
                        self.__capture_pawn((y + 1, x - 1))
                        pawn.set_position(pos)
                        return True
                    elif (new_y == y - 2 and new_x == x + 2) and (y - 1, x + 1) not in self.free_tiles:
                        self.__capture_pawn((y - 1, x + 1))
                        pawn.set_position(pos)
                        return True
                    elif (new_y == y - 2 and new_x == x - 2) and (y - 1, x - 1) not in self.free_tiles:
                        self.__capture_pawn((y - 1, x - 1))
                        pawn.set_position(pos)
                        return True
        return False
    
    def __capture_pawn(self, pos):
        for pawn in self.pawns.copy():
            if pawn.get_position() == pos:
                self.pawns.remove(pawn)
                if pawn.get_state() == STATE_BLACK:
                    self.score_red += 1
                    self.black_pawns.remove(pawn)
                elif pawn.get_state() == STATE_RED:
                    self.score_black += 1
                    self.red_pawns.remove(pawn)