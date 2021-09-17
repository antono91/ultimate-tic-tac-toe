import pygame
from .constants import SQUARE_SIZE, PADDING, X, O

class Symbol:

    def __init__(self, row, col, symbol):
        self.type = symbol
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.y = PADDING + (self.row * SQUARE_SIZE)
        self.x = PADDING + (self.col * SQUARE_SIZE)
    
    def draw(self, win):
        win.blit(X if self.type == "X" else O, (self.x + ((SQUARE_SIZE - X.get_width())//2), self.y + ((SQUARE_SIZE - X.get_height())//2)))
