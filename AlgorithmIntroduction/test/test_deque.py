from ..deque import *
import pytest

print("tet")


def test_head_enqueue():
    dq = Deque()
    dq.head_enqueue(1)
    assert dq.head_dequeue() == 1, "head_dequeue not working"


def test_tail_enqueue():
    dq = Deque()
    dq.tail_enqueue(1)
    assert dq.head_dequeue() == 1, "tail_dequeue not working"


def test_tail_enqueue_and_dequeue():
    dq = Deque()
    for i in range(2):
        dq.tail_enqueue(i)
    for i in range(2, 5):
        dq.head_enqueue(i)
    for _ in range(5):
        dq.head_dequeue()
    with pytest.raises(Exception):
        assert dq.head_dequeue()


def test_tail_dequeue():
    dq = Deque()
    dq.head_enqueue(1)
    dq.head_enqueue(2)
    assert dq.tail_dequeue() == 1, "tail_dequeue not working"
    assert dq.tail_dequeue() == 2, "tail_dequeue not working"
    dq.tail_enqueue(3)
    dq.tail_enqueue(4)
    dq.head_enqueue(5)
    dq.tail_enqueue(6)
    assert dq.tail_dequeue() == 6, "tail_dequeue not working"
    assert dq.tail_dequeue() == 4, "tail_dequeue not working"
    assert dq.tail_dequeue() == 3, "tail_dequeue not working"
    assert dq.tail_dequeue() == 5, "tail_dequeue not working"


def test_head_dequeue():
    dq = Deque()
    dq.head_enqueue(1)
    dq.tail_enqueue(2)
    assert dq.head_dequeue() == 1, "head_dequeue not working"
    assert dq.head_dequeue() == 2, "head_dequeue not working"
    dq.tail_enqueue(3)
    dq.tail_enqueue(4)
    dq.head_enqueue(5)
    dq.tail_enqueue(6)
    assert dq.head_dequeue() == 5, "tail_dequeue not working"
    assert dq.head_dequeue() == 3, "tail_dequeue not working"
    assert dq.head_dequeue() == 4, "tail_dequeue not working"
    assert dq.head_dequeue() == 6, "tail_dequeue not working"


def test_tail_enqueue_overflow():
    dq = Deque()
    for i in range(dq.n - 1):
        dq.tail_enqueue(i)
    print(dq.head, dq.tail)
    with pytest.raises(TailOverFlow):
        dq.tail_enqueue(1)


def test_head_enqueue_overflow():
    dq = Deque()
    for i in range(dq.n - 1):
        dq.head_enqueue(i)
    print(dq.head, dq.tail)
    with pytest.raises(HeadOverFlow):
        dq.head_enqueue(1)


def test_head_dequeue_underflow():
    dq = Deque()
    with pytest.raises(Exception):
        dq.head_dequeue()
