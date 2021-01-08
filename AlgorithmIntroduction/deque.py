class HeadOverFlow(Exception):
    pass


class TailOverFlow(Exception):
    pass


class Deque:
    def __init__(self):
        self.tail: int = 0  # 先頭の要素の次のポインタ。tail_enqueueで右に要素を追加し、tailは右に動く。
        self.head: int = 0  # 末尾の要素のポインタ。head_enqueueで左に要素を追加し、headは左に動く。
        self.n: int = 10  # n-1個の要素を格納する
        self.arr: list = [None] * self.n

    def tail_enqueue(self, v: int):
        if (self.tail + 1) % self.n == self.head % self.n:
            raise TailOverFlow()
        self.arr[self.tail] = v
        self.tail = (self.tail + 1) % self.n

    def head_enqueue(self, v: int):
        """
        配列arrの左に要素を追加していく
        self.headをデクリメントして、その位置に要素を追加する
        つまり、self.headの位置には空の時以外は要素が存在する
        """
        if self.tail % self.n == (self.head - 1) % self.n:
            raise HeadOverFlow()
        self.head = (self.head - 1) % self.n
        self.arr[self.head] = v

    def tail_dequeue(self):
        if self.tail == self.head:
            raise Exception()
        self.tail = (self.tail - 1) % self.n
        return self.arr[self.tail]

    def head_dequeue(self):
        if self.tail == self.head:
            raise Exception()
        result = self.arr[self.head]
        self.head = (self.head + 1) % self.n
        return result
