from copy import deepcopy
from typing import List

N1 = 3
N2 = N1 ** 2
"""
マンハッタン距離のメモ
以下の通りパネルの場所に番号をつけたとき、i->j のマンハッタン距離をMDT[i][j]に格納する。
以下の番号は場所を表すだけで、その場所に置かれるパネルが1オリジンかどうかは関係ない。
MDT=[[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
例）0->4へのマンハッタン距離は MDT[0][4]==2 となる
"""
MDT = [[None for _ in range(N2)] for _ in range(N2)]
for i in range(N2):
    for j in range(N2):
        MDT[i][j] = abs(i // N1 + j // N1) + abs(i % N1 - j % N1)


class Puzzle:
    dx = (-1, 0, 1, 0)
    dy = (0, -1, 0, 1)
    dir = ('u', 'l', 'd', 'r')
    ans_hash = hash(str([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))

    def __init__(self, board: List[List[int]]):
        self.board = board
        self.size = len(board)
        self.path = ''
        self.sx, self.sy = 0, 0
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == 0:
                    self.sx = r
                    self.sy = c
        self.md = self.get_all_md()

    def __hash__(self):
        return hash(str(self.board))

    def __eq__(self, other: 'Puzzle'):
        """同じ形の場合True"""
        return hash(other) == hash(self)

    # copy.deepcopy()の高速化
    def __deepcopy__(self, memo={}):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[hash(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result

    def __str__(self):
        return str(self.board)

    def __repr__(self):
        return self.__str__()

    @property
    def is_finished(self):
        return self.ans_hash == hash(self)

    def get_all_md(self):
        """パズルの空白以外のパネルの最終状態へのマンハッタン距離の和を返す"""
        _sum = 0
        for i in range(N2):
            sx, sy = i // N1, i % N1
            # board上のパネルを左上から順に取り出す
            v = self.board[sx][sy]
            # vは1オリジンのパネルがあるので、v-1の位置が最終状態。v==1なら、(0,0)の位置が最終状態。
            _sum += MDT[i][v - 1]
        return _sum


class EightPuzzleIDAStar:
    LIMIT = 100

    def execute(self, s: Puzzle):
        state = deepcopy(s)

    def dfs(self, depth: int, prev: int, state: Puzzle, limit: int) -> bool:
        if state.md == 0:
            return True
        if limit < depth + state.md:
            return False
        tmp: Puzzle
        for i in range(N1):
            tx = state.sx + Puzzle.dx[i]
            ty = state.sy + Puzzle.dy[i]
            if tx < 0 or ty < 0 or N1 <= tx or N1 <= ty:
                continue
            if max(prev, i) - min(prev, i) == 2:
                continue
            tmp = deepcopy(state)
            state.md -= MDT[tx * N1 + ty]


def main():
    board = []
    for _ in range(3):
        board.append(list(map(int, input().split())))
    p = Puzzle(board)
    path = EightPuzzle().execute(p)
    print(len(path))


main()
