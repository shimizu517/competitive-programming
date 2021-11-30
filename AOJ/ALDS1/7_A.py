# 2021/11/30 未完成

from collections import defaultdict
from typing import Optional, List, Dict


class Node:
    def __init__(self, _id=-1, parent=None, left=None, right=None):
        self.id = _id
        self.parent: Optional['Node'] = parent
        self.left: Optional['Node'] = left
        self.right: Optional['Node'] = right

    def __str__(self):
        return f'node {self.id}: parent = {self.parent.id if self.parent else "-1"}, depth = {self.depth}, {self.type}, ' \
               f'[{", ".join(map(str, self.children_id))}]'

    @property
    def type(self):
        if self.parent is None:
            return 'root'
        elif self.left is None:
            return 'leaf'
        else:
            return 'internal node'

    @property
    def children_id(self) -> List[int]:
        # leftがなければ空配列を返す
        if self.left is None:
            return []
        # leftがあればleftのrightを再帰的にたどる
        result: List[int] = []
        cur = self.left
        while cur is not None:
            result.append(cur.id)
            cur = cur.right
        return result

    @property
    def depth(self):
        d = 0
        cur = self
        while cur.parent and cur.parent.id != -1:
            d += 1
            cur = cur.parent
        return d


def set_node_if_not_exists(d: Dict[int, Node], _id: int):
    if d[_id].id == -1:
        d[_id] = Node(_id=_id)


def main():
    n = int(input())
    nodes = defaultdict(Node)
    for _ in range(n):
        _id, k, *children_id = map(int, input().split(' '))
        set_node_if_not_exists(nodes, _id)
        if k > 0:
            first_c_id = children_id[0]
            set_node_if_not_exists(nodes, first_c_id)
            nodes[first_c_id].parent = nodes[_id]  # set parent
            nodes[_id].left = nodes[first_c_id]  # set child
            for idx in range(1, len(children_id)):
                set_node_if_not_exists(nodes, children_id[idx - 1])
                set_node_if_not_exists(nodes, children_id[idx])
                nodes[children_id[idx - 1]].right = nodes[children_id[idx]]
    for idx in sorted(nodes):
        print(nodes[idx])


main()
