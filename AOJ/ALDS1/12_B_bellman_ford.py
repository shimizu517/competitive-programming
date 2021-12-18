from typing import Dict, Tuple, List, Optional

INF = 10 ** 10


class BellmanFord:
    def __init__(self):
        pass

    def execute(self, adj_list: Dict[int, List[Tuple[int, int]]]):
        self.d: List[int] = []
        self.p: List[Optional[int]] = []
        for _ in adj_list:
            self.d.append(INF)
            self.p.append(None)
        self.d[0] = 0
        for _ in range(len(adj_list) - 1):
            for u, edges in adj_list.items():
                for edge in edges:
                    self.relax(u, edge[0], edge[1])
        for u, edges in adj_list.items():
            for edge in edges:
                if self.d[u] + edge[1] < self.d[edge[0]]:
                    raise Exception("It contains unreachable vertex.")
        return self.d

    def relax(self, u: int, v: int, w: int):
        """
        始点~>uを緩和する
        現在の 始点~>u より 始点~>v->(w)u の方が近ければself.dとself.pを更新
        """
        if self.d[u] + w < self.d[v]:
            self.d[v] = self.d[u] + w
            self.p[v] = u


def main():
    n = int(input())
    adj_list: Dict[int, List[Tuple[int, int]]] = {}
    for _ in range(n):
        vc: List[int]
        u, k, *vc = list(map(int, input().split()))
        adj_list[u] = [(vc[i * 2], vc[i * 2 + 1]) for i in range(len(vc) // 2)]

    for idx, d in enumerate(BellmanFord().execute(adj_list=adj_list)):
        print(f'{idx} {d}')


main()
