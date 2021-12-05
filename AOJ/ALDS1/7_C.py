from typing import Dict, List, Optional, Callable


class Node:
    def __init__(self, _id=None, left: 'Node' = None, right: 'Node' = None):
        self.id = _id
        self.left = left
        self.right = right

    @property
    def is_nil(self):
        return self.id is None

    def __str__(self):
        return f'id: {self.id}, left: {self.left.id}, right: {self.right.id}'


# sentinel node
NIL = Node()


class Tree:
    def __init__(self):
        # id と Nodeオブジェクトのマッピング
        self.node_mapping: Dict[int, Node] = {}
        # 各Nodeオブジェクトの入次数
        self.in_deg = {}

    def add_node(self, _id: int, l_id: Optional[int], r_id: Optional[int]):
        node = self._get_or_create_node(_id=_id)
        self._create_in_deg(node=node)
        l_node = self._get_or_create_node(_id=l_id)
        r_node = self._get_or_create_node(_id=r_id)
        node.left = l_node
        node.right = r_node
        # 入次数を記録
        self._increment_or_create_in_deg(l_node)
        self._increment_or_create_in_deg(r_node)

    def _get_or_create_node(self, _id: Optional[int]) -> Node:
        """
        _idのNodeオブジェクトを登録済みならそのノードを返し、未登録ならオブジェクトを登録して返す
        _id is None の場合は登録せずにNIlを返す
        """
        if _id is None:
            return NIL
        if _id not in self.node_mapping:
            node = Node(_id=_id)
            self.node_mapping[_id] = node
            node.left = NIL
            node.right = NIL
        return self.node_mapping[_id]

    def _create_in_deg(self, node: Node):
        if node.id not in self.in_deg:
            self.in_deg[node.id] = 0

    def _increment_or_create_in_deg(self, node: Node):
        """Nodeの入次数を記録。NILの場合は何もしない"""
        if node.is_nil:
            return
        if node.id not in self.in_deg:
            self._create_in_deg(node=node)
        self.in_deg[node.id] += 1

    def print_ordered_ids(self, order_func: Callable[[Node, List[int]], None]):
        ordered_node_ids: List[int] = []
        root_id = 0
        for _id, _in_deg in self.in_deg.items():
            if _in_deg == 0:
                root_id = _id
                break
        order_func(self.node_mapping[root_id], ordered_node_ids)
        self._print(ordered_node_ids)

    @classmethod
    def order_by_preorder(cls, node: Node, ordered_node_ids: List[int]):
        if node.is_nil:
            return
        ordered_node_ids.append(node.id)
        cls.order_by_preorder(node.left, ordered_node_ids)
        cls.order_by_preorder(node.right, ordered_node_ids)

    @classmethod
    def order_by_inorder(cls, node: Node, ordered_node_ids: List[int]):
        if node.is_nil:
            return
        cls.order_by_inorder(node.left, ordered_node_ids)
        ordered_node_ids.append(node.id)
        cls.order_by_inorder(node.right, ordered_node_ids)

    @classmethod
    def order_by_postorder(cls, node: Node, ordered_node_ids: List[int]):
        if node.is_nil:
            return
        cls.order_by_postorder(node.left, ordered_node_ids)
        cls.order_by_postorder(node.right, ordered_node_ids)
        ordered_node_ids.append(node.id)

    def _print(self, l: List[int]):
        print(' ' + ' '.join(map(str, l)))


def main():
    n = int(input())
    t = Tree()
    root_id = None
    for _ in range(n):
        _id, l_id, r_id = map(int, input().split(' '))
        # ↓最初のノードがrootになる？
        if root_id is None:
            root_id = _id
        l_id = l_id if l_id >= 0 else None
        r_id = r_id if r_id >= 0 else None
        t.add_node(_id=_id, l_id=l_id, r_id=r_id)
    print("Preorder")
    t.print_ordered_ids(order_func=Tree.order_by_preorder)
    print("Inorder")
    t.print_ordered_ids(order_func=Tree.order_by_inorder)
    print("Postorder")
    t.print_ordered_ids(order_func=Tree.order_by_postorder)


main()
