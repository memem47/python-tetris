import pygame
import sys

# 初期化
pygame.init()
GRID_SIZE = 30
COLS, ROWS = 10, 20
WIDTH, HEIGHT = COLS * GRID_SIZE, ROWS * GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 画面を黒で塗りつぶす
    screen.fill("black")

    # draw grid
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, "dimgray", (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, "dimgray", (0, y), (WIDTH, y))
        
    # 画面を更新
    pygame.display.flip()

    # フレームレートを設定
    clock.tick(60)