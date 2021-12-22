N = 8

NOT_FREE = 0
FREE = 1


class EightQueen:
    def __init__(self, coordinates):
        self.row = [FREE for _ in range(N)]
        self.col = [FREE for _ in range(N)]
        self.dpos = [FREE for _ in range(N * 2 - 1)]
        self.dneg = [FREE for _ in range(N * 2 - 1)]
        for x, y in coordinates:
            self.row[y] = self.col[x] = self.dpos[x + y] = self.dneg[x - y + N - 1] = NOT_FREE

    def execute(self, i):
        if i == N:
            print(self.col, self.row)
            return FREE
        for j in range(N):
            if not (self.col[j] and self.dpos[i + j] and self.dneg[i - j + N - 1]):
                continue
            self.row[i] = self.col[j] = self.dpos[i + j] = self.dneg[i - j + N - 1] = NOT_FREE
            self.execute(i=i + 1)
            self.row[i] = self.col[j] = self.dpos[i + j] = self.dneg[i - j + N - 1] = FREE


def main():
    k = int(input())
    coordinates = []
    for _ in range(k):
        coordinates.append(map(int, input().split()))
    e = EightQueen(coordinates)
    print(e.execute(0))


main()
