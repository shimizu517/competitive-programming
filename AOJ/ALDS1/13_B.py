import json
from collections import deque
from copy import deepcopy
from typing import List, Deque, Set


class Puzzle:
    dx = (-1, 0, 1, 0)
    dy = (0, -1, 0, 1)
    dir = ('u', 'l', 'd', 'r')
    ans_hash = hash(str([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))

    def __init__(self, board: List[List[int]]):
        self.board = board
        self.path = ''
        self.sx, self.sy = 0, 0
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == 0:
                    self.sx = r
                    self.sy = c

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

    @property
    def size(self):
        return 3


class EightPuzzle:
    def execute(self, s: Puzzle):
        Q: Deque[Puzzle] = deque()
        # ある状態が既出かどうか確認するためのset
        _set: Set[Puzzle] = set()
        Q.append(deepcopy(s))
        while 0 < len(Q):
            u = Q.popleft()
            if u.is_finished:
                return u.path
            for i in range(4):
                tx = u.sx + Puzzle.dx[i]
                ty = u.sy + Puzzle.dy[i]
                if tx < 0 or ty < 0 or u.size <= tx or u.size <= ty:
                    continue
                v = deepcopy(u)
                v.board[v.sx][v.sy], v.board[tx][ty] = v.board[tx][ty], v.board[v.sx][v.sy]
                v.sx, v.sy = tx, ty
                if v not in _set:
                    _set.add(v)
                    v.path += Puzzle.dir[i]
                    Q.append(v)


def main():
    board = []
    for _ in range(3):
        board.append(list(map(int, input().split())))
    p = Puzzle(board)
    path = EightPuzzle().execute(p)
    print(len(path))


main()
