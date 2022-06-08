class Pawn:
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state
        self.is_king = False
    
    def __str__(self):
        return f'{self.state} at {self.pos}'
    
    def make_king(self):
        self.is_king = True
    
    def get_position(self):
        return self.pos
    
    def get_state(self):
        return self.state