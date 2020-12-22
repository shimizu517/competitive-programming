import math
from typing import Counter
import random


class Heap:
    def __init__(self, l: list) -> None:
        self.l = l

    def _max_heapify(self, idx: int, last_i: int):
        left_i = 2 * idx + 1
        right_i = 2 * idx + 2
        if left_i > last_i:
            return

        _max_i = idx
        if self.l[left_i] > self.l[_max_i]:
            _max_i = left_i
        if right_i <= last_i and self.l[right_i] > self.l[_max_i]:
            _max_i = right_i
        if _max_i != idx:
            self.l[_max_i], self.l[idx] = self.l[idx], self.l[_max_i]
            self._max_heapify(_max_i, last_i)

    def _build_max_heap(self):
        for i in range(math.floor(len(self.l) // 2) - 1, -1, -1):
            self._max_heapify(i, len(self.l) - 1)
        return self.l

    def heap_sort(self):
        result = []
        self._build_max_heap()
        heap_last_i = len(self.l) - 1
        for _ in range(len(self.l) - 1):
            self.l[heap_last_i], self.l[0] = self.l[0], self.l[heap_last_i]
            heap_last_i -= 1
            self._max_heapify(0, heap_last_i)


data = random.choices(range(100), k=110)
print(data)

h = Heap(l=data)
h.heap_sort()
print(h.l)
