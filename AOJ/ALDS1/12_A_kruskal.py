from typing import List, Tuple


class DisjointSet:
    def __init__(self):
        self.p = {}
        self.rank = {}

    def is_same(self, x: int, y: int) -> bool:
        return self.find_set(x) == self.find_set(y)

    def make_set(self, key: int):
        self.p[key] = key
        self.rank[key] = 0

    def unite(self, x: int, y: int):
        if self.is_same(x, y):
            return

        xr = self.find_set(x)
        yr = self.find_set(y)
        if self.rank[xr] < self.rank[yr]:
            self.p[xr] = yr
        elif self.rank[yr] < self.rank[xr]:
            self.p[yr] = xr
        else:
            self.rank[xr] += 1
            self.p[yr] = xr

    def find_set(self, key: int) -> int:
        p_key = self.p[key]
        while p_key != key:
            key = p_key
            p_key = self.p[p_key]
        return key


class Kruskal:
    def __init__(self):
        pass

    def execute(self, keys: List[int], edges: List[Tuple[int, Tuple[int, int]]]):
        edges = sorted(edges)
        ds = DisjointSet()
        result = 0
        for key in keys:
            ds.make_set(key=key)
        for w, st in edges:
            s = st[0]
            t = st[1]
            if not ds.is_same(s, t):
                result += w
                ds.unite(s, t)
        return result


def main():
    n = int(input())
    edges = []
    keys = []
    for s in range(n):
        keys.append(s)
        row = list(map(int, input().split()))
        for t, weight in enumerate(row[:s + 1]):
            if weight == -1:
                continue
            edges.append((weight, (s, t)))
    print(Kruskal().execute(keys=keys, edges=edges))


main()
