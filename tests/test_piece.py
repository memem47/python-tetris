from piece import Piece

def test_rotation_cycle():
    p = Piece('I', 0, 0)
    first = p.blocks
    p.rotate()
    p.rotate()
    p.rotate()
    p.rotate()
    assert p.blocks == first