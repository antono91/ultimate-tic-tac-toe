import pygame
from src.constants import WIDTH, HEIGHT, SQUARE_SIZE, PADDING, ROWS, COLS
from src.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y - PADDING) // SQUARE_SIZE
    col = (x - PADDING) // SQUARE_SIZE
    return row, col


def main():
    running = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if 0 <= row < ROWS and 0 <= col < COLS:
                    if game.select(row, col):
                        running = False

        game.update()
    pygame.quit()


main()
