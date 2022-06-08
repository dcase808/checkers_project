import pygame as pg
from .Board import Board
from .constants import BOARD_HEIGHT, BOARD_WIDTH, STATE_RED, STATE_BLACK

class Engine:
    def __init__(self, resolution):
        self.board = Board()
        pg.init()
        self.window = pg.display.set_mode(resolution)
        self.window.fill('white')
        self.game_loop()

    def game_loop(self): 
        running = True
        clock = pg.time.Clock()
        while running:
            clock.tick(60)
            self.draw_board()
            self.draw_pieces()
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                else:
                    self.event_handler(event)
    
    def draw_board(self):
        for row in range(BOARD_HEIGHT):
            for col in range(BOARD_WIDTH):
                if col % 2 == 1 and row % 2 == 0:
                    pg.draw.rect(self.window, (0, 0, 0), (row * 100, col * 100, 100, 100))
                elif col % 2 == 0 and row % 2 == 1:
                    pg.draw.rect(self.window, (0, 0, 0), (row * 100, col * 100, 100, 100))

    def draw_pieces(self):
        for pawn in self.board.pawns:
            y, x = pawn.get_position()
            if pawn.get_state() == STATE_RED:
                pg.draw.circle(self.window, (255, 0, 0), (x * 100 + 50, y * 100 + 50), 30)
            if pawn.get_state() == STATE_BLACK:
                pg.draw.circle(self.window, (255, 255, 255), (x * 100 + 50, y * 100 + 50), 30)

    def event_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            for pawn in self.board.pawns:
                x, y = pg.mouse.get_pos()
                pos = (y // 100, x // 100)
                if pawn.is_clicked():
                    print('we here, clicked')
                    pawn.set_position(pos)
                    pawn.set_clicked(False)
                elif pawn.get_position() == pos and not pawn.is_clicked():
                    for p in self.board.pawns:
                        p.set_clicked(False)
                    print('we here, not clicked')
                    pawn.set_clicked(True)



            x, y = pos
            # print(x // 100, y // 100)
