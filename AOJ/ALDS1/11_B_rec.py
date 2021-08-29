from typing import Dict, List

AdjList = Dict[int, List[int]]


class Dfs:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self, adj_l: AdjList):
        self.adj_l: AdjList = adj_l
        self.d = {}
        self.f = {}
        self.color = {v_id: self.WHITE for v_id in self.adj_l}
        self.time = 0

    def dfs(self):
        for u_id in self.adj_l:
            if self.color[u_id] == self.WHITE:
                self.dfs_visit(u_id=u_id)

    def dfs_visit(self, u_id):
        self.time += 1
        self.d[u_id] = self.time
        self.color[u_id] = self.GRAY
        for v_id in self.adj_l[u_id]:
            if self.color[v_id] == self.WHITE:
                self.dfs_visit(u_id=v_id)

        self.time += 1
        self.f[u_id] = self.time
        self.color[u_id] = self.BLACK

    def print_ans(self):
        for v_id in self.adj_l:
            print(v_id, self.d[v_id], self.f[v_id])


def main():
    n = int(input())
    adj_l: AdjList = {}
    for _ in range(n):
        u, k, *v = map(int, input().split())
        adj_l[u] = v
    d = Dfs(adj_l=adj_l)
    d.dfs()
    d.print_ans()


main()
