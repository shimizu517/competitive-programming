import sys
from sys import stdin
from typing import List, Callable


class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)

    @property
    def is_nil(self):
        return self.key is None


class BinarySearchTree:
    def __init__(self):
        self.nil = Node()
        self.root = self.nil

    def insert(self, key: int):
        node = Node(key=key)
        node.left = node.right = self.nil
        x = self.root
        y = self.nil
        while not x.is_nil:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y.is_nil:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def print_ordered_id(self, order_func: Callable[[Node, List[Node]], None]):
        result = []
        order_func(self.root, result)
        print(' ' + ' '.join(map(str, result)))

    def print_inorder(self):
        result = []

        def order_by_inorder(node: Node):
            if node.is_nil:
                return
            order_by_inorder(node=node.left)
            result.append(node)
            order_by_inorder(node=node.right)

        order_by_inorder(self.root)
        print(' ' + ' '.join(map(str, result)))

    def print_preorder(self):
        result = []

        def order_by_preorder(node: Node):
            if node.is_nil:
                return
            result.append(node)
            order_by_preorder(node=node.left)
            order_by_preorder(node=node.right)

        order_by_preorder(self.root)
        print(' ' + ' '.join(map(str, result)))

    @classmethod
    def order_by_inorder(cls, node: Node, result: List[Node]):
        if node.is_nil:
            return
        cls.order_by_inorder(node=node.left, result=result)
        result.append(node)
        cls.order_by_inorder(node=node.right, result=result)

    @classmethod
    def order_by_preorder(cls, node: Node, result: List[Node]):
        if node.is_nil:
            return
        result.append(node)
        cls.order_by_preorder(node=node.left, result=result)
        cls.order_by_preorder(node=node.right, result=result)


bt = BinarySearchTree()


def main():
    readline = stdin.readline
    n = int(input())
    for i in sys.stdin.readlines():
        if i[0] == 'i':
            key = int(i[7:])
            bt.insert(key=key)
        else:
            bt.print_inorder()
            bt.print_preorder()
    # ↑TLEになったり通ったりしている。よくわからん
    # for _ in range(n):
    #     _input = readline()[:-1].split(' ')
    #     if _input[0] == 'insert':
    #         bt.insert(key=int(_input[1]))
    #     elif _input[0] == 'print':
    #         bt.print_ordered_id(BinarySearchTree.order_by_inorder)
    #         bt.print_ordered_id(BinarySearchTree.order_by_preorder)


main()
