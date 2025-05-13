import pygame, sys, random
from piece import Piece, SHAPES

# ---- 1. 定数 ------------------------------------------------
GRID = 30
COLS, ROWS = 10, 20
WIDTH, HEIGHT = COLS * GRID, ROWS * GRID
FPS = 60
FALL_MS = 500  # 落下間隔（ミリ秒）

# ---- 2. ヘルパ関数 ----------------------------------------------
def draw_grid(surface):
    """グリッドを描画"""
    for x in range(0, WIDTH, GRID):
        pygame.draw.line(surface, "dimgray", (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID):
        pygame.draw.line(surface, "dimgray", (0, y), (WIDTH, y))

def draw_piece(surface, piece: Piece):
    COLORS = {
        'I': "cyan",
        'O': "yellow",
        'T': "purple",
        'S': "lime",
        'Z': "red",
        'L': "orange",
        'J': "blue"
    }
    for col, row in piece.coordinates():
        rect = pygame.Rect(col * GRID, row * GRID, GRID, GRID)
        pygame.draw.rect(surface, COLORS[piece.shape], rect)
        pygame.draw.rect(surface, "black", rect, 1)  # グリッド線を描画

def spawn_piece() -> Piece:
    """新しいテトロミノを生成"""
    shape = random.choice(list(SHAPES.keys()))
    col = COLS // 2
    return Piece(shape, col, 0)

# ---- 3. Pygame 初期化 ------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

current = spawn_piece()
fall_time = 0

# ---- 4. メインループ ------------------------------------------------
while True:
    dt = clock.tick(FPS)  # フレーム時間を取得
    fall_time += dt

    # --- 入力処理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current.rotate()

    # --- 自動落下 ---
    if fall_time >= FALL_MS:
        current.row += 1
        fall_time = 0

    # --- 描画 ---
    screen.fill("black")
    draw_grid(screen)
    draw_piece(screen, current)
    pygame.display.flip()
