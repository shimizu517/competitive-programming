from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, _id=None, parent=None, left=None, right=None):
        self.id: Optional[int] = _id
        self.parent: Optional[Node] = parent
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __str__(self):
        return f'id: {self.id}, left: {self.left_id}, right: {self.right_id}'

    @property
    def parent_id(self):
        return self.parent.id if self.parent is not None else -1

    @property
    def left_id(self):
        return self.left.id if self.left is not None else -1

    @property
    def right_id(self):
        return self.right.id if self.right is not None else -1

    @property
    def type(self):
        if self.parent_id == -1:
            return 'root'
        elif self.left_id == -1 and self.right_id == -1:
            return 'leaf'
        else:
            return 'internal node'

    @property
    def siblings(self):
        # 親がいない場合はsiblingがいない
        if self.parent_id == -1:
            return -1
        # 親の子が1つしかない、つまり自分自身しかいない場合はsiblingがいない
        if self.parent.left is None or self.parent.right is None:
            return -1
        # 親が2つ子をもつ場合は自分ではない親の子のidを返す
        if self.parent.left.id == self.id:
            return self.parent.right.id
        else:
            return self.parent.left.id

    @property
    def degree(self):
        return int(self.left_id != -1) + int(self.right_id != -1)

    @property
    def height(self):
        l_h = self.left.height + 1 if self.left_id != -1 else 0
        r_h = self.right.height + 1 if self.right_id != -1 else 0
        return max(l_h, r_h)

    @property
    def depth(self):
        cur = self
        d = 0
        while cur.parent:
            d += 1
            cur = cur.parent
        return d


class BinaryTree:
    def __init__(self):
        self.nodes = defaultdict(Node)

    def add_node(self, _id, left, right):
        node = self._set_node_if_not_exists(_id=_id)
        left = self._set_node_if_not_exists(_id=left)
        right = self._set_node_if_not_exists(_id=right)
        node.left = left
        node.right = right
        left.parent = node
        right.parent = node

    def _set_node_if_not_exists(self, _id: int) -> Node:
        if _id not in self.nodes:
            self.nodes[_id] = Node(_id=_id)
        return self.nodes[_id]

    def print_nodes(self):
        for _id in sorted([_id for _id in self.nodes if _id != -1]):
            node = self.nodes[_id]
            print(
                f'node {_id}: parent = {node.parent_id}, sibling = {node.siblings}, degree = {node.degree}, '
                f'depth = {node.depth}, height = {node.height}, {node.type}'
            )


NIL = Node()


def main():
    n = int(input())
    bt = BinaryTree()
    for _ in range(n):
        _id, left, right = map(int, input().split(' '))
        bt.add_node(_id, left, right)
    bt.print_nodes()


main()
