import pygame

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 9, 9
SQUARE_SIZE = (WIDTH - 50) // COLS
PADDING = 25

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game Assets
X = pygame.transform.scale(pygame.image.load('assets/x.png'), (32, 32))
O = pygame.transform.scale(pygame.image.load('assets/o.png'), (32, 32))
X_big = pygame.transform.scale(pygame.image.load('assets/x.png'), (112, 112))
O_big = pygame.transform.scale(pygame.image.load('assets/o.png'), (112, 112))
