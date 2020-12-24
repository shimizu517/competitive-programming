import random
from dataclasses import dataclass
import names
from typing import TypeVar, List
from pprint import pprint


@dataclass
class Player:
    name: str
    age: int
    level: int

    @property
    def mpq_key(self):
        return self.age + self.level


T = TypeVar("T")


@dataclass
class MaxPriorityQueue:
    s: List[T]

    def __post_init__(self):
        for el in self.s:
            self.assert_key(el)
        self._build_max_heap()

    @staticmethod
    def assert_key(t: T):
        assert hasattr(t, "mpq_key") and isinstance(
            t.mpq_key, int
        ), f"{t.__str__} does not implement mpq_key."

    def heap_maximum(self):
        return self.s[0]

    def extract_maximum(self):
        result = self.s[0]
        self.s[0] = self.s[len(self.s) - 1]
        del self.s[len(self.s) - 1]
        self._max_heapify(0)
        return result

    def _max_heapify(self, p_i):
        left_i = p_i * 2 + 1
        right_i = p_i * 2 + 2
        if left_i > len(self.s) - 1:
            return

        max_i = p_i
        if self.s[left_i].mpq_key > self.s[max_i].mpq_key:
            max_i = left_i
        if right_i < len(self.s) and self.s[right_i].mpq_key > self.s[max_i].mpq_key:
            max_i = right_i

        if max_i != p_i:
            self.s[max_i], self.s[p_i] = self.s[p_i], self.s[max_i]
            self._max_heapify(max_i)

    def _build_max_heap(self):
        for i in range((len(self.s) - 1) // 2, -1, -1):
            self._max_heapify(i)


players: List[Player] = [
    Player(
        name=names.get_first_name(),
        age=random.randrange(20, 80),
        level=random.randrange(1, 100),
    )
    for _ in range(50)
]

mpq = MaxPriorityQueue(s=players)

for p in mpq.s:
    print(p.mpq_key, p)
