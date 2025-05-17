import importlib, main
from piece import Piece

def setup_function():
    importlib.reload(main)
    main.board[:] = [[None]*main.COLS for _ in range(main.ROWS)]

def test_game_over_detected():
    # 上部中央をブロックで埋める
    main.board[0][main.COLS//2] = 'O'
    p = main.spawn_piece()
    assert not main.is_valid(p)