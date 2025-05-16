import sys, pathlib, os
sys.path.append(os.fspath(pathlib.Path(__file__).resolve().parents[1]))
from piece import Piece
import main

def setup_function():
    # board を毎テストごとに初期化
    main.board = [[None] * main.COLS for _ in range(main.ROWS)]

def test_bottom_collision():
    p = Piece('O', 4, main.ROWS - 2)  # 18行目（0-index）
    assert not main.is_valid(p, 0, 1)

def test_lock():
    p =  Piece('O', 4, main.ROWS - 2)
    main.lock_piece(p)
    # 4 block分がboardに埋まっているか
    filled = sum(cell is not None for row in main.board for cell in row)
    assert filled == 4