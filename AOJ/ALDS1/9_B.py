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


def main():
    _ = int(input())
    keys = list(map(int, input().split(' ')))
    h = Heap.build_max_heap(keys)
    print(' ' + ' '.join(map(str, h.nodes)))


main()
