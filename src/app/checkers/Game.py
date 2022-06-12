import pygame as pg
from .Board import Board
from .constants import BOARD_HEIGHT, BOARD_WIDTH, STATE_RED, STATE_BLACK
from ai.Minimax import Minimax

class Game:
    def __init__(self, resolution, game_mode, ai):
        self.board = Board()
        pg.init()
        self.window = pg.display.set_mode(resolution)
        self.window.fill('white')
        self.font = pg.font.SysFont(None, 40)
        self.game_mode = game_mode
        self.running = True
        self.winner = None
        self.ai = ai
        self.game_loop()

    def game_loop(self): 
        clock = pg.time.Clock()
        while self.running:
            while not self.winner:
                clock.tick(60)
                self.window.fill('white')
                self.draw_board()
                self.draw_score()
                self.draw_pieces()
                pg.display.update()
                self.check_if_over()
                if self.game_mode:
                    if self.board.who_to_move == self.ai:
                        minimax = Minimax(self.game_mode, self.board, self.ai)
                        minimax.run()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                        self.winner = 404
                    else:
                        self.event_handler(event)
            clock.tick(60)
            self.window.fill('white')
            text_winner = self.font.render(f'WINNER: {"RED" if self.winner == STATE_RED else "WHITE"}', True, (0, 0, 0))
            text_winner2 = self.font.render(f'press any key to continue', True, (0, 0, 0))
            self.window.blit(text_winner, (400, 400))
            self.window.blit(text_winner2, (320, 700))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                    self.running = False
    
    def check_if_over(self):
        if self.board.who_to_move == STATE_RED and len(self.board.all_moves_red) == 0:
            self.winner = STATE_BLACK
        elif self.board.who_to_move == STATE_BLACK and len(self.board.all_moves_black) == 0:
            self.winner = STATE_RED
        elif len(self.board.red_pawns) == 0:
            self.winner = STATE_BLACK
        elif len(self.board.black_pawns) == 0:
            self.winner = STATE_RED

    def draw_score(self):
        text_surface = self.font.render(f'White: {self.board.score_black}', True, (0, 0, 0))
        text_surface2 = self.font.render(f'Red: {self.board.score_red}', True, (0, 0, 0))
        text_surface3 = self.font.render(f'{"Reds turn" if self.board.who_to_move == STATE_RED else "Whites turn"}', True, (0, 0, 0))
        self.window.blit(text_surface, (830, 200))
        self.window.blit(text_surface2, (830, 600))
        self.window.blit(text_surface3, (830, 400))
    
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
                if pawn.is_clicked():
                    pg.draw.circle(self.window, (155, 0, 0), (x * 100 + 50, y * 100 + 50), 30)
                    for pos in pawn.get_available_moves():
                        y, x = pos
                        pg.draw.circle(self.window, (0, 255, 0), (x * 100 + 50, y * 100 + 50), 10)
                else:
                    pg.draw.circle(self.window, (255, 0, 0), (x * 100 + 50, y * 100 + 50), 30)
            elif pawn.get_state() == STATE_BLACK:
                if pawn.is_clicked():
                    pg.draw.circle(self.window, (155, 155, 155), (x * 100 + 50, y * 100 + 50), 30)
                    for pos in pawn.get_available_moves():
                        y, x = pos
                        pg.draw.circle(self.window, (0, 255, 0), (x * 100 + 50, y * 100 + 50), 10)
                else:
                    pg.draw.circle(self.window, (255, 255, 255), (x * 100 + 50, y * 100 + 50), 30)
            if pawn.get_is_king():
                pg.draw.circle(self.window, (0, 0, 0), (x * 100 + 50, y * 100 + 50), 10)

    def event_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.board.click_pawn_event(pg.mouse.get_pos())
