from typing import Optional, Dict, Union, List

Key = Union[int, str]


class Node:
    def __init__(self, key: Key, parent=None, rank=0):
        self.key: Key = key
        self.parent: Optional['Node'] = parent
        self.rank = rank


class DisjointSet:
    def __init__(self):
        self.nodes: Dict[Key, Node] = {}

    def make_set(self, x: Key):
        self.nodes[x] = Node(key=x)

    def find_set(self, x: Key) -> Key:
        xn = self.nodes[x]
        while xn.parent:
            xn = xn.parent
        return xn.key

    def is_already_exist(self, x: Key):
        return x in self.nodes

    def is_same(self, x: Key, y: Key):
        return self.find_set(x=x) == self.find_set(x=y)

    def unite(self, x: Key, y: Key):
        xroot = self.nodes.get(self.find_set(x=x))
        yroot = self.nodes.get(self.find_set(x=y))
        if self.is_same(x=x, y=y):
            return

        if xroot.rank > yroot.rank:
            yroot.parent = xroot
        else:
            xroot.parent = yroot
            if xroot.rank == yroot.rank:
                yroot.rank += 1


class Edge:
    def __init__(self, s, t, w):
        self.s = s
        self.t = t
        self.w = w


def main():
    v, e = map(int, input().split())
    edges: List[Edge] = []
    ds = DisjointSet()
    for _ in range(e):
        s, t, w = map(int, input().split())
        if not ds.is_already_exist(x=s):
            ds.make_set(x=s)
        if not ds.is_already_exist(x=t):
            ds.make_set(x=t)
        edges.append(Edge(s=s, t=t, w=w))

    sorted_edges = sorted(edges, key=lambda edge: edge.w)
    ans = 0
    for edge in sorted_edges:
        if not ds.is_same(x=edge.s, y=edge.t):
            ans += edge.w
            ds.unite(x=edge.s, y=edge.t)

    print(ans)


main()
