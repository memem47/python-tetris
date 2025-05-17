import main, importlib
from piece import Piece

def setup_function():
    # リロードしてボード初期化
    importlib.reload(main)
    main.board[:] = [[None] * main.COLS for _ in range(main.ROWS)]

def test_line_is_cleared():
    # 最下行を埋める
    main.board[-1] = ['I'] * main.COLS
    lines =main.check_full_lines()
    assert lines == [main.ROWS - 1]

    main.clear_lines(lines)
    assert all(cell is None for cell in main.board[0]) # 先頭行が空
    assert main.score == 100