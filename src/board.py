import pygame
from src.constants import ROWS, COLS, SQUARE_SIZE, BLACK, WHITE, WIDTH, HEIGHT, PADDING, X_big, O_big
from .symbol import Symbol


class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        self.turn = "X"
        self.field_won = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last = (-1, -1)

    def draw_board(self, win):
        win.fill(WHITE)

        for i in range(1, 3):
            pygame.draw.line(win, BLACK,
                             (PADDING + i * 3 * SQUARE_SIZE, PADDING),
                             (PADDING + i * 3 * SQUARE_SIZE, HEIGHT - PADDING),
                             4)
            pygame.draw.line(win, BLACK,
                             (PADDING, PADDING + i * 3 * SQUARE_SIZE),
                             (WIDTH - PADDING, PADDING + i * 3 * SQUARE_SIZE),
                             4)

        for i in range(3):
            for j in range(3):
                offset_x = j * SQUARE_SIZE * 3
                offset_y = i * SQUARE_SIZE * 3

                if self.field_won[i][j] != 0:
                    win.blit(X_big if self.field_won[i][j] == "X" else O_big,
                             (PADDING + offset_x +
                              (3 * SQUARE_SIZE - X_big.get_width()) // 2,
                              PADDING + offset_y +
                              (3 * SQUARE_SIZE - X_big.get_width()) // 2))
                else:
                    for r in range(2):
                        start_x = PADDING + ((r + 1) * SQUARE_SIZE) + offset_x
                        start_y = PADDING + 5 + offset_y
                        end_x = start_x
                        end_y = start_y + (3 * SQUARE_SIZE) - 10
                        pygame.draw.line(win, BLACK, (start_x, start_y),
                                         (end_x, end_y))
                    for c in range(2):
                        start_x = PADDING + 5 + offset_x
                        start_y = PADDING + ((c + 1) * SQUARE_SIZE) + offset_y
                        end_x = start_x + (3 * SQUARE_SIZE) - 10
                        end_y = start_y
                        pygame.draw.line(win, BLACK, (start_x, start_y),
                                         (end_x, end_y))

    def is_field_won(self, field):
        for i in range(3):
            if field[i][0] == self.turn and field[i][1] == self.turn and field[i][2] == self.turn:
                return True
            if field[0][i] == self.turn and field[1][i] == self.turn and field[2][i] == self.turn:
                return True
        if field[0][0] == self.turn and field[1][1] == self.turn and field[2][2] == self.turn:
            return True
        if field[0][2] == self.turn and field[1][1] == self and field[2][0] == self.turn:
            return True
        return False

    def is_game_won(self):
        if self.is_field_won(self.field_won):
            return True
        return False

    def get_field(self, row, col):
        field = []
        for i in range(3):
            field.append(
                [0 if self.board[row * 3 + i][col * 3 + j] == 0 else self.board[row * 3 + i][col * 3 + j].type for j in
                 range(3)])
        return field

    def get_possible_moves(self):
        moves = []
        next_field = (self.last[0] - (self.last[0] // 3 * 3), self.last[1] - (self.last[1] // 3 * 3))

        if self.field_won[next_field[0]][next_field[1]] != 0 or self.last == (-1, -1):
            for i in range(ROWS):
                for j in range(COLS):
                    if self.board[i][j] == 0 and self.field_won[i // 3][j // 3] == 0:
                        moves.append((i, j))
        else:
            for i in range(next_field[0]*3, next_field[0]*3 + 3):
                for j in range(next_field[1]*3, next_field[1]*3 + 3):
                    if self.board[i][j] == 0:
                        moves.append((i, j))
        return moves

    def move(self, row, col):
        self.board[row][col] = Symbol(row, col, self.turn)
        self.last = (row, col)

    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def draw(self, win):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0 and self.field_won[row // 3][col // 3] == 0:
                    self.board[row][col].draw(win)

    def create_board(self):
        for row in range(ROWS):
            self.board.append([0 for _ in range(COLS)])
