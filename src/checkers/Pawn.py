from .constants import STATE_BLACK, STATE_RED

class Pawn:
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state
        self.is_king = False
        self.clicked = False
    
    def __str__(self):
        return f'{self.state} at {self.pos}'
    
    def make_king(self):
        self.is_king = True
    
    def get_is_king(self):
        return self.is_king
    
    def get_position(self):
        return self.pos
    
    def get_state(self):
        return self.state
    
    def set_position(self, pos):
        self.pos = pos
        if self.pos[0] == 7 and self.state == STATE_BLACK:
            self.make_king()
        if self.pos[0] == 0 and self.state == STATE_RED:
            self.make_king()
    
    def set_clicked(self, state):
        self.clicked = state
    
    def is_clicked(self):
        return self.clicked