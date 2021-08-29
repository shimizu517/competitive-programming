from collections import defaultdict


class WeightedDisjointSet:
    def __init__(self):
        self.parent = defaultdict(lambda _: None)  # valueはkeyの親
        self.rank = defaultdict(lambda _: 0)
        self.weight = defaultdict(lambda _: 0)

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = None
            self.rank[x] = 0
            self.weight[x] = 0

    def find_set(self, x):
        if self.parent[x] is None:
            return x
        root = self.find_set(x=self.parent[x])
        self.weight[x] += self.weight[self.parent[x]]
        self.parent[x] = root
        return root

    def merge(self, x, y, diff_y_x):
        # find_setで根への累計の重みを計算する。ここで経路圧縮してもよい
        xroot = self.find_set(x)
        yroot = self.find_set(y)
        if xroot == yroot:
            return

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
            self.weight[xroot] += diff_y_x - self.weight[x] + self.weight[y]
        else:
            self.parent[yroot] = xroot
            self.weight[yroot] = -diff_y_x + self.weight[x] - self.weight[y]
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

    def is_same(self, x, y) -> bool:
        if x not in self.parent or y not in self.parent:
            return False
        return self.find_set(x) == self.find_set(y)

    def get_diff(self, x, y):
        if not self.is_same(x=x, y=y):
            raise Exception()
        return self.weight[x] - self.weight[y]


def main():
    n, q = map(int, input().split())
    wds = WeightedDisjointSet()
    for _ in range(q):
        flag, *data = map(int, input().split())
        if flag:
            x, y = data[0], data[1]
            if wds.is_same(x=x, y=y):
                print(wds.get_diff(x=x, y=y))
            else:
                print('?')
        else:
            wds.make_set(x=data[0])
            wds.make_set(x=data[1])
            wds.merge(x=data[0], y=data[1], diff_y_x=data[2])


main()
