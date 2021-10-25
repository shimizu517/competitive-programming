from typing import Any, Optional


# そもそもQueueの使い方間違ってる。consumeするときはdequeueして計算してenqueueし直す！！
class SchedulerQueue:
    def __init__(self, n):
        assert n > 0, 'n has to be more than 0'
        self.n = n + 1
        self.q: Optional[list] = [None] * self.n
        self.head = 0
        self.tail = 0
        self.time = 0
        self.cur = 0
        self.result = []

    def enqueue(self, el):
        if self.is_full:
            raise Exception('cannot enqueue because it is full')
        self.q[self.tail] = el
        self.tail = (self.tail + 1) % self.n

    def dequeue(self) -> Any:
        if self.is_empty:
            raise Exception('cannot dequeue because it is empty')

        el = self.q[self.head]
        self.head = (self.head + 1) % self.n
        return el

    def consume(self, quantum: int) -> Optional[tuple]:
        if self.q[self.cur] is None:
            self.cur = (self.cur + 1) % self.n
        name, remaining_time = self.q[self.cur]
        if remaining_time <= 0:
            self.cur = (self.cur + 1) % self.n
            return
        if remaining_time <= quantum:
            self.result.append([name, remaining_time + self.time])
            self.time += remaining_time
            self.q[self.cur][1] = 0
            return name, self.time
        else:
            self.q[self.cur][1] -= quantum
            self.time += quantum
        self.cur = (self.cur + 1) % self.n

    @property
    def is_empty(self):
        return self.head == self.tail

    @property
    def is_full(self):
        return self.head == (self.tail + 1) % self.n


def main():
    n, q = map(int, input().split())
    sq = SchedulerQueue(n=n)
    for _ in range(n):
        name, time = input().split()
        sq.enqueue(el=[name, int(time)])
    count = 0
    while count != n:
        item = sq.consume(quantum=q)
        if item is None:
            continue
        print(f'{item[0]} {item[1]}')
        count += 1


main()
