from heapq import heappush, heappop

INF = 10 ** 9


class Dijkstra:
    def __init__(self, l):
        self.d = []
        self.p = []
        self.used = []
        self.l = l

    def execute(self):
        self.initialize_sssp()
        self.d[0] = 0
        q = []
        heappush(q, (0, 0))
        while 0 < len(q):
            _, u = heappop(q)
            if self.used[u]:
                continue
            self.used[u] = True
            for vw in self.l[u]:
                if not self.used[vw[0]]:
                    self.relax(u, vw[0], vw[1])
                    heappush(q, (self.d[vw[0]], vw[0]))
        return self.d

    def initialize_sssp(self):
        for i in range(len(self.l)):
            self.d.append(INF)
            self.p.append(None)
            self.used.append(False)

    def relax(self, u, v, w):
        if self.d[u] + w < self.d[v]:
            self.d[v] = self.d[u] + w
            self.p[v] = u


def main():
    n = int(input())
    adj_l = []
    for _ in range(n):
        u, k, *cv = map(int, input().split())
        adj_l.append([(cv[i * 2], cv[i * 2 + 1]) for i in range(k)])
    d = Dijkstra(l=adj_l)
    for v, _d in enumerate(d.execute()):
        print(f'{v} {_d}')


main()
