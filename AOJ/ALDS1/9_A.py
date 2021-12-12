from typing import Optional, List


class Node:
    def __init__(self, key: Optional[int] = None):
        self.key: int = key

    def __str__(self):
        return f'key: {self.key}'

    @property
    def is_nil(self) -> bool:
        return self.key is None


class Heap:
    nil = Node()

    def __init__(self):
        self.nodes: List[Node] = []

    @staticmethod
    def get_parent_idx(idx: int):
        return (idx - 1) // 2

    @staticmethod
    def get_left_idx(idx: int):
        return idx * 2 + 1

    @staticmethod
    def get_right_idx(idx: int):
        return idx * 2 + 2

    def insert(self, key: int):
        n = Node(key=key)
        self.nodes.append(n)

    def print(self):
        for idx, n in enumerate(self.nodes):
            text = f'node {idx + 1}: key = {n.key}, '
            if idx != 0:
                text += f'parent key = {self.nodes[self.get_parent_idx(idx)].key}, '
            if self.get_left_idx(idx) < len(self.nodes):
                text += f'left key = {self.nodes[self.get_left_idx(idx)].key}, '
            if self.get_right_idx(idx) < len(self.nodes):
                text += f'right key = {self.nodes[self.get_right_idx(idx)].key}, '
            print(text)


def main():
    _ = int(input())
    keys = list(map(int, input().split(' ')))
    h = Heap()
    for k in keys:
        h.insert(key=k)
    h.print()


main()
