import sys
from typing import List


class Heap:
    def __init__(self):
        self.nodes: List[int] = []

    @staticmethod
    def get_parent_idx(idx: int):
        return (idx - 1) // 2

    @staticmethod
    def get_left_idx(idx: int):
        return idx * 2 + 1

    @staticmethod
    def get_right_idx(idx: int):
        return idx * 2 + 2

    @classmethod
    def build_max_heap(cls, keys: List[int]) -> 'Heap':
        start_i = cls.get_parent_idx(len(keys) - 1)
        for idx in range(start_i, -1, -1):
            cls._max_heapify(keys, idx)
        h = cls()
        h.nodes = keys
        return h

    @classmethod
    def _max_heapify(cls, keys: List[int], idx: int):
        l_id = cls.get_left_idx(idx)
        r_id = cls.get_right_idx(idx)
        largest_id = idx
        if l_id < len(keys) and keys[largest_id] < keys[l_id]:
            largest_id = l_id
        if r_id < len(keys) and keys[largest_id] < keys[r_id]:
            largest_id = r_id
        if largest_id != idx:
            keys[largest_id], keys[idx] = keys[idx], keys[largest_id]
            cls._max_heapify(keys, largest_id)

    def insert(self, key: int):
        self.nodes.append(key)
        cur_id = len(self.nodes) - 1
        p_id = self.get_parent_idx(cur_id)
        while cur_id != 0 and self.nodes[p_id] < self.nodes[cur_id]:
            self.nodes[cur_id], self.nodes[p_id] = self.nodes[p_id], self.nodes[cur_id]
            cur_id = p_id
            p_id = self.get_parent_idx(cur_id)

    def extract_max(self) -> int:
        if len(self.nodes) == 0:
            raise Exception('Heap under flow')
        result = self.nodes[0]
        self.nodes[0] = self.nodes[len(self.nodes) - 1]
        del self.nodes[len(self.nodes) - 1]
        self._max_heapify(self.nodes, 0)
        return result


def main():
    h = Heap()
    import sys
    for _input in sys.stdin:
        if _input == 'end':
            break
        if _input[0] == 'i':
            h.insert(int(_input[7:-1]))
        elif _input[:2] == 'ex':
            print(h.extract_max())


main()
