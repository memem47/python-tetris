import pygame, sys, random
from piece import Piece, SHAPES

# ---- 1. 定数 ------------------------------------------------
GRID = 30
COLS, ROWS = 10, 20
WIDTH, HEIGHT = COLS * GRID, ROWS * GRID
FPS = 60
FALL_MS = 500  # 落下間隔（ミリ秒）

board = [[None] * COLS for _ in range(ROWS)]  # 

score = 0
pygame.font.init()
font = pygame.font.SysFont(None, 28)

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

def is_valid(piece, dx=0, dy=0):
    """ピースが移動可能かチェック"""
    for col, row in piece.coordinates():
        nx, ny = col + dx, row + dy
        # 1) wall, floor
        if nx < 0 or nx >= COLS or ny >= ROWS:
            return False
        # 2) existing blocks
        if board[ny][nx]:
            return False
    return True

def lock_piece(piece):
    """ピースをロックしてボードに追加"""
    for col, row in piece.coordinates():
        board[row][col] = piece.shape
    
def draw_board(surface):
    color_map = {
        'I': "cyan",
        'O': "yellow",
        'T': "purple",
        'S': "lime",
        'Z': "red",
        'L': "orange",
        'J': "blue"
    }
    for y, line in enumerate(board):
        for x, cell in enumerate(line):
            if cell:
                rect = pygame.Rect(x * GRID, y * GRID, GRID, GRID)
                pygame.draw.rect(surface, color_map[cell], rect)
                pygame.draw.rect(surface, "black", rect, 1)

def check_full_lines():
    """
    完全に埋まった行番号リストを返す（下から上）
    """
    full = [y for y, line in enumerate(board) if all(line)]
    return sorted(full, reverse=True)

def clear_lines(lines):
    global score
    for y in sorted(lines, reverse=True):
        del board[y]
        board.insert(0, [None] * COLS)
    score += 100 * len(lines)  # スコア加算

def main():
    # ---- 3. Pygame 初期化 ------------------------------------------------
    running = True
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Tetris")
    clock = pygame.time.Clock()
    current = spawn_piece()
    fall_time = 0

    # ---- 4. メインループ ------------------------------------------------
    while running:
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
                    if not is_valid(current):
                        current.rotate()
                        current.rotate()
                        current.rotate() # 3回戻す
                elif event.key == pygame.K_LEFT and is_valid(current, -1, 0):
                    current.col -= 1
                elif event.key == pygame.K_RIGHT and is_valid(current, 1, 0):
                    current.col += 1
                elif event.key == pygame.K_DOWN and is_valid(current, 0, 1):
                    current.row += 1
        # --- 自動落下 ---
        if fall_time >= FALL_MS:
            if is_valid(current,0,1):
                current.row += 1
            else:
                lock_piece(current)
                lines = check_full_lines()
                if lines:
                    clear_lines(lines)
                current = spawn_piece()
                if not is_valid(current):
                    running = False
                    break
                    
            fall_time = 0

        # --- 描画 ---
        screen.fill("black")
        draw_grid(screen)
        draw_board(screen)
        draw_piece(screen, current)
        score_surf =font.render(f"Score: {score}", True, "white")
        screen.blit(score_surf, (10, 5))
        pygame.display.flip()

    # --- ゲームオーバー ---
    game_over_surf = font.render("Game Over", True, "red")
    rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_surf, rect)
    pygame.display.flip()
    pygame.time.wait(3000) # 3 秒表示

if __name__ == "__main__":
    main()