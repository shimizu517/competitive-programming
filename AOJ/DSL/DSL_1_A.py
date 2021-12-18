from typing import Union

KeyType = Union[int, str]

__all__ = ['DisjointSet']


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


def main():
    n, q = map(int, input().split())
    ds = DisjointSet()
    for i in range(n):
        ds.make_set(i)

    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            ds.unite(x=x, y=y)
        else:
            print(int(ds.is_same(x=x, y=y)))


main()
