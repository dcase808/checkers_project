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
    
    def get_position(self):
        return self.pos
    
    def get_state(self):
        return self.state
    
    def set_position(self, pos):
        self.pos = pos
    
    def set_clicked(self, state):
        self.clicked = state
    
    def is_clicked(self):
        return self.clicked