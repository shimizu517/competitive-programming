from typing import Any


class Queue:
    def __init__(self, n):
        self.size = n + 1
        self.q = [None] * self.size
        self.head = self.tail = 0

    def enqueue(self, el: Any):
        if self.is_full:
            raise Exception('full')
        self.q[self.tail] = el
        self.tail = (self.tail + 1) % self.size

    def dequeue(self) -> Any:
        if self.is_empty:
            raise Exception('empty')
        head = self.q[self.head]
        self.head = (self.head + 1) % self.size
        return head

    @property
    def is_empty(self):
        return self.head == self.tail

    @property
    def is_full(self):
        return self.head == (self.tail + 1) % self.size


class SchedulerQueue:
    def __init__(self, n):
        assert n > 0, 'n has to be more than 0'
        self.q = Queue(n=n)
        self.time = 0

    def consume_time(self, q):
        name, t = self.q.dequeue()
        if t <= q:
            self.time += t
            return name, self.time
        else:
            t -= q
            self.time += q
            self.q.enqueue(el=[name, t])
            return None


def main():
    n, q = map(int, input().split())
    sq = SchedulerQueue(n=n)
    for _ in range(n):
        name, time = input().split()
        sq.q.enqueue(el=[name, int(time)])
    while not sq.q.is_empty:
        item = sq.consume_time(q=q)
        if item is None:
            continue
        print(f'{item[0]} {item[1]}')


main()
