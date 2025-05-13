from piece import Piece
from main import spawn_piece, COLS

def test_spawn_returns_piece():
    p = spawn_piece()
    assert isinstance(p, Piece)
    assert 0 <= p.col < COLS