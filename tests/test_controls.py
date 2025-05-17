import main, importlib
from piece import Piece

def setup_function():
    importlib.reload(main)
    main.board[:] = [[None] * main.COLS for _ in range(main.ROWS)]

def test_move_left_right():
    p = Piece('I', 5, 0)
    assert main.is_valid(p, -1, 0)
    assert main.is_valid(p, 1, 0)

def test_rotation_invalid_then_revert():
    p = Piece('I', 0, 0)
    p.rotate()
    assert not main.is_valid(p)
