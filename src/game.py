import pygame
from .board import Board


class Game:

    def __init__(self, win):
        self.board = Board()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def select(self, row, col):
        moves = self.board.get_possible_moves()
        if (row, col) in moves:
            self.board.move(row, col)
            if self.board.is_field_won(self.board.get_field(row // 3, col // 3)):
                self.board.field_won[row // 3][col // 3] = self.board.turn
                return self.board.is_game_won()
            self.board.change_turn()
