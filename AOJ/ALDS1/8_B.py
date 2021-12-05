import sys


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

    def find(self, key: int) -> bool:
        x = self.root
        while not x.is_nil:
            if x.key == key:
                return True
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return False

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
            print('yes' if bt.find(key) else 'no')
        else:
            bt.print_inorder()
            bt.print_preorder()


main()
