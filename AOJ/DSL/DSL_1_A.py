from typing import Optional, Dict, Union

KeyType = Union[int, str]

__all__ = ['DisjointSet']


class Node:
    def __init__(self, key, rank=0, parent=None):
        self.key: KeyType = key
        self.parent: Optional['Node'] = parent
        self.rank = rank


# 利用者はKeyTypeのデータを入れられることだけ知っている

class DisjointSet:
    def __init__(self):
        self.nodes: Dict[KeyType, Node] = {}

    def make_set(self, x: KeyType):
        if x in self.nodes:
            raise Exception
        self.nodes[x] = Node(key=x)

    def find_set(self, x: KeyType) -> KeyType:
        xn = self.nodes.get(x)
        while xn.parent:
            xn = xn.parent
        return xn.key

    def union(self, x: KeyType, y: KeyType):
        xroot_node = self.nodes[self.find_set(x)]
        yroot_node = self.nodes[self.find_set(y)]
        if self.is_same(x=x, y=y):
            return

        if xroot_node.rank > yroot_node.rank:
            yroot_node.parent = xroot_node
        else:
            xroot_node.parent = yroot_node
            if xroot_node.rank == yroot_node.rank:
                yroot_node.rank += 1

    def is_same(self, x: KeyType, y: KeyType):
        return self.find_set(x) == self.find_set(y)


def main():
    n, q = map(int, input().split())
    ds = DisjointSet()
    for i in range(n):
        ds.make_set(x=i)

    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            ds.union(x=x, y=y)
        else:
            print(int(ds.is_same(x=x, y=y)))


main()
