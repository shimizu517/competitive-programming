from typing import Optional, List


class Treap:
    class Node:
        def __init__(self, key: Optional[int] = None, priority: int = 0, left=None, right=None, parent=None):
            self.key: int = key
            self.priority: int = priority
            self.left: 'Treap.Node' = left
            self.right: 'Treap.Node' = right
            self.parent: 'Treap.Node' = parent
            self.sum: int = 0  # 部分木のkeyの合計
            self.cnt: int = 1  # 部分木のサイズ

        @property
        def is_nil(self) -> bool:
            return self.key is None

        def __str__(self):
            return f'key: {self.key}, priority: {self.priority}'

    nil = Node()

    def __init__(self):
        self.root: 'Treap.Node' = self.nil

    @staticmethod
    def right_rotate(n: 'Treap.Node'):
        r = n.left
        if not n.parent.is_nil:
            r.parent = n.parent
        n.left = r.right
        if not r.right.is_nil:
            r.right.parent = n
        r.right = n
        if not n.is_nil:
            n.parent = r
        return r

    @staticmethod
    def left_rotate(n: 'Treap.Node'):
        r = n.right
        if not n.parent.is_nil:
            r.parent = n.parent
        n.right = r.left
        if not r.left.is_nil:
            r.left.parent = n
        r.left = n
        if not n.is_nil:
            n.parent = r
        return r

    def insert(self, n: 'Treap.Node', key: int, priority: int):
        if n.is_nil:
            node = self.Node(key=key, priority=priority)
            node.left = node.right = self.nil
            if self.root.is_nil:
                self.root = node
                return node
            else:
                return node
        if key == n.key:
            return n

        if key < n.key:
            n.left = self.insert(n=n.left, key=key, priority=priority)
            if n.priority < n.left.priority:
                n = self.right_rotate(n=n)
        else:
            n.right = self.insert(n=n.right, key=key, priority=priority)
            if n.priority < n.right.priority:
                n = self.left_rotate(n=n)
        return n

    def delete(self, n: 'Treap.Node', key: int):
        if n.is_nil:
            return self.nil
        if key < n.key:
            n.left = self.delete(n=n.left, key=key)
        elif n.key < key:
            n.right = self.delete(n=n.right, key=key)
        else:
            return self._delete(n=n, key=key)

    def _delete(self, n: 'Treap.Node', key: int):
        if n.left.is_nil and n.right.is_nil:
            return self.nil
        elif n.left.is_nil:
            x = self.left_rotate(n=n)
        elif n.right.is_nil:
            x = self.right_rotate(n=n)
        else:
            if n.right.priority < n.left.priority:
                x = self.right_rotate(n=n)
            else:
                x = self.left_rotate(n=n)
        if self.root.key == n.key:
            self.root = x
        return self.delete(n=x, key=key)

    def is_left_of_parent(self, node: 'Treap.Node'):
        return node.parent.left.key == node.key

    def find(self, key: int) -> 'Treap.Node':
        x = self.root
        while not x.is_nil:
            if x.key == key:
                return x
            elif key <= x.key:
                x = x.left
            else:
                x = x.right
        return self.nil

    def print(self):
        print(' ' + ' '.join(map(str, self._get_inorder())))
        print(' ' + ' '.join(map(str, self._get_preorder())))

    def _get_inorder(self) -> List[int]:
        result = []

        def _traverse_inorder(n: 'Treap.Node'):
            if n.is_nil:
                return
            _traverse_inorder(n.left)
            result.append(n.key)
            _traverse_inorder(n.right)

        _traverse_inorder(self.root)
        return result

    def _get_preorder(self) -> List[int]:
        result = []

        def _traverse_preorder(n: 'Treap.Node'):
            if n.is_nil:
                return
            result.append(n.key)
            _traverse_preorder(n.left)
            _traverse_preorder(n.right)

        _traverse_preorder(self.root)
        return result


def main():
    n = int(input())
    treap = Treap()
    for _ in range(n):
        command, *_input = input().split(' ')
        if command == 'insert':
            treap.insert(treap.root, int(_input[0]), int(_input[1]))
        elif command == 'print':
            treap.print()
        elif command == 'find':
            print('yes' if not treap.find(int(_input[0])).is_nil else 'no')
        elif command == 'delete':
            treap.delete(treap.root, int(_input[0]))


main()
