N = 8

NOT_FREE = 1
FREE = -1


class EightQueen:
    def __init__(self, rcs):
        self.row = [FREE for _ in range(N)]
        self.col = [FREE for _ in range(N)]
        self.dpos = [FREE for _ in range(N * 2 - 1)]
        self.dneg = [FREE for _ in range(N * 2 - 1)]
        for r, c in rcs:
            self.row[r] = self.col[c] = self.dpos[r + c] = self.dneg[r - c + N - 1] = NOT_FREE

    def execute(self, i):
        if i == N:
            print(self.col, self.row)
            return FREE
        for j in range(N):
            if self.col[j] == FREE and self.dpos[i + j] == FREE and self.dneg[i - j + N - 1] == FREE:
                self.row[i] = j
                self.col[j] = self.dpos[i + j] = self.dneg[i - j + N - 1] = NOT_FREE
                self.execute(i=i + 1)
                self.row[i] = self.col[j] = self.dpos[i + j] = self.dneg[i - j + N - 1] = FREE


def main():
    k = int(input())
    rcs = []
    for _ in range(k):
        rcs.append(map(int, input().split()))
    e = EightQueen(rcs)
    e.execute(0)


main()
