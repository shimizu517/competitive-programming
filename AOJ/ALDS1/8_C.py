import sys
from typing import Union


class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent: Node = parent
        self.left: Node = left
        self.right: Node = right

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

    def find(self, key: int) -> Node:
        x = self.root
        while not x.is_nil:
            if x.key == key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return self.nil

    def delete(self, key_or_node: Union[int, Node]):
        if isinstance(key_or_node, int):
            node: Node = self.find(key=key_or_node)
        elif isinstance(key_or_node, Node):
            node = key_or_node
        else:
            raise Exception()
        if node.is_nil:
            return
        if node.left.is_nil and node.right.is_nil:
            if self._get_is_node_left_of_parent(node):
                node.parent.left = self.nil
            else:
                node.parent.right = self.nil
        elif node.left.is_nil or node.right.is_nil:
            child = node.left if node.right.is_nil else node.right
            child.parent = node.parent
            if self._get_is_node_left_of_parent(node):
                node.parent.left = child
            else:
                node.parent.right = child
        else:
            successor: Node = self.get_successor(node)
            node.key = successor.key
            self.delete(key_or_node=successor)

    def get_successor(self, cur: Node) -> Node:
        if cur.right.is_nil:
            return self.nil
        cur = cur.right
        x = self.nil
        while not cur.is_nil:
            x = cur
            cur = cur.left
        return x

    @staticmethod
    def _get_is_node_left_of_parent(node: Node):
        return node.parent.left.key == node.key

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


bt = BinarySearchTree()


def main():
    n = int(input())
    for i in range(n):
        i = sys.stdin.readline()[:-1]
        if i[0] == 'i':
            key = int(i[7:])
            bt.insert(key=key)
        elif i[0] == 'f':
            key = int(i[5:])
            print('yes' if not bt.find(key).is_nil else 'no')
        elif i[0] == 'd':
            key = int(i[7:])
            bt.delete(key_or_node=key)
        else:
            bt.print_inorder()
            bt.print_preorder()


main()
