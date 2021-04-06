import sys
from typing import List, Set

sys.setrecursionlimit(500000)

AdjList = List[List[int]]


class DFS:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self, n, adj_l: AdjList):
        self.color = [self.WHITE] * n
        self.f: List[int] = []
        self.d: List[int] = []
        self.adj_l: AdjList = adj_l
        self.rev_adj_l: AdjList = [[] for _ in range(n)]
        self.sets: List[Set[int]] = []

    def _dfs(self):
        for v in range(len(self.adj_l)):
            if self.color[v] == self.WHITE:
                self._dfs_visit(v=v)

    def _dfs_visit(self, v):
        self.color[v] = self.GRAY
        self.d.append(v)
        for u in self.adj_l[v]:
            if self.color[u] == self.WHITE:
                self._dfs_visit(v=u)
        self.color[v] = self.BLACK
        self.f.append(v)

    def _transpose_adj_l(self):
        for v, l in enumerate(self.adj_l):
            for u in l:
                self.rev_adj_l[u].append(v)

    def _dfs2(self):
        self.color = [self.WHITE for _ in range(len(self.adj_l))]
        for idx, v in enumerate(reversed(self.f)):
            self.sets.append(set())
            if self.color[v] == self.WHITE:
                self._dfs_visit2(v=v, idx=idx)

    def _dfs_visit2(self, v, idx):
        self.sets[idx] |= {v}
        self.color[v] = self.GRAY
        self.d.append(v)
        for u in self.rev_adj_l[v]:
            if self.color[u] == self.WHITE:
                self._dfs_visit2(v=u, idx=idx)
        self.color[v] = self.BLACK
        self.f.append(v)

    def solve(self, q: List[List[int]]):
        self._dfs()
        self._transpose_adj_l()
        self._dfs2()
        for vs in q:
            self.check(q=vs)

    def check(self, q: List[int]):
        # おそらくここが遅くてTLE
        for _set in self.sets:
            if q[0] in _set and q[1] in _set:
                print(1)
                return
        print(0)


def main():
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V)]
    for _ in range(E):
        s, t = map(int, input().split())
        adj_l[s].append(t)
    Q = int(input())
    q = [list(map(int, input().split())) for _ in range(Q)]
    dfs = DFS(n=V, adj_l=adj_l)
    dfs.solve(q=q)


main()
