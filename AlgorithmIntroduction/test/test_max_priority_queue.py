from os import name
from ..max_priority_queue import *


players: List[Player] = [
    Player(
        name=names.get_first_name(),
        age=random.randrange(20, 80),
        level=random.randrange(1, 100),
    )
    for _ in range(51)
]

players2: List[Player] = [
    Player(
        name=names.get_first_name(),
        age=random.randrange(20, 80),
        level=random.randrange(1, 10),
    )
    for _ in range(100)
]

ZERO_PLAYER = Player(name="test", age=0, level=0)

human1: List[Human] = [
    Human(
        name=names.get_first_name(),
        mpq_key=random.randrange(1, 500),
    )
    for _ in range(100)
]

human2: List[Human] = [
    Human(
        name=names.get_first_name(),
        mpq_key=random.randrange(1, 500),
    )
    for _ in range(101)
]


def is_correct_max_heap(mpq):
    for idx, el in enumerate(mpq.s):
        left_el = ZERO_PLAYER
        right_el = ZERO_PLAYER
        if idx * 2 + 1 <= len(mpq.s) - 1:
            left_el = mpq.s[idx * 2 + 1]
        if idx * 2 + 2 <= len(mpq.s) - 1:
            right_el = mpq.s[idx * 2 + 2]
        if not (el.mpq_key >= left_el.mpq_key and el.mpq_key >= right_el.mpq_key):
            print(el, left_el, right_el)
            return False
    return True


def test_build_max_heap():
    mpq1 = MaxPriorityQueue(s=players)
    mpq2 = MaxPriorityQueue(s=players2)
    mpq3 = MaxPriorityQueue(s=human1)
    mpq4 = MaxPriorityQueue(s=human2)
    mpqs = [mpq1, mpq2, mpq3, mpq4]
    for mpq in mpqs:
        assert is_correct_max_heap(mpq=mpq)


def test_extract_max_heap():
    mpq1 = MaxPriorityQueue(s=players)
    mpq2 = MaxPriorityQueue(s=players2)
    mpq3 = MaxPriorityQueue(s=human1)
    mpq4 = MaxPriorityQueue(s=human2)
    mpqs = [mpq1, mpq2, mpq3, mpq4]
    for mpq in mpqs:
        before_len = len(mpq.s)
        maximum = max(map(lambda x: x.mpq_key, mpq.s))
        assert mpq.extract_maximum().mpq_key == maximum
        maximum2 = max(map(lambda x: x.mpq_key, mpq.s))
        # extract_maximumで要素が一つ削除されており、ことを確認
        assert mpq.heap_maximum().mpq_key == maximum2 and before_len != len(mpq.s)


def test_heap_increase_key():
    mpq3 = MaxPriorityQueue(s=human1)
    mpq4 = MaxPriorityQueue(s=human2)
    mpqs = [mpq3, mpq4]
    for _ in range(100):
        for mpq in mpqs:
            mpq.heap_increase_key(
                i=random.randrange(1, len(mpq.s) - 1),
                mpq_el=Human(
                    name=names.get_first_name(), mpq_key=random.randrange(1, 1000)
                ),
            )
            assert is_correct_max_heap(mpq=mpq)


def test_max_heap_insert():
    mpq3 = MaxPriorityQueue(s=human1)
    mpq4 = MaxPriorityQueue(s=human2)
    mpqs = [mpq3, mpq4]
    for _ in range(100):
        for mpq in mpqs:
            mpq.max_heap_insert(
                mpq_el=Human(
                    name=names.get_first_name(), mpq_key=random.randrange(1, 1000)
                ),
            )
            assert is_correct_max_heap(mpq=mpq)
