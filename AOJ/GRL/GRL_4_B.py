from collections import deque
from typing import List, Deque

AdjList = List[List[int]]


class TopologicalSort:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self, adj_l: AdjList):
        self.adj_l = adj_l  # 0以上の数値が頂点のidである
        self.color: List[int] = [self.WHITE] * len(adj_l)
        self.topo_l: Deque[int] = deque()

    def dfs(self):
        for v_id, _ in enumerate(self.adj_l):
            if self.color[v_id] == self.WHITE:
                self.dfs_visit(v_id)

    def dfs_visit(self, u_id):
        self.color[u_id] = self.GRAY
        for v_id in self.adj_l[u_id]:
            if self.color[v_id] == self.WHITE:
                self.dfs_visit(u_id=v_id)
        self.color[u_id] = self.BLACK
        self.topo_l.appendleft(u_id)

    def print_ans(self):
        print(*self.topo_l)


def main():
    V, E = map(int, input().split())
    adj_l: AdjList = [[] for _ in range(V)]
    for _ in range(E):
        s, t = map(int, input().split())
        adj_l[s].append(t)
    t = TopologicalSort(adj_l=adj_l)
    t.dfs()
    t.print_ans()


main()
