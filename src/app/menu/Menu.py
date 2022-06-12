import sys
from checkers.Game import Game
from checkers.constants import WINDOW_HEIGHT, WINDOW_WIDTH, STATE_RED, STATE_BLACK
import pygame as pg
import pygame_menu

class Menu:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.game_mode = 0
        self.color = STATE_BLACK
        self.menu = None
        self.run_menu()

    def run_menu(self):
        self.menu = pygame_menu.Menu('Checkers', WINDOW_WIDTH, WINDOW_HEIGHT, theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button('Play', self.start_game)
        self.menu.add.selector('Game mode :', [('Versus', 0), ('Very Easy', 1), ('Easy', 2), ('Medium', 3), ('Hard', 4)], onchange=self.change_mode)
        self.menu.add.selector('Select your color :', [('Red', STATE_BLACK), ('White', STATE_RED)], onchange=self.change_color)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.window)
    
    def change_mode(self, mode, value):
        self.game_mode = value
    
    def start_game(self):
        # self.menu.disable()
        Game((WINDOW_WIDTH, WINDOW_HEIGHT), self.game_mode, self.color)
    
    def change_color(self, color, value):
        self.color = value
