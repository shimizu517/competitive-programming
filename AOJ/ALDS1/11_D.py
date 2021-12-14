import sys
from collections import defaultdict
from typing import Dict, Union

sys.setrecursionlimit(500000)


class Graph:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self):
        self.adj_list = defaultdict(list)
        self.color: Dict[int, Union['Graph.WHITE', 'Graph.GRAY', 'Graph.BLACK']] = defaultdict(lambda: self.WHITE)
        self.group = dict()  # connected component用のディクショナリ

    def append(self, s: int, t: int):
        self.adj_list[s].append(t)
        self.adj_list[t].append(s)

    def dfs(self):
        group_id = 0
        for s in self.adj_list:
            if self.color[s] == self.WHITE:
                group_id += 1
                self.dfs_visit(s, group_id)

    def dfs_visit(self, s: int, group_id: int):
        self.group[s] = group_id
        self.color[s] = self.GRAY
        for t in self.adj_list[s]:
            if self.color[t] == self.WHITE:
                self.dfs_visit(t, group_id)
        self.color[s] = self.BLACK

    def can_reach(self, s: int, t: int) -> bool:
        if s not in self.group or t not in self.group:
            return False
        return self.group[s] == self.group[t]


def main():
    _, m = map(int, input().split(' '))
    g = Graph()
    for _ in range(m):
        g.append(*map(int, input().split(' ')))
    g.dfs()
    n = int(input())
    for _ in range(n):
        print('yes' if g.can_reach(*map(int, input().split(' '))) else 'no')


main()
