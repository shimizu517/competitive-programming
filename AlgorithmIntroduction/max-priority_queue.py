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

    @staticmethod
    def assert_key(t: T):
        assert hasattr(t, "mpq_key") and isinstance(
            t.mpq_key, int
        ), f"{t.__str__} does not implement mpq_key."

    def heap_maximum(self):
        return self.s[0]


players: List[Player] = [
    Player(
        name=names.get_first_name(),
        age=random.randrange(20, 80),
        level=random.randrange(1, 100),
    )
    for _ in range(50)
]
pprint(players)
mpq = MaxPriorityQueue(s=players)
pprint(mpq.s)
