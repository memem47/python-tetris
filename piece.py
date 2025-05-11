import random
import pygame

# -------------------------------------------------------
# テトロミノの形定義
#   各キーが1つのテトロミノ（I,O,T,S,Z,L,J）
#   値は「回転ごとの4ブロック座標」リスト
#   90°回転で形が重複するもの（I,S,Z）は2つだけ持たせています
# -------------------------------------------------------
SHAPES: dict[str, list[list[tuple[int, int]]]] = {
    'I': [
        [(0, -1), (0,0), (0, 1),(0, 2)], # 縦
        [(-1, 0), (0,0), (1,0),(2, 0)] # 横
    ],
    'O': [
        [(0, 0), (1,0), (0, 1),(1, 1)], # 正方形
    ],
    'T': [
        [(-1, 0), (0,0), (1, 0),(0, 1)], #
        [(0, -1), (0,0), (1, 0),(0, 1)], #
        [(-1, 0), (0,0), (1, 0),(0, -1)],
        [(0, -1), (0,0), (-1, 0),(0, 1)]
    ],
    'S': [
        [(0, 0), (1,0), (-1, 1),(0, 1)],
        [(0, -1), (0,0), (1, 0),(1, 1)]
    ],
    'Z': [
        [(-1, 0), (0, 0), (0, 1), (1, 1)],
        [(1, -1), (0, 0), (1, 0), (0, 1)]
    ],
    'L': [
        [(-1, 0), (0, 0), (1, 0), (-1, 1)],  # └─
        [(0, -1), (0, 0), (0, 1), (1, 1)],   # ├
        [(-1, 0), (0, 0), (1, 0), (1, -1)],  # ─┘
        [(0, -1), (0, 0), (0, 1), (-1, -1)]  # ┤
    ],
    'J': [
        [(-1, 0), (0, 0), (1, 0), (1, 1)],   # ┘
        [(0, -1), (0, 0), (0, 1), (1, -1)],  # ┤
        [(-1, -1), (-1, 0), (0, 0), (1, 0)], # ┌
        [(-1, 1), (0, -1), (0, 0), (0, 1)]   # ├
    ]
}

class Piece:
    """テトロミノのクラス"""
    def __init__(self, shape: str, col: int, row: int):
        self.shape = shape
        self.rot = 0
        self.col = col
        self.row = row
        self.blocks = SHAPES[shape][self.rot]

    def rotate(self):
        """回転"""
        self.rot = (self.rot + 1) % len(SHAPES[self.shape])
        self.blocks = SHAPES[self.shape][self.rot]

    def coordinates(self):
        """ブロック座標を取得"""
        return [(self.col + x, self.row + y) for x, y in self.blocks]

    @staticmethod
    def random_spawn(cols: int):
        """ランダムなテトロミノを生成"""
        shape = random.choice(list(SHAPES.keys()))
        col = cols//2
        return Piece(shape, col, 0)
    
    