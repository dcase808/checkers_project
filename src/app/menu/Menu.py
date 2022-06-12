from checkers.Game import Game
from checkers.constants import WINDOW_HEIGHT, WINDOW_WIDTH
import pygame as pg

class Menu:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.game_loop()
    
    def game_loop(self):
        clock = pg.time.Clock()
        while self.running:
            clock.tick(30)
            self.window.fill('white')
            pg.display.update()
            for event in pg.event.get():
                self.event_handler(event)

    def event_handler(self, event):
        if event.type == pg.QUIT:
            game = Game((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 0)
            pg.quit()