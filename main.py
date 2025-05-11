import pygame
import sys

# 初期化
pygame.init()
WIDTH, HEIGHT = 300, 600
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
    screen.fill((0, 0, 0))

    # 画面を更新
    pygame.display.flip()

    # フレームレートを設定
    clock.tick(60)